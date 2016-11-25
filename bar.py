#BarCharts
import matplotlib.pyplot as pit


x = [2,4,6,8]
y = [10,19,5,7]

x1=[1,3,5,7]
y1 = [7,5,14,12]

pit.bar(x,y,label="Salary for 2015",color="red")
pit.bar(x1,y1, label= "Salary for 2016")

pit.xlabel("Employee ID")
pit.ylabel("Salary in $s")

pit.title("Employee Salary")
pit.legend()
pit.show()
