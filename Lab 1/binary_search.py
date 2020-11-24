import matplotlib.pyplot as plt
import numpy as np
import math
import time
import unittest
import more_itertools as mit

def binary_search(data, value):
    l, r = 0, len(data)-1

    while(l <= r):
        mid = (l+r)//2
        if(data[mid] == value):
            return mid
        elif value > data[mid]:
            l = mid+1
        elif value < data[mid]:
            r = mid-1
    return -1


bs_bc=[]
bs_ws=[]



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


################BEST CASE########################
for i in range(0,100):
    data=mit.random_combination(range(0, 100000*(10*(i+1))), r=10000*(10*(i+1)))
    mid=10000*(10*(i+1))//2
    start=time.time()
    print("Index of {}: {}".format(data[mid], binary_search_recursive(data, data[mid] )))
    end=time.time()
    bs_wc.append(end-start)
    print(bs_bc[i])

#######################################


################WORST CASE########################
for i in range(0,100):
    data=mit.random_combination(range(0, 100000*(10*(i+1))), r=10000*(10*(i+1)))
    start=time.time()
    print("Index of {}: {}".format(data[-1], binary_search_recursive(data, data[-1])))
    end=time.time()
    bs_wc.append(end-start)
    print(bs_wc[i])

#######################################

x=(np.arange(1,101))   
x=x.tolist()  
fig, (ax1,ax2) = plt.subplots(2)
fig.tight_layout(pad=3.0)
ax1.title.set_text('Worst Case')
ax1.set_xlabel('Data Size (10^5)')
ax1.set_ylabel('Time')
ax1.plot(x, bs_wc)

plt.ylim(-.01,.01)
ax2.plot(x, bs_bc)
ax2.title.set_text('Best Case')
ax2.set_xlabel('Data Size (10^5)')
ax2.set_ylabel('Time')

plt.show()

