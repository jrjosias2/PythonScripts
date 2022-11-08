#Errros & Exceptions Try, Exception

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(3)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

try:
    a = 5/0
except Exception as e:
    print(e)

try:
    a = 5/1
    b = a + 4

except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print(a, b)
finally:
    a = 0
    b = 0
    print('Cleaning up block to make sure everything stays fine ahead')

x = -5
assert(x>=0), f"valor de x deve ser positivo, x = {x}"

if x < 0:
    raise Exception(f"X deve ser um valor positivo, valor recebido foi {x}")
