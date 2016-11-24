import os
hostname ="127.0.0.1"
response = os.system("ping -n 1 "+hostname)

if response ==0:
    print   (hostname, "is up!")
else:
    print(hostname,"is down")
