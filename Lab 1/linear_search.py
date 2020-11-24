import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time
import unittest

def Sequential_Search(dlist, item):

    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos+1
    
    return  pos

w_t=[]
b_t=[]


# Unit Testing Implementation
class TestSearch(unittest.TestCase):
    
    def test_search(self):
        data = [2,3,4,5,6,7,8,12]
        self.assertEqual(binary_search(data,5),3)
        
    def test_searchChar(self):
        data = ['a','b','x','z']
        self.assertEqual(binary_search(data, 'x'),2)

if __name__ == "__main__":
    unittest.main()



####WORST CASE###########
for i in range (0,100):
    data=random.sample(range(10000*(10*(i+1))),1000*(10*(i+1)))
    #print(10**(i))
    #print (data[len(data)-1])
    start=time.time()
    print(Sequential_Search(data, data[len(data)-1]))
    end=time.time()    
    w_t.append(end-start)
    print (w_t[i])      

#################



##########BEST CASE################
for i in range (0,100):
    data=random.sample(range(10000*(10*(i+1))),1000*(10*(i+1)))
    #print(10**(i))
    #print (data[len(data)-1])
    start=time.time()
    print(Sequential_Search(data, data[0]))
    end=time.time()    
    b_t.append(end-start)
    print (b_t[i])      

###########################


x=(np.arange(1,101))   
x=x.tolist()  
fig, (ax1,ax2) = plt.subplots(2)
fig.tight_layout(pad=3.0)
ax1.title.set_text('Worst Case')
ax1.set_xlabel('Data Size (10^5)')
ax1.set_ylabel('Time')

ax1.plot(x, w_t)

plt.ylim(-.01,.01)
ax2.plot(x, b_t)
ax2.title.set_text('Best Case')
ax2.set_xlabel('Data Size (10^5)')
ax2.set_ylabel('Time')

plt.show()


