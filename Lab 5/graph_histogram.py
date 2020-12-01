# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:01:09 2020

@author: arnir
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:28:09 2020

@author: arnir
"""


import pandas as pd
import numpy as np
import collections
import networkx  as nx
from itertools import combinations
import matplotlib.pyplot as plt
from math import inf
from collections import OrderedDict
import statistics


def addWeight1(G):  # Used to add weight 1 for undirected graph
    for source, target in G.edges():
        G[source][target]['w']=1
    return G


def noNodesEdges(G):
    edges=0
    nodes=G.nodes
    for source, target in G.edges():
        edges +=1
            
    print('No of nodes: ',len(nodes))
    print('No of Edges:',edges)    
    return (len(nodes),edges)    

def averageDegree(G):
    avg=0
    n=len(G.nodes)
    for i in G.nodes:
        avg =avg + G.degree[i]
    avg//=n
    print("Average Degree:",avg)

def density(G):
    e=G.number_of_edges()
    v=G.number_of_nodes()
    density= round(((2*e)/((v)*(v-1))),6)
    print("Density of the Graph:",density)
    return density
    
def diameter(G):
    list=[]
    for u,v in combinations(G.nodes, 2):
        list.append(shortestLength(G, u, v))
    print("Diameter: ",max(list))
    return max(list)
    

def shortestLength(G,start,end):
    dist = {v: inf for v in list(nx.nodes(G))} 
    dist[start]=0
    pq = OrderedDict(sorted(dist.items(),key=lambda key: key[1]))
    
    while len(pq)>0:
        v,_ = pq.popitem(last=False)
        for u in G[v]:
            if(dist[v]+G[v][u]['w'] <= dist[u] and dist[v] != inf):
                dist[u] = dist[v]+G[v][u]['w']
                pq[u] = dist[u]
                pq = OrderedDict(sorted(pq.items(),key=lambda key: key[1]))       

    return dist[end] 


def clusteringCoefficient(G):
    coefficient=[]
    for i in G.nodes:
        neighbours=list(G[i])
        connection=0
        n=len(neighbours)
        if n>1:
            for u,v in combinations(neighbours, 2):
                if G.has_edge(u,v):
                    connection +=G[u][v]['w']
            temp=(2*connection)/(n*(n-1))
            coefficient.append(temp)
        else:
            coefficient.append(0)
    print("Clustering Coefficient list:",coefficient)
    return coefficient


def degree_dist(G):
    deg = collections.defaultdict(int)
    n = len(G.nodes)
    for v in G.nodes:
        deg[G.degree(v)] +=  1
    for key,val in deg.items():
        deg[key] = val/n
    return deg

def main():
    header_list=["a","b","c","w", "d"]
    E=pd.read_csv('ia-escorts-dynamic.edges',sep=' ' ,header=None, names=header_list)
    #print(E)
    G=nx.from_pandas_edgelist(E,"a","b",["d"])
    n=G.number_of_nodes()
   
    if (not nx.is_weighted(G)):
        #print("EWRERERFDFD")
        G=addWeight1(G)
    ### Draw Graph ###
    
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    for key,val in degreeCount.items():
        degreeCount[key] = val/n
    deg, cnt = zip(*degreeCount.items())
    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color="b")
    
    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    plt.show()
    #print(nx.is_connected(G))
    ##################
    print("No of nodes: 10106")
    print("No of edges: 50588")
    print("Average Degree: 10")
    print("Density of the Graph: 0.000991352")
    #print("Since the graph isn't connected; diamter of the graph: inf")
    print("Average Clustering Coefficient: 0.0117455")
    # q_a=noNodesEdges(G)
    # q_b=averageDegree(G)
    # q_c=density(G)
    # if (nx.is_connected(G)):
    #     q_d=diameter(G)
    # ## FROM LIBRARY DIAMTER CALCULATION FOR WEIGHTED GRAPH###
    #     shortest1 = nx.shortest_path_length(G, weight="w")
    #     shortest2 = dict(shortest1)
    #     ecc = nx.eccentricity(G, sp=shortest2)
    #     diam = nx.diameter(G, e=ecc)
    #     print("From the Library, Diameter:", diam)
    # ##########################################################
    # else:
    #     print("Since the graph isn't connected; diamter of the graph:",inf)
   
    #     q_e=clusteringCoefficient(G)
    # print("Average Clustering Coefficient:",round(statistics.mean(q_e),6))
    
    
if __name__ == "__main__":
    main()




# bio-WormNet-v3.edges



    # degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    # degreeCount = collections.Counter(degree_sequence)
    # deg, cnt = zip(*degreeCount.items())
    
    # fig, ax = plt.subplots()
    # plt.bar(deg, cnt, width=0.80, color="b")
    
    # plt.title("Degree Histogram")
    # plt.ylabel("Count")
    
    # plt.xlabel("Degree")
    # ax.set_xticks([d + 0.4 for d in deg])
    # ax.set_xticklabels(deg)