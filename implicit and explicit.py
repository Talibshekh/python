          #implicit type convertion

# In the implicit type convertion,python automatically converts one data into another data type

a = 5
b = 2
value = a/b
print(value)
print(type(value))

#python hamesa dhyan rakhta aapka data loss na ho
# int se badiya hai float ka value
x = 10
y = 5.5
total = x + y
print(total)
print(type(total))

#ek int or str apas me concatinate ya jod nhi skte hamesa error aaye ga'''
'''q = 20
u = '10'
r = q + u
print(r)'''

'''m = 20
n = 'talib'
t = m + n
print(t)'''

        #explicit type conversion

# In the cast/Explicit type conversion,programmer convert one data type into another data type

#int
#float
#str
#boolean
#conplex (n)
#list
#tuple
#bin yani binary
#oct or octal
#hex or hexa

a1 = 5
b1 = 2
value = a1/b1
int_value = int(value)
print(int_value)

num = 20
num1 = '10'
value = num + int(num1)
print(value)

 # float to Integer

n1 = 10.35
vn = int(n1)
print(vn)
print(type(vn))

 # integer to Float

n2 = 10
vn1 = float(n2)
print(vn1)
print(type(vn1))

