import os

stream = os.popen('aws s3 ls s3://snowpipe-examples/csv/employee_data_1.csv --summarize --human-readable')
output = stream.read()
print(f'Saida geral eh:', output)
i_output = float(output[83:87])
print(i_output * 1000000)