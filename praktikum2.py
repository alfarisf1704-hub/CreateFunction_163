import math

def ConvertTemperature (value,unit):
    if unit =="C":
        print((value-32) * 5/9)
    elif unit =="F":
        print((value*9/5)+32)
    else :
        print("wrong unite")
    return

print ("----Konversi suhu----")
input_value = float(input("Masukkan value : "))
input_suhu = input("Masukkan suhu : ")

ConvertTemperature(value = input_value, unit = input_suhu)

sum = lambda p, r: math.pi*(r*r)

r = float(input ("Masukkan jari jari : "))
print ("value of Circle area : ", sum (math, r))





