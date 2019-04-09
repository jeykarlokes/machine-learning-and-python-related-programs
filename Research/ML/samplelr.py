import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data2 = pd.read_csv("Multi_linear.txt",header = None)
data2.head()
data2.describe()
fig, axes = plt.subplots(figsize=(12,4),nrows=1,ncols=2)

axes[0].scatter(data2[0],data2[2],color="g")
axes[0].set_xlabel("size (square Feet)")
axes[0].set_ylabel("Prices")
axes[0].set_title("Houses prices against size of house")
axes[1].scatter(data2[0],data2[2],color="b")
axes[1].set_xlabel("Number of bedrooms")
axes[1].set_ylabel("Prices")
axes[1].set_title("Houses prices against size of house")
plt.tight_layout()

def featureNormalization(X):
    mean = np.mean(X,axis=0)
    # print(mean)
    std = np.std(X,axis=0)
    X_norm = (X - mean)/std
    return X_norm,mean,std

def computeCost(X,y,theta):
    """Take in a numpy array X,y, theta and generate the cost function of using theta as parameter 
    	in a linear regression model"""
    # print("theta ",theta)
    m=len(y)
    predictions=X.dot(theta)
    # print("predictions",predictions)
    square_err=(predictions - y)**2
    
    final =  1/(2*m) * np.sum(square_err)
    # print("final",final)
    return final

data_n2=data2.values
m2=len(data_n2[:,-1])
X2=data_n2[:,0:2].reshape(m2,2)
X2, mean_X2, std_X2 = featureNormalization(X2)
X2 = np.append(np.ones((m2,1)),X2,axis=1)
y2=data_n2[:,-1].reshape(m2,1)
theta2=np.zeros((3,1))

def gradientDescent(X,y,theta,alpha,num_iters):
    """Take in numpy array X, y and theta and update theta by taking num_iters gradient steps
    with learning rate of alpha return theta and the list of the cost of theta during each iteration
    """
    m=len(y)
    J_history=[]
    for i in range(num_iters):
        predictions = X.dot(theta)
        error = np.dot(X.transpose(),(predictions -y))
        descent=alpha * 1/m * error
        theta-=descent
        J_history.append(computeCost(X,y,theta))
    return theta, J_history

computeCost(X2,y2,theta2)

theta2, J_history2 = gradientDescent(X2,y2,theta2,0.1,400)
print("h(x) ="+str(round(theta2[0,0],2))+" + "+str(round(theta2[1,0],2))+"x1 + "+str(round(theta2[2,0],2))+"x2")

plt.plot(J_history2)
plt.xlabel("Iteration")
plt.ylabel("$J(Theta)$")
plt.title("Cost function using Gradient Descent")

def predict(x,theta):
    """Takes in numpy array of x and theta and return the predicted value of y based on theta"""
    predictions= np.dot(theta.transpose(),x)
    return predictions[0]
#feature normalisation of x values
x_sample = featureNormalization(np.array([1650,3]))[0]
x_sample=np.append(np.ones(1),x_sample)
predict3=predict(x_sample,theta2)
print("For size of house = 1650, Number of bedroom = 3, we predict a house value of $"+str(round(predict3,0)))
