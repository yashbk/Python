#!/usr/bin/python3
#dictionary
'''
syntax :
variable_name = {key:value}  #key must be a immutable datatype but value can be any type
'''
d={"j":[1,2]}
print(d)

d={"A":"Apple","a":"Apple"}
print(d)

#dictionaries cannot have two items with the same key:
d={"A":"Apple","A":"Ant"}
print(d)

#Dictionaries keys are case sensitive:
d={"A":"Apple","a":"Aircraft"}
print(d)

#items can be added using key as index:
d={"A":"Ant","B":"Bat"}
d["C"]="Cat"
print(d)

dir(d)#methods

#methods
#clear
d={1:"one"}
print(d)
d.clear()
print(d)

#copy()
d={1:"one"}
x=d.copy()
print(x)

#fromkeys(seq[,v])
d={1:"one",2:"two",3:"three"}
x=dict.fromkeys(d)
print(x)

#get(key[,d])
d={'Brand':'Xiaomi','model':'redmi','launced in india':'yes'}
x=d.get('B')
print(x)

#items()
d={'Brand':'Xiaomi','model':'redmi','launced in india':'yes'}
x=d.items()
print(x)

#keys()
d={'Brand':'Xiaomi','model':'redmi','launced in india':'yes'}
x=d.keys()
print(x)

#values()
d={'brand':'Xiaomi','model':'Redmi'}
x=d.values()
print(x)

#del
d={'brand':'Xiaomi','model':'Redmi'}
del d['brand']
print(d)

#pop(key[,d])
d={'Brand':'Xiaomi','model':'redmi','launced in india':'yes'}
x=d.pop('model')
print(x)

#popitems()
d={'Brand':'Xiaomi','model':'redmi','launced in india':'yes'}
x=d.popitem()
print(x)

#setdefault(key[,d])
d={'brand':'Xiaomi'}
x=d.setdefault('model','Redmi')
print(x)

#update([other])
d={'brand':'Xiaomi','model':'Redmi'}
x={'launced in india':'yes'}
print(x)
d.update(x)
print(d)
