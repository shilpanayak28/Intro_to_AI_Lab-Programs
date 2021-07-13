s=True
t=True
a=not(s or t)
b= s and t
c=t or (not t)
d=not((not s or s) and (not s or s))
e=not(not s) or (not t)
print (a)
print (b)
print (c)
print (d)
print (e)
if a==b:
    print("a entailes b")
else :
    print("a does not entail b")
if a==c:
    print("a entailes c")
else :
    print("a does not entail c")
if a==d:
    print ("a entailes d")
else :
    print("a does not entail d")
if a==e:
    print ("a entailes e")
else:
    print("a does not  entail e")
