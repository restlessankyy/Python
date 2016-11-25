import subprocess as s
ip = raw_input("Enter the IP Domain")
response = s.call(["ping",ip],shell=True
if(response==0):
     print "your IP is alive"
else:
     print "Check your IP"
                
                
