#jo funtion class k ander bnta use hum method bolte hai

    #len() ye funtion hai

    # jo funtion dot laga k call ho raha ho use method bolege

     # str.lower()

text = "my name is talib shekh"
print(text.upper())

text2 ="My name is Talib shekh"
print(text.lower())

  #title har word ka pahla letter capital kr dega

text3 = "my name is talib shekh"
print(text3.title())

  #strip ka kaam hai left right ka space ko htadena

tex = "    my name is talib shekh     "
print(tex)

new_tex = tex.strip()

print(new_tex)

tex1 ="   my name is talib shekh    "
print(tex1.lstrip)

tex2 = "    my name is talib shekh     "
print(tex2.rstrip)


  #find method

rex = " my name is talib shekh"
new_rex = rex.find("tal")
print(new_rex)


       #replace

'''rex2 = "my name is talib shekh"
new_tex = rex2.replace("t","d")          #("my","your")
print(new_tex)'''


       #answer in true or flase , polian variable

rex2 = "my name is talib shekh"
new_rex2 = "name" in rex
print(new_rex2)

rex3 = "my name is talib shekh"
new_rex3 ="your" in rex3
print(new_rex3)

rex4 = "my name is talib shekh"
new_rex4 ="your" not in rex4
print(new_rex4)