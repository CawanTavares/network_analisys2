import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Criar um grafo vazio
G = nx.karate_club_graph()

# Matriz de adjacência
adj_matrix = nx.to_numpy_array(G)

# Diâmetro da rede
diameter = nx.diameter(G)

# Periferia da rede
periphery = nx.periphery(G)

# Histograma de distribuição empírica de grau
degrees = [G.degree(node) for node in G.nodes()]

# Coeficiente de clustering global
global_clustering = nx.average_clustering(G)

# Componentes Conectados
connected_components = list(nx.connected_components(G))

# Eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality(G)

# Degree centrality
degree_centrality = nx.degree_centrality(G)

# Closeness centrality
closeness_centrality = nx.closeness_centrality(G)

# Betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Assortatividade geral da rede
assortativity = nx.degree_assortativity_coefficient(G)

# Salvar o grafo como uma imagem
plt.figure(figsize=(8, 8))
nx.draw_networkx(G, with_labels=True, node_color='lightblue', node_size=400, font_size=10, alpha=0.8)
plt.axis('off')
plt.savefig('graph.png', dpi=300)
plt.show()

# Configurar o streamlit para ignorar o aviso de depreciação
st.set_option('deprecation.showPyplotGlobalUse', False)

# Exibir outras informações da rede
st.title('Análise Exploratória de Rede')
st.subheader('Grafo')
img = plt.imread('graph.png')
st.image(img, use_column_width=True)

st.subheader('Informações da Rede')
st.write(f'Diâmetro: {diameter}')
st.write(f'Periferia: {periphery}')
st.write('Histograma de distribuição empírica de grau')
plt.hist(degrees, bins=np.arange(min(degrees), max(degrees)+1), rwidth=0.8)
plt.xlabel('Grau')
plt.ylabel('Contagem')
st.pyplot()
st.write(f'Coeficiente de clustering global: {global_clustering}')
st.write(f'Componentes Conectados: {connected_components}')
st.write(f'Eigenvector centrality: {eigenvector_centrality}')
st.write(f'Degree centrality: {degree_centrality}')
st.write(f'Closeness centrality: {closeness_centrality}')
st.write(f'Betweenness centrality: {betweenness_centrality}')
st.write(f'Assortatividade geral da rede: {assortativity}')
