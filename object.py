class HideCounter:
    __secretValue=0
    def count(self):
                 self.__secretValue+=1
                 print self.__secretValue
                 
ob= HideCounter()
ob.count()
ob.count()

print ob.__secretValue

