import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Criar um grafo vazio
G = nx.karate_club_graph()
@@ -44,29 +44,29 @@
nx.draw_networkx(G, with_labels=True, node_color='lightblue', node_size=400, font_size=10, alpha=0.8)
plt.axis('off')
plt.savefig('graph.png', dpi=300)
plt.show()

# Função para exibir o grafo no Streamlit
def show_graph():
    image = Image.open('graph.png')
    st.image(image, use_column_width=True)
# Configurar o streamlit para ignorar o aviso de depreciação
st.set_option('deprecation.showPyplotGlobalUse', False)

# Configuração do app Streamlit
# Exibir outras informações da rede
st.title('Análise Exploratória de Rede')
st.subheader('Grafo')
show_graph()
img = plt.imread('graph.png')
st.image(img, use_column_width=True)

# Exibir outras informações da rede
st.subheader('Informações da Rede')
st.write(f'Diâmetro: {diameter}')
st.write(f'Periferia: {periphery}')
st.write('Histograma de distribuição empírica de grau')
plt.hist(degrees, bins=max(degrees)-min(degrees)+1, rwidth=0.8)
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
st.write(f'Assortatividade geral da rede: {assortativity}')
