import re
phone = "2004-959-559 #This is a Phone Number"

#Delete Python-Stylecomments
num = re.sub(r'#.*$',"",phone,1)
print "Phone Num :",num

num = re.sub(r"-","/",num)
print num

num = re.sub(r'\D',"",phone)
print "Phone Num :",num
             
