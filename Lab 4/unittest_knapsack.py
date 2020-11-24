# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:13:20 2020

@author: arnir
"""


import unittest
from knapsack_brute_force import bruteforce
from brute_frac import bruteforce_fractional
from knapsack_greedy import fractional_knapsack
from knapsack_dynamic import knapsack_dynamic
 
class Knapsack(unittest.TestCase):

   def test_bruteforce(self):
      p = [5, 6, 7, 2]
      w = [4, 2, 3, 1]  
      m = 8
      ### For 0/1
      ans_brute=(bruteforce(p,w,m))
      ans_dynamic=(knapsack_dynamic(p,w,m))
      
      output_1 = ['0111', 15]
      output_2= 15
      self.assertListEqual(ans_brute, output_1)
      self.assertEqual(ans_dynamic, output_2)
      
      ##### For Fractional 
      wt = [10, 40, 20, 30] 
      val = [60, 40, 100, 120] 
      capacity = 50
      ans_brute_frac=bruteforce_fractional(val, wt, capacity)
      ans_greedy=fractional_knapsack(val, wt, capacity)
      
      output_3=(240, ['1', '0', '1', '67.0%'])
      self.assertEqual(ans_brute_frac, output_3)
      self.assertEqual(ans_greedy, output_3)
      
      
if __name__ == '__main__':
   unittest.main()
   
