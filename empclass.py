class employee:
   "This is employee class"
   empCount =0
   def  __init__(self,name,salary):
      self.name =name
      self.salary =salary
      employee.empCount +=1
   def displayCount(self):
        print "Total Employee  %d" %employee.empCount
   def displayEmployee(self):
         print "Name:",self.name,"Salary:",self.salary

#print("*#"*20)
empl
emp1=employee('restless',99900)
emp1.displayCount()
emp1.displayEmployee()

emp2=employee('ankyyy',999989)
emp2.displayCount()
emp2.displayEmployee()

print "Employee.__doc__:",employee.__doc__








