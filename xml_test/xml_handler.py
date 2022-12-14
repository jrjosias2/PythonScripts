import os
import sys
import xml.etree.ElementTree as ET
import zipfile as zip
from datetime import datetime, timedelta

import pandas as pd
import requests

'''
Requirements.txt
pip updated pandas and boto3 to the latest
pip installed lxml

-----------------------------

Datetime parameter are as follows:
-> Sales: daily | weekly | monthly | quarter <params><Fecha_Desde>{datetime.function}</Fecha_Desde><Fecha_Hasta>{datetime.function}</Fecha_Hasta></params>
-> Retailer: weekly <params><Fecha_Desde>{datetime.function}</Fecha_Desde><Fecha_Hasta>{datetime.function}</Fecha_Hasta></params>
-> Inventory: daily <params></params> 'NOT NEED TO SPECIFY ANY DATE'
'''

#Replace these values later on for S3 settings established at task_config.json file
RAW_INV_PATH = 'cdt\\routines\\uruguay_sales_sellthrough_fortylex\\tasks\\api_integration\\python\\xml_files\\raw\\inventory\\'
RAW_SLS_PATH = 'cdt\\routines\\uruguay_sales_sellthrough_fortylex\\tasks\\api_integration\\python\\xml_files\\raw\\sales\\'
RAW_RTL_PATH = 'cdt\\routines\\uruguay_sales_sellthrough_fortylex\\tasks\\api_integration\\python\\xml_files\\raw\\retailers\\'

CURATED_INV_PATH = 'cdt\\routines\\uruguay_sales_sellthrough_fortylex\\tasks\\api_integration\\python\\xml_files\\curated\\inventory\\'
CURATED_SLS_PATH = 'cdt\\routines\\uruguay_sales_sellthrough_fortylex\\tasks\\api_integration\\python\\xml_files\\curated\\sales\\'
CURATED_RTL_PATH = 'cdt\\routines\\uruguay_sales_sellthrough_fortylex\\tasks\\api_integration\\python\\xml_files\\curated\\retailers\\'

INV_AQV_PATH = CURATED_INV_PATH
SLS_AQV_PATH = CURATED_SLS_PATH
RTL_AQV_PATH = CURATED_RTL_PATH

FLG_FILE = 'cdt\\routines\\uruguay_sales_sellthrough_fortylex\\tasks\\api_integration\\python\\xml_files\\curated\\processed\\'

BITSYS_API = "https://190.64.90.131/WsGenQueryFacade/wsGenQuery.asmx/GetData"

def check_API_Response(api_dic_parameters, raw_path):
    
    response = requests.get(url=BITSYS_API, params= api_dic_parameters, auth=('usrBitWsFacade', 'Jyj#Lex++Forti2021'), timeout=999, verify=False)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        sys.exit( "Error: " + str(e))

    with open(raw_path, encoding='utf-8', mode='w+') as raw_xml:
        raw_xml.write(response.text)

def xml_to_df_parser(file_source, file_dest, archiving_path):

    #07-Nov-2022 Tem que padronizar o arquivo primeiro, remover o namespace, substituir os chars por < >
    xml_content = ''
    file_tgt_name = file_source.split('\\')[-1].replace('raw', 'curated')
    file_dest += file_tgt_name
 
    with open(file_source, encoding='utf-8', mode='r+') as fin:
        xml_content = fin.read()
        xml_content = xml_content.replace('&lt;', '<')
        xml_content = xml_content.replace('&gt;', '>')
        xml_content = xml_content.replace('<string xmlns="http://wsGenQueryFacade/">', '')
        xml_content = xml_content.replace('</string>', '')

    #salvar o arquivo no diretorio de dev curated para diferenciar entre o arquivo original e o manipulado, para então criar o dataframe
    with open(file_dest, encoding='utf-8', mode='w+') as fout:
        fout.write(xml_content)

        #Check with Beatriz or Ligia after if there's some file rotating rule for this FlagFile
        size = os.path.getsize(FLG_FILE + "FLAG_CON_PY_ETL.txt") / 1024

        with open(FLG_FILE + "FLAG_CON_PY_ETL.txt", encoding='utf-8', mode='a+') as flg:

            timestamp = datetime.now()
            tgt_file = str(file_dest).split('\\')[-1]

            flg.write(f"XML file: {tgt_file} was processed parsed and handled withouth errors at timestamp {timestamp}\n")
    
    # 10-Nov - Create the zip File at "Backup Folder" on landing layer renaming the file with the timestamp, S3 retention/archive period of 1 year.
    file_zip = ''
    with zip.ZipFile(INV_AQV_PATH + file_tgt_name.replace('xml', 'zip'), mode='x') as myzip:
        myzip.writestr(file_tgt_name, data=xml_content, compress_type=zip.ZIP_STORED)

    return pd.read_xml(file_dest)
    
