import matplotlib.pyplot as plt 
x=[1,2,3]
y=[4,5,6]


x1=[1,2,3]
y1=[7,3,6]

plt.plot(x,y, label='TeamA')
plt.plot(x1,y1,label='TeamB')
plt.xlabel('overs')
plt.ylabel('Score per over')
plt.legend()
plt.title('Match statistics')
plt.show()