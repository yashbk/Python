#equality operator ==

line1="I am in thundersoft"  
line2="I am in thundersoft"
if line1==line2:
    print("same")
else:
    print("different")
    
    
#built-in string method

line1="I am yashaswini"   
line2="I am yashu"
if line1 in line2:
    print("same")
else:
    print("different")
    
    
#find()and index()

line1="i am yashaswini"
line2="yashu"
print(line1.find(line2))

line1="i am yashaswini"
line2="yashu"
print(line1.index(line2))

#re.compile()

#import re.compile
import re
text_to_search="abcdefghijklmnopqrstuvwxyz"
pattern=re.compile(r'abc')      #raw data
res=re.match(pattern,text_to_search)
print(res)
print(type(pattern))
print(pattern)

#re.match()
import re
text_to_search="abcdefghijklmnopqrstuvwxyz"
pattern=re.compile(r'abc') #raw data
res=re.match(pattern,text_to_search)
print(res)
res=re.match(pattern,text_to_search)
print(pattern)

#re.search
import re
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
pattern=re.compile(r'abc') #raw data
res=re.match(pattern,text_to_search)
print(res)
res=re.search(pattern,text_to_search)
print(res)

#re.finder()
import re
text_to_search="abcdefghijklabcmnopqrstuvwxyz"
pattern=re.compile(r'abc') #raw data
res=re.finditer(pattern,text_to_search)
for result in res:
    print(res)
    
#re.sub
re.sub()
import re
text_to_search="abc defghijkl abc tuvwxyz"
pattern=re.compile(r'abc')
res=re.sub(pattern,'123',text_to_search) #abc will replace 123
print("sub:",res)

#re.findall()
import re
line1="I am from India and i am proud that i am in India"
res=re.findall(r'India',line1) #2times it will find 
print(res)

#fullmatch()
import re
line1="i play volleyball "
res=re.fullmatch(r'i will play volleyball',line1) #the string will not match 
print(res)

#group()
import re
string ="30851 345,6728 2456"
#three digit numer followed by spece followed by two digit number.
pattern='(\d{3})(\d{2})' 
#match variable contains a match object.
match=re.search(pattern,string)
if match:
    print(match.group())
else:
    print("pattern not found")
    
# Split()
import re
text_to_search="abcdefghijklabcmnopqabcrstuvwxyz"
pattern=re.compile(r'abc') #abc is splited
res=re.split(pattern,text_to_search)
print("split",res)
    
    



