from scipy.optimize import fsolve
import numpy as np 
import inspect
line = lambda x:x+3

print inspect.getargspec(line)
solution = fsolve(line,-2)
print solution