data = input("Enter the temperature along with it's unit: ")
value = int(data[0:-1])
unit = data[-1]
def c_others(c_value):
    k_value = c_value + 273.15
    f_value = ((9/5)* c_value)+ 32
    print("{}C = {:.2f}F".format(c_value,f_value))
    print("{}C = {:.2f}K".format(c_value,k_value))

def f_others(f_value):
    c_value = (f_value - 32) * 5/9
    k_value = c_value + 273.15
    print("{}F = {:.2f}C".format(f_value,c_value))
    print("{}F = {:.2f}K".format(f_value,k_value))


def k_others(k_value):
    c_value = k_value - 273.15
    f_value = ((9/5)* c_value)+ 32
    print("{}K = {:.2f}C".format(k_value,c_value))
    print("{}K = {:.2f}F".format(k_value,f_value))

units_list = ['c','C','f','F','k','K']

if (unit in units_list) and (unit == 'c' or unit == 'C'):
    c_others(value)
elif (unit in units_list) and (unit == 'f' or unit == 'F'):
    f_others(value)
elif (unit in units_list) and (unit == 'k' or unit == 'K'):
    k_others(value)
else :
    print("Enter a valid input")

