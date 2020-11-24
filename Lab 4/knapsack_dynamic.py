# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 09:07:23 2020

@author: arnir
"""




def knapsack_dynamic(item_values,item_weights,m):
    if len(item_weights) != len(item_values):
       return("Profit and weight do not have the same number of elements")
    n = len(item_weights)
    
    Table = [[0 for w in range(m + 1)] for i in range(n)]
    
    for i in range(1, n):
      for w in range(1, m + 1):
        wi = item_weights[i]
        vi = item_values[i]
        if wi <= w:
          Table[i][w] = max([Table[i - 1][w - wi] + vi, Table[i - 1][w]])
          
        else:
          Table[i][w] = Table[i - 1][w]
    # print(DataFrame(Table)) #Memoization Table
    
    return int(Table[n - 1][m])

p = [5, 6, 7, 2]
w = [4, 2, 3, 1]  
m = 8    
print(knapsack_dynamic(p, w, m))




