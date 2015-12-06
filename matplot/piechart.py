import matplotlib.pyplot as plt 
import inspect


scoringArea=[10,20,30,10,3]
print dir(inspect)

print (inspect.getargspec(plt.pie))
labels=['mid','straightdrive','long','left','right']
plt.pie(scoringArea,labels=labels,shadow=True,counterclock=True,pctdistance=8.0)
plt.xlabel('score')
#plt.ylabel('score')
plt.legend()
plt.show()
