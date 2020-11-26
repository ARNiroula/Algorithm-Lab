# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:31:39 2020

@author: arnir
"""

import math
import random
import numpy as np
from collections import OrderedDict
#from queue import PriorityQueue
#import heapq
from math import inf
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt


G=nx.Graph()


#int(random.random()*20)

def randomGraph(n,p):
    nodes=np.arange(1,n+1)
    G.add_nodes_from(nodes)
    
    for u,v in combinations (G,2):
        if (random.random()<=p):
            G.add_edge(u,v,weight=random.randint(1, 30))
    pos = nx.circular_layout(G)
    nx.draw(G,pos,with_labels = True)
    grafo_labels = nx.get_edge_attributes(G,'weight')
    edges_label = nx.draw_networkx_edge_labels(G, pos, edge_labels = grafo_labels)
    print(nx.is_weighted(G))
    plt.figure(figsize=(12,8))
    plt.show()

    
def dijkstra(G: nx.Graph,start,end):

    dist = {v: inf for v in list(nx.nodes(G))} 
    dist[start]=0
    pq = OrderedDict(sorted(dist.items(),key=lambda key: key[1]))
    
    while len(pq)>0:
        
        v,_ = pq.popitem(last=False)
        for u in G[v]:
            if(dist[v]+G[v][u]['weight'] <= dist[u] and dist[v] != inf):
                dist[u] = dist[v]+G[v][u]['weight']
                pq[u] = dist[u]
                pq = OrderedDict(sorted(pq.items(),key=lambda key: key[1]))
                

    return dist[end] 
    

def cumilativeShortestLength(G):
    sum=0
    for u,v in combinations (G.nodes,2):
         dis = dijkstra(G,u,v)
         sum += dis
        #sum += nx.shortest_path_length(G,u,v,weight="weight")
    return sum


def main():
    # n=int(input("Enter the Number of nodes you want in the Graph:"))
    # p=float(input("Enter the probability of edge formation between 2 nodes. It should be between (0,.99)"))
    n=19
    p=.3
    randomGraph(n,p)
    if (nx.is_connected(G)!= True):
        print("The Graph isn't completely connected")
    else:        
        dij=cumilativeShortestLength(G)
        average_shortest_path=round(dij/(0.5*(n*(n+1))),4)
        print("Average Shortest Path Length:",average_shortest_path)
        #print(nx.average_shortest_path_length(G,weight="weight"))
        
        
        
    
    

if __name__ == "__main__":
    main()