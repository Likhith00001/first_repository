'''#variables
print("hello world")
a=1
b='hello'
c=2.2
g=35e3
d=True
e=3+1j#complex
f=None
h=''''fgfsf,fdf,htdtf,jfyf,hgf''''
print(h)
print(type(e))
#type function
print(type(a))
#assinging variable
x,y,z="a","b","c"
print(x)
print(y)
print(z)
x=y=z="orange"
print(x)
print(y)
print(z)
#concatinating string
x="aw"
y="hd"
z="hde"
print(x+y+z)
#globle and local varible
x="aws"#globle
def myfun():
    x="sql"#locle
    print("local",x)
myfun()
print("globle",x)
#making local to globle
x="aws"#globle
def myfun():
    global x
    x="sql"#locle
    print("local",x)
myfun()
print("globle",x)
#imperaltypecasting
a=1
b=2.34
c="4"
print("float to int",int(b))
print("string to int",int(c))
#emperaltypecasting
list1=[1,'3','dhj',[2,'dh']]
print(type(list1))
tuple1={1,'3','dhj',2,'dh'}
print(type(tuple1))
dict1={'a':1,'d':2}
print(type(dict1))'''

''''#string as array as evry index accesable
a='python'
print(a[0],a[5])
b=''''''x5cstudy_Material
py1.py' ;a1e1aa92-cad0-4ba4-
a4b4-843fa30aa79ep n'''
'''for i in b:
    print(i)'''

#lenth and indexing
''''a='heloo,world'
print(len(a))
print(a[0:6])#start include and end -1 take index nummbering
print(a[2:6])
print(a[:6])# it will take atomatic 0
print(a[0:])#take end number
print (a[0:-4])#reverse indexing skip the last index
print(a[-5:8])#reverse indexing skip the first index
#both same
print(a[-4:len(a)-1])
print(a[-1:-4])'''
n="harry1"
print("dhdh2",n[-4:-2])
print(n[-1:len(n)-3])
print(n[-3:-1])
'''for i in range(1,21):
    for j in range(1,11):
        print(i,' X ',j,' = ',i*j )'''