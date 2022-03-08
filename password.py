#############################

#PROJECT : PASSWORD GENERATOR

#Language :English
  
#Turkey ID(identification) number SIBLING FINDER

#basic and safe password generator

#Contact me  on ;

#Telegram  : Zafiyetsiz0
#Instagram : Zafiyetsiz
#Discord   : Zafiyetsiz#4172

##############################

import random
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper  = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numb   = ["1","2","3","4","5","6","7","8","9","0"]
symb   = ["!","@","#","%","=","+",";"]

a1=random.choice(letter)
b2=random.choice(numb )
c3=random.choice(letter)
d4=random.choice(numb )
e5=random.choice(letter)
f6=random.choice(upper)
g7=random.choice(numb )
h8=random.choice(upper)
i9=random.choice(numb )
j10=random.choice(upper)
k11=random.choice(numb)
l12=random.choice(symb)
m13=random.choice(numb)
n14=random.choice(numb)
o15=random.choice(symb)
p16=random.choice(letter)
q17a1=random.choice(upper)
r18a1=random.choice(letter)
s19a1=random.choice(numb)
t19a1=random.choice(letter)
u20a1=random.choice(symb)
v21a1=random.choice(upper)



shuffle=(a1+b2+c3+d4+e5+f6+g7+h8+i9+j10+k11+l12+m13+n14+o15
+p16+q17a1+s19a1+t19a1+u20a1+v21a1)


print("your password is :")

print(shuffle)

x=open("passwords.txt" , "a")

x.write("*************")
x.write(shuffle)
x.write("*************")

x.close()
