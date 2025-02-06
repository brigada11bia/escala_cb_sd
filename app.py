import streamlit as st

st.set_page_config(
        page_title="Escalas de Serviço",
        page_icon="logo.ico"
    )


pagina = st.navigation(
    [st.Page("cb_dia.py", title="Escala Cb Dia"),
    st.Page("cb_gda.py", title="Escala Cb Gda"),
    st.Page("motorista.py", title="Escala Motorista Dia"),
    st.Page("vila.py", title="Escala Vila")],
    position='sidebar')
pagina.run()

