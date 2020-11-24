# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 09:15:17 2020

@author: arnir
"""


  
# class ItemValue: 
#     def __init__(self, wt, val, ind): 
#         self.wt = wt 
#         self.val = val 
#         self.ind = ind 
#         self.cost = val // wt 
  
#     def __lt__(self, other): 
#         return self.cost < other.cost 
  
# # Greedy Approach 
  
  
# class FractionalKnapSack: 
  
#     def getMaxValue(wt, val, capacity): 
#         itemValue = [] 
#         for i in range(len(wt)): 
#             itemValue.append(ItemValue(wt[i], val[i], i)) 
  
#         # sorting items by value 
#         itemValue.sort(reverse=True) 
#         for i in itemValue:
#             print (i.wt,i.val)
#         totalValue = 0
#         for i in itemValue: 
#             curWt = int(i.wt) 
#             curVal = int(i.val) 
#             if capacity - curWt >= 0: 
#                 capacity -= curWt 
#                 totalValue += curVal 
#             else: 
#                 fraction = capacity / curWt 
#                 totalValue += curVal * fraction 
#                 capacity = int(capacity - (curWt * fraction)) 
#                 break
#         return totalValue 
  

def fractional_knapsack(p, w, m):
    if len(p) != len(w):
       return("Profit and weight do not have the same number of elements")
    item_no = list(range(len(p)))
    
    ratio = [val/wt for val, wt in zip(p, w)]
    item_no.sort(key=lambda i: ratio[i], reverse=True)
    
    max_profit = 0
    fractions = ['0']*len(p)
    
    for i in item_no:   
        if w[i] <= m:
            fractions[i] = str(1)
            max_profit += p[i]
            m -= w[i]
        else:
            fractions[i] = str(round(m/w[i],2)*100)+'%'
            max_profit += p[i]*m/w[i]
            break
 
    return int(max_profit), fractions
 
 

  
wt = [10, 40, 20, 30] 
val = [60, 40, 100, 120] 
capacity = 50
print(fractional_knapsack(val, wt, capacity))    
    
