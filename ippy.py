import subprocess as s
ip=raw_input("Enter the IP Domain")
if(s.call(["ping",ip])==0):
     print "your IP is alive"
else:
     print "Check your IP"
                
                
