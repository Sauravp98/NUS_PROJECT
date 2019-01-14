import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.externals import joblib
from sklearn import metrics, datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.linear_model import LogisticRegression
#import Tkinter as Tk

import tkinter as tk 
from tkinter import *
r = tk.Tk() 
r.configure(background="orange")
r.title('MOVIE CLASSIFIER') 
Label(r, text='BUDGET',bg='cyan').grid(row=0) 
Label(r, text='SCORE',bg='cyan').grid(row=1)
Label(r, text='RUNTIME',bg='cyan').grid(row=2) 
Label(r, text='GENRE',bg='cyan').grid(row=3)
Label(r, text='COUNTRY',bg='cyan').grid(row=4) 
Label(r, text='RATING',bg='cyan').grid(row=5) 
Label(r, text='VOTES',bg='cyan').grid(row=6) 
Label(r, text='YEAR',bg='cyan').grid(row=7) 
Label(r, text='MONTH',bg='cyan').grid(row=8) 
#Label(r, text='GROSS',bg='cyan').grid(row=8)  
e1 = Entry(r,bg='cyan') 
e2 = Entry(r,bg='cyan') 
e3 = Entry(r,bg='cyan') 
e4 = tk.Spinbox(r,values=("Adventure","Comedy","Action","Drama","Crime","Thriller","Horror","Animation","Biography","Sci-Fi","Musical","Family","Fantasy","Mystery","War","Romance","Western"),bg='cyan')
e5 = tk.Spinbox(r,values=("Argentina","Australia","Belgium","Canada","Chile","Czech Republic","Ireland","Panama","China","Denmark","France","Germany","Hong Kong","Hungary","Iran","Isreal","Italy","Japan","Netherlands","New Zealand","Peru","South Africa","Spain","Sweden","Switzerland","UK","USA","West Germany"),bg='cyan')
e6 = tk.Spinbox(r,values=("R","PG-13","PG","UNRATED","G","NC-17","TV-PG","TV-MA","B","B15","TV-14"),bg='cyan')
e7 = Entry(r,bg='cyan') 
e8 = Entry(r,bg='cyan') 
e9=Entry(r,bg='cyan') 

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
e3.grid(row=2, column=1) 
e4.grid(row=3, column=1) 
e5.grid(row=4, column=1) 
e6.grid(row=5, column=1) 
e7.grid(row=6, column=1) 
e8.grid(row=7, column=1) 
e9.grid(row=8, column=1)

button = tk.Button(r, text='Predict', width=25,bg='yellow',command=lambda:retrieve_input())
button.grid(row=19,column=1)
#button.pack() 
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text= msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
def retrieve_input():
	in1=int(e1.get())
	in2=int(e2.get())
	in3=int(e3.get())
	in4=e4.get()
	in5=e5.get()
	in6=e6.get()
	in7=int(e7.get())
	in8=int(e8.get())
	in9=int(e9.get())

	l1=("Adventure","Comedy","Action","Drama","Crime","Thriller","Horror","Animation","Biography","Sci-Fi","Musical","Family","Fantasy","Mystery","War","Romance","Western")
	l2=("Argentina","Australia","Belgium","Canada","Chile","Czech Republic","Ireland","Panama","China","Denmark","France","Germany","Hong Kong","Hungary","Iran","Isreal","Italy","Japan","Netherlands","New Zealand","Peru","South Africa","Spain","Sweden","Switzerland","UK","USA","West Germany")
	l3=("R","PG-13","PG","UNRATED","G","NC-17","TV-PG","TV-MA","B","B15","TV-14")


	for i in range(len(l1)):
		if(in4==l1[i]):
			in4=i         
	for i in range(len(l2)):
		if(in5==l2[i]):
			in5=i
	for i in range(len(l3)):
	    if(in6==l3[i]):
	    	in6=i
	    elif((in6=="Non Rated")|(in6=="Not specified")):
	    	in6=3
	clf = joblib.load('extwt.joblib')
	print(in1)
	print(in2)
	print(in3)
	print(in4)
	print(in5)
	print(in6)
	print(in7)
	print(in8)
	print(in9)
	#input = np.array([[76], [74], [71], [73], [72], [70], [100], [97], [93], [30], [10], [5], [1], [7], [2], [12]])
	#BUDGET COUNTRY GENRE RATING RUNTIME SCORE VOTES YEAR MONTH 
	input1 = np.array([in1, in5, in4, in3, in2, in6, in7, in8, in9])
	input1 = input1.reshape(1, -1)
	if(clf.predict(input1)==2):
	         popupmsg("This  movie is more likely to  be successful at the box office!!")
	else:
		     popupmsg("This  movie is less likely to perform well at the box office!!")
r.mainloop()
#prediction
print(clf.predict(input1))
