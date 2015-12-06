import random
import matplotlib.pyplot as plt
import inspect

x=[1,2,3,4,5,6,7,8]
y=[5,3,2,7,8,1,4,4]


x1=[3,15,6,7,8,9,10,11]
y1=[15,13,12,17,18,1,4,4]

print  inspect.getargspec(plt.stackplot)


#label for stack 
plt.plot([],[],label='mineral1',color='c',linewidth=10)
plt.plot([],[],label='mineral2',color='m',linewidth=10)
plt.plot([],[],label='mineral3',color='r',linewidth=10)
team1=[1,2,3,4,5]


team2=[1,3,4,5,6]
team3=[3,3,5,1,7]
team4=[8,5,3,1,4]
# wont support label or legend by default 
#need to use plot like above
plt.stackplot(team1,team2,team3,team4,colors=['c','m','r','k'])

#plt.bar(x1,y1,label='TeamB',color='orange')

plt.xlabel('minerals')
plt.ylabel('% distributions')
plt.legend()
plt.title('country wise  statistics')
plt.show()
