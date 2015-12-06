import matplotlib.pyplot as plt 
import matplotlib.style as style 

x=[1,2,3,4,6]
y=[5,2,1,4,8]

#[u'grayscale', u'bmh', u'dark_background',u'ggplot', u'fivethirtyeight']
style.use('dark_background')
print style.available
plt.plot(x,y,color='g' ,label='style')
print dir(style)
plt.xlabel('over')
plt.ylabel('Score per over')
plt.legend()

plt.show()