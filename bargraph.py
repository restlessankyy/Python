import matplotlib.pyplot as pit

scores = [10,20,25,24,24,5,0,14,8]
over=[x for x in range(len(scores))]

pit.bar(over,scores,label='Score per Over',color="red")
pit.xlabel("x")
pit.ylabel("y")

pit.title("Runs for Over")
pit.legend()
pit.show()

