import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model
# import tkinter as tk 
import statsmodels.api as sm

def estimate_coef(x, y): 
	# number of observations/points 
	n = np.size(x) 
	print(n)
	# mean of x and y vector 
	m_x, m_y = np.mean(x), np.mean(y) 
	print(m_x,m_y)
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 
	print("calculating cross-deviation and deviation about x ",SS_xy,SS_xx)
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x 
	
	print("# calculating regression coefficients ",b_1,b_0)
	return(b_0, b_1) 

def plot_regression_line(x, y, b): 
	# plotting the actual points as scatter plot 
	plt.scatter(x, y, color = "m", 
			marker = "o", s = 30) 

	# predicted response vector 
	y_pred = b[0] + b[1]*x 

	# plotting the regression line 
	plt.plot(x, y_pred, color = "g") 

	# putting labels 
	plt.xlabel('x') 
	plt.ylabel('y') 

	# function to show plot 
	plt.show() 

def main(): 
	# observations 
	x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
	y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 

	# estimating coefficients 
	b = estimate_coef(x, y)
	print("b value is ",b) 
	print("Estimated coefficients:\nb_0 = {} \\nb_1 = {}".format(b[0], b[1])) 

	# plotting regression line 
	plot_regression_line(x, y, b) 
	print(reg)
if __name__ == "__main__": 
	main() 
