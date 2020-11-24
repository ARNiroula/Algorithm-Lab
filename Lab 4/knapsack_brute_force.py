# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:16:56 2020

@author: arnir
"""


def getStrings(n):
   return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

# Solve 0/1 Knapsack problem with Brute force 
def bruteforce(p, w, m):
   if len(p) != len(w):
       return("Profit and weight do not have the same number of elements")
   n = len(p)
   item_configuration = getStrings(n)
   
   max_profit = 0
   solution = ''

   result = []

   for s in item_configuration:
      
      profit = sum([int(s[i]) * p[i] for i in range(n)])
      weight = sum([int(s[i]) * w[i] for i in range(n)])

      if weight <= m and profit > max_profit:
         max_profit = profit
         solution = s
         
   result.append(solution)
   result.append(max_profit)

   return result




    
