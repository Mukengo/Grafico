import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🎮 Ranking de Jogos 2024", layout="wide")

st.title("🎮 Ranking dos Jogos Mais Jogados em 2024")

# Lê o CSV
df = pd.read_csv("jogos.csv")

# Mostra os dados
st.write("### 📄 Tabela de Dados:")
st.dataframe(df)

# Ordena os dados por número de jogadores
df = df.sort_values(by="Jogadores (milhões)", ascending=True)

# Cria o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df["Jogo"], df["Jogadores (milhões)"], color='skyblue')
ax.set_title("Jogos mais jogados em 2024", fontsize=18)
ax.set_xlabel("Número de Jogadores (em milhões)")
ax.set_ylabel("Jogos")
for i, v in enumerate(df["Jogadores (milhões)"]):
    ax.text(v + 1, i, str(v), color='black', va='center')

# Mostra o gráfico
st.pyplot(fig)

# Extra: Top 1
top1 = df.sort_values(by="Jogadores (milhões)", ascending=False).iloc[0]
st.markdown(f"🏆 **Jogo mais jogado:** {top1['Jogo']} com {top1['Jogadores (milhões)']} milhões de jogadores.")
