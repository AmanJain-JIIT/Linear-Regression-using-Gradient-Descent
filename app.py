from tkinter import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#defining main window
root = Tk()
root.title("Linear Regression")
root.geometry("900x900")

#defining frame 
frame = LabelFrame(root, padx = 20, pady = 20, bg = "black")
frame.pack(padx = 20, pady = 20)

#x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
#y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#training set
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

#gradient descent function
def gradient_descent(x,y):
	w_curr = b_curr = 0
	iterations = 10000
	learning_rate = 0.01
	m = len(x)
	for i in range(iterations):
		y_predicted = w_curr*x + b_curr

		wd = (2/m)*sum(x*(y_predicted - y))
		bd = (2/m)*sum(y_predicted - y)

		w_curr = w_curr - learning_rate*wd
		b_curr = b_curr - learning_rate*bd

	w = w_curr
	b = b_curr

	return w, b

#plotting training set
plt.scatter(x, y)

#using in_built function to calculate w and b
slope, intercept, r, p, std_err = stats.linregress(x, y)

result = gradient_descent(x, y)
w = result[0]
b = result[1]

#calculating predicted value
def calc(x):
	return w*x + b

# plotting straight line 
model = list(map(calc, x))
plt.plot(x, model)

# defining function to call predict
def predict():
	global choice
	global result

	result.grid_forget()

	c = choice.get()
	choice.delete(0, END)

	if len(c) == 0:
		result = Label(frame, text = "Please enter a value first", padx = 10, pady = 10, bg = "black", fg = "white", font = ("Times", 40, "bold"))
		result.grid(row = 4, column = 0, padx = 20, pady = (20, 0))
		return

	out = calc(int(c))

	result = Label(frame, text = str(c) + "   --->   " +str(out), padx = 10, pady = 10, bg = "black", fg = "white", font = ("Times", 40, "bold"))
	result.grid(row = 4, column = 0, padx = 20, pady = (20, 0))

	#plt.bar(int(c), int(out), color ='black', width = 0.1)
	#plt.show()

# defining function to check co-relation
def check():
	global result2
	global r

	result2 = Label(frame, text = r, padx = 10, pady = 10, bg = "black", fg = "white", font = ("Times", 40, "bold"))
	result2.grid(row = 6, column = 0, padx = 20, pady = (20, 0))

#formatting main window
heading = Label(frame, text = "LINEAR REGRESSION", padx = 10, pady = 10, bg = "black", fg = "white")
heading.configure(font = ("Times", 50, "bold"))
heading.grid(row = 0, column = 0, padx = 20, pady = 20)

Label(frame, text = "Enter the value", padx = 10, pady = 10, bg = "black", fg = "white", font = ("Times", 30, "bold")).grid(row = 1, column = 0, padx = 20, pady = (20, 0))

choice = Entry(frame, width = 50, borderwidth = 5)
choice.configure(font = ("Times", 15, "bold"))
choice.grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 40, ipady = 5)

button = Button(frame, text = "PREDICT", padx = 10, pady = 10, borderwidth = 10, relief = RAISED,bg="#454545", fg="white", command = predict)
button.configure(font = ("Times", 20, "bold"))
button.grid(row = 3, column = 0, padx = 10, pady = (50, 10), ipadx = 40, ipady = 5)

result = Label(frame, text = "", padx = 10, pady = 10, bg = "black", fg = "white", font = ("Times", 40, "bold"))
result.grid(row = 4, column = 0, padx = 20, pady = (20, 0))

button2 = Button(frame, text = "CHECK RELATIONSHIP", padx = 10, pady = 10, borderwidth = 10, relief = RAISED,bg="#454545", fg="white", command = check)
button2.configure(font = ("Times", 20, "bold"))
button2.grid(row = 5, column = 0, padx = 10, pady = (50, 10), ipadx = 40, ipady = 5)

result2 = Label(frame, text = "", padx = 10, pady = 10, bg = "black", fg = "white", font = ("Times", 40, "bold"))
result2.grid(row = 6, column = 0, padx = 20, pady = (20, 0))


root.mainloop()