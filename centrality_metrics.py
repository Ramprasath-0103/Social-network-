from read_dataset import df,G
import pandas as pd,networkx as nx,matplotlib.pyplot as plt

deg = nx.degree_centrality(G)
btw =nx.betweenness_centrality(G, weight='weight')
clo = nx.closeness_centrality(G , distance='weight')

def top5(d): return sorted(d.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top degree:", top5(deg))
print("Top betweenness:", top5(btw))
print("Top closeness:", top5(clo))