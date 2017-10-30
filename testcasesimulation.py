import pylab
import matplotlib.pyplot as plt
def make_data():
  s=np.random.uniform(.3,.85,50)
  x=np.average(s)
  y=np.array(filter(lambda x:x>=0.5,s)).size
  print "%.5f,%.5f" %(x,y)
  return (x,y)

data=[make_data() for i in xrange(100)]
zip(*data)

plt.scatter(*zip(*data))
plt.show()