# actual date
base = datetime.today()
# if you need to extract monthly or quartely data from API, you will need to change to a specific date
# replace with eighth day to run monthly
# base = base.replace(day=8)
# replace with october to run quarterly extraction
# base = base.replace(month=10)

base_import = base - timedelta(days=1) 
expectedrange = 2 #Set the minimum of 2 days of data range.

#Generate date list between specified dates
#Sales Period Range.
if (base.day == 8): #Check if date is 8th of a month.

    # Quarter Case
    if (base.month == 1) or (base.month == 4) or (base.month == 7) or (base.month == 10): #Quarter end Periods
        prev_quarter_ref = base - timedelta(days=90)
        start_day_of_prev_quarter = prev_quarter_ref.replace(day=1)
        expectedrange = (base - start_day_of_prev_quarter).days
    
    else:
        prev_month_ref = base - timedelta(days=30)
        start_day_of_prev_month = prev_month_ref.replace(day=1)
        expectedrange = (base - start_day_of_prev_month).days 

elif (base.weekday() == 2): #At Wednesday loads the last week as period range.
    start_previous_week = base - timedelta(days=base.weekday(), weeks=1)
    expectedrange = (base - start_previous_week).days + 5   

else:
    expectedrange = 2

#Reference for Sales to Get the day before (e.g today 10-Nov, date_list_sls[08-Nov, 09-Nov]), week, month or quarter before
date_list_sls = [(base_import - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(expectedrange)]

#Retailers timespan is 7.
date_list_rtl = [(base_import - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(7)] 

RAW_INV_PATH += "raw_inventory_" + str(base.year) + str(base.month) + str(base.day) + ".xml"
RAW_RTL_PATH += "raw_retailers_" + str(date_list_rtl[-1]).replace('-','') + "_to_" + str(date_list_rtl[0]).replace('-','') + ".xml"
RAW_SLS_PATH += "raw_sales_"     + str(date_list_sls[-1]).replace('-','') + "_to_" + str(date_list_sls[0]).replace('-','') + ".xml"

INV_PARAMS = {"KeyCode": "INVENTARIO_JNJ", "parameters": "<params></params>"}
SLS_PARAMS = {"KeyCode": "VENTAS_JNJ",     "parameters": f"<params><Fecha_Desde>{str((date_list_sls[len(date_list_sls)-1]).replace('-', ''))}</Fecha_Desde><Fecha_Hasta>{str((date_list_sls[0]).replace('-', ''))}</Fecha_Hasta></params>"}
RTL_PARAMS = {"KeyCode": "CLIENTES_JNJ",   "parameters": f"<params><Fecha_Desde>{str((date_list_rtl[len(date_list_rtl)-1]).replace('-', ''))}</Fecha_Desde><Fecha_Hasta>{str((date_list_rtl[0]).replace('-', ''))}</Fecha_Hasta></params>"}

check_API_Response(INV_PARAMS, RAW_INV_PATH)
check_API_Response(SLS_PARAMS, RAW_SLS_PATH)
check_API_Response(RTL_PARAMS, RAW_RTL_PATH)

df_inv = xml_to_df_parser(RAW_INV_PATH, CURATED_INV_PATH, INV_AQV_PATH)
df_sls = xml_to_df_parser(RAW_SLS_PATH, CURATED_SLS_PATH, SLS_AQV_PATH)
df_rtl = xml_to_df_parser(RAW_RTL_PATH, CURATED_RTL_PATH, RTL_AQV_PATH)

print(df_inv.isnull().sum())
df_inv.fillna('-9', inplace=True)
