import streamlit as st

st.set_page_config(
    page_title = "DataConst Jr",
    page_icon = "imagem/logo_site.png",
    layout = "centered",
    initial_sidebar_state = "expanded",
    )



paginas = {
    "Geral":[
    st.Page("Paginas/home.py", 
        title = "Início", icon = "", default = True)],
    "Quem somos":[
        st.Page("Paginas/sobre_emp.py", 
        title = "Sobre a empresa", icon = ""),
        st.Page("Paginas/quem-somos.py", 
        title = "Organograma", icon = ""),
        
        st.Page("Paginas/servicos.py",
        title = "Serviços", icon ="")    
    ]
}

pg = st.navigation(paginas)
pg.run() 
