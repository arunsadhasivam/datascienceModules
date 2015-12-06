import numpy as np 
from scipy.optimize  import curve_fit 
import matplotlib.pyplot as plt 
import math


def func(x,a,b):
     
     return a*x+b


x=np.linspace(0,10,100)
y=func(x,1,5)
yn=y+0.90*np.random.normal(size=len(x))
dir,dir1=curve_fit(func,x,yn)
print dir
print dir1

plt.plot(dir,dir1)
plt.xlabel('x-Axis')
plt.ylabel('y-Axis')
plt.legend()
plt.show()



