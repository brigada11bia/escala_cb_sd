import streamlit as st

# Título da página, divido em duas colunas, uma para a imagem
coluna_titulo, coluna_img = st.columns(2)
with coluna_titulo:
    st.title("Cb Dia")
    
with coluna_img:
    st.image('logo11bia.png', width=80)
    
    
#upload do arquivo
st.image('previsao_cb_dia.png', width=650)
