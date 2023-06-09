import streamlit as st
import networkx as nx
from pyvis.network import Network

# Criar um grafo vazio
G = nx.karate_club_graph()

# Configurar o grafo para visualização com pyvis
nt = Network('500px', '500px')
nt.from_nx(G)

# Configuração do app Streamlit
st.title('Análise Exploratória de Rede')
st.subheader('Grafo')

# Exibir o grafo usando pyvis
viz_graph = nt.show('network.html')
viz_graph.add_module("clickevents")

# Exibir o grafo no Streamlit usando um iframe
st.components.v1.iframe(src='network.html', width=800, height=600)

# Outras informações da rede
st.subheader('Informações da Rede')
st.write(f'Diâmetro: {nx.diameter(G)}')
st.write(f'Periferia: {nx.periphery(G)}')
st.write('Histograma de distribuição empírica de grau')
degrees = [G.degree(node) for node in G.nodes()]
st.hist(degrees, bins=max(degrees)-min(degrees)+1, rwidth=0.8)
st.write(f'Coeficiente de clustering global: {nx.average_clustering(G)}')
st.write(f'Componentes Conectados: {list(nx.connected_components(G))}')
st.write(f'Eigenvector centrality: {nx.eigenvector_centrality(G)}')
st.write(f'Degree centrality: {nx.degree_centrality(G)}')
st.write(f'Closeness centrality: {nx.closeness_centrality(G)}')
st.write(f'Betweenness centrality: {nx.betweenness_centrality(G)}')
st.write(f'Assortatividade geral da rede: {nx.degree_assortativity_coefficient(G)}')
