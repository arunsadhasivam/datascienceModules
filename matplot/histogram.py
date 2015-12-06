import random
import matplotlib.pyplot as plt

print random.randrange(1,33)

#histogram
over =[i for i in range(1,50) ]
over =[1,8,27,33,39]
over =[5,10,15,20,25]

print over
val = random.randrange(1,33)
score= [i for i in range(1,33)]

#MUST THAT VALUES ONLY IN INCREASING ORDER
#score=[10,30,50,60,70]
score=[10,15,20,25,30,50,55,70]
print score
plt.hist(score,over, histtype='bar',rwidth=0.6 ,color='c',label='Team A' )



#plt.bar(x1,y1,label='TeamB',color='orange')

plt.xlabel('overs')
plt.ylabel('Score per over')
plt.legend()
plt.title('Match statistics')
plt.show()





#population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
#bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
#plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
