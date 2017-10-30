import pylab
import numpy as np
import matplotlib.pyplot as plt
def make_data():
  s=np.random.uniform(.3,.85,50)
  x=np.average(s)
  y=sum(s>.5)/50
  print "%.5f,%.5f" %(x,y)
  return (x,y)

data=[make_data() for i in range(0,10000000)]
zip(*data)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(*zip(*data))
ax.xaxis.set_ticks(np.arange(0,1,.1))
ax.yaxis.set_ticks(np.arange(0,50,10))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Fairness')
plt.savefig('Fairness.png')
fig.show()



