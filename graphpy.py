import matplotlib .pyplot as pit
x = [101,102,103]
y= [5500,6000,4000]

x1 = [101,102,103]
y1=[5500,4800,1800]

pit.plot(x,y,label="Salary for 2015",color= 'red')
pit.plot(x1,y1,label="Salary for 2016")

pit.xlabel("Employee ID")
pit.ylabel("Salary in $s")

pit.title("Employee Salary")

pit.legend()
pit.show()         
                  


