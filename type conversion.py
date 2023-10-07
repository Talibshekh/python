#data type or type of data

#int (6)
#float   (2.5)
#string   ("talib") single or double
#boolean   ( True or False)

       #int

data = 5
data_type = type(data)
#print(type(data))
print(data_type)

   #float

data1 = 2.6
data1_type = type(data1)
print(data1_type)
#print(type(data1))

    #string

data2 = "talib"
#print(type(data2))
data2_type = type(data2)
print(data2_type)

        #boolean

data3 = True
data3_type = type(data3)
print(data3_type)
#print(type(data3))


num = 1
result = num + 1
print(result)

#sring or number joda nhi ja skta

'''num = "1"
result = num + 1
print(result)
ab hum log print krege to error
#plus sign kab kaam krta jab dono data same ho ya to dono string ho ya dono numerical ho'''

num1 = "1"
result = num1 + "1"
print(result)
#yaha do string add ho raha is liye 11 aaya result

    #inbuild funtion

num2 = "1" #isko hume int banana ho to int funtion ko aplly kre ge
result = int(num2) + 1
print(result)

#kisi data ko convert krna hoto ek dusre me
#int
#float
#sri
#bool


        #bool

a = "false"
#print(type(a))
a = bool(a)
print(a)

#rule "",0,none else true