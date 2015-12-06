import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y=[4,5,6,12,15]


x1=[1,2,3,4,5]
y1=[7,3,6,1,30]

plt.bar(x,y, label='TeamA',color='cyan')
plt.bar(x1,y1,label='TeamB',color='orange')

plt.xlabel('overs')
plt.ylabel('Score per over')
plt.legend()
plt.title('Match statistics')
plt.show()



