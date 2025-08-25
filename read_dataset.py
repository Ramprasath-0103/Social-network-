import pandas as pd, networkx as nx, matplotlib.pyplot as plt

df = pd.read_csv("indian_names_network_dataset.csv")
G=nx.DiGraph()
for _,r in df.iterrows():
    G.add_edge(r['source'],r['target'],weight=r['weight'])

print("Nodes:" ,G.number_of_nodes(),"Edges: ",G.number_of_edges())
pos = nx.spring_layout(G,seed=45)
nx.draw(G,pos,with_labels=True,node_size=500)
plt.show()