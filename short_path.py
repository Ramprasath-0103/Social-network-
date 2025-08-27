from read_dataset import df,G
import pandas as pd, networkx as nx, matplotlib.pyplot as plt
if __name__ == "__main__":
    unique_names = sorted(df['source'].unique())
    length = len(unique_names)
    for i in range(length-1):
        for j in range(i+1,length):
            src = unique_names[i]
            trgt = unique_names[j]
            short_path = nx.dijkstra_path(G,src,trgt,weight='weight')
            dist = nx.dijkstra_path_length(G,src,trgt,weight='weight')
            print("Path: ",short_path,"Length: ",dist)
            plt.show()
            break #break statement can be removed to showcase all the possible paths btw unique source,target pair
