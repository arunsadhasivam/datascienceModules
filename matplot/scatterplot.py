import random
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[5,3,2,7,8,1,4,4]


x1=[3,15,6,7,8,9,10,11]
y1=[15,13,12,17,18,1,4,4]

plt.scatter(x,y,label='country1' ,s=100 ,marker='o')
plt.scatter(x1,y1,label='country2',s=100 ,marker='x')

#plt.bar(x1,y1,label='TeamB',color='orange')

plt.xlabel('minerals')
plt.ylabel('% distributions')
plt.legend()
plt.title('country wise  statistics')
plt.show()
