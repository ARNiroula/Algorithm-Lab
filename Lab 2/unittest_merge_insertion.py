# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 08:59:50 2020

@author: arnir
"""


import unittest
import merge_insertion

class MergeSortTest(unittest.TestCase):
    def testInt(self):
        data = [[7,15,14,16,17,26,21,27,30,2],
                [9,13,18,24,30,5,11,16,19,27],
                [3,5,16,18,26,2,4,11,17,25]]
        output = [[2, 7, 14, 15, 16, 17, 21, 26, 27, 30],
                  [5, 9, 11, 13, 16, 18, 19, 24, 27, 30],
                  [2, 3, 4, 5, 11, 16, 17, 18, 25, 26]]
        merge_insertion.mergesort(data[0],0,len(data[0]))
        merge_insertion.mergesort(data[1],0,len(data[1]))
        merge_insertion.mergesort(data[2],0,len(data[2]))
        self.assertEqual(data,output)
        
        # self.assertEqual(data[1],output[1])
        
        # self.assertEqual(data[2],output[2])
        
   
class InstertionSortTest(unittest.TestCase):
    def testInt(self):

        
        data = [[7,15,14,16,17,26,21,27,30,2],
                [9,13,18,24,30,5,11,16,19,27],
                [3,5,16,18,26,2,4,11,17,25]]

        output = [[2, 7, 14, 15, 16, 17, 21, 26, 27, 30],
                  [5, 9, 11, 13, 16, 18, 19, 24, 27, 30],
                  [2, 3, 4, 5, 11, 16, 17, 18, 25, 26]]
        merge_insertion.insertionSort(data[0])
        merge_insertion.insertionSort(data[1])
        merge_insertion.insertionSort(data[2])
        self.assertEqual(data,output)
if __name__ == "__main__":
    unittest.main()
