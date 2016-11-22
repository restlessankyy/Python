import re
line = "Hello Cats are smarter than dogs"

matchObj = re.match(r'(.*)are(.*)',line,re.I)
if matchObj:
    print "matchObj.group():",matchObj.group()
    print "matchObj.group(1):",matchObj.group(1)
    print "matchObj.group(2):",matchObj.group(2)
    print "matchObj.group(2):",matchObj.group(2)
else:
    
     print "No Match !!"
