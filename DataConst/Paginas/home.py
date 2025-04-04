import streamlit as st
from PIL import Image
from funcao import imagem_fundo



st.title('DataConstJr')
"\n"
"\n"
"\n"
st.markdown("""
    <div style=' width: 600px; text-align: justify; font-size: 18px'>
    Lorem ipsum dolor sit amet. Non ullam omnis ut esse dolorem ea fugiat iusto et nobis obcaecati. Sed vero corrupti non rerum vero qui molestiae illo id voluptatem natus sit sunt rerum.
    Est sequi sequi est eaque laborum et tenetur laudantium aut exercitationem asperiores. Rem distinctio alias vel galisum facilis et impedit esse At quibusdam eaque et provident voluptatem 
    Utut sint consequatur. Sit nulla facere nam quidem accusamus non eveniet doloribus vel incidunt eaque! Hic quidem Quis vel maiores nihil et nesciunt iste ex maxime laudantium!
    Ut quaerat eligendi et repellat dolore et blanditiis consequatur et adipisci galisum et quia asperiores nam tempore ipsa. Quo adipisci harum id molestiae tempore ut velit corporis. Non 
    adipisci suscipit hic perspiciatis similique aut quas nihil aut officia ducimus est excepturi illo sed rerum provident et natus labore.
       </div>
    
    """,
    unsafe_allow_html=True
    )
















############################# parte de ajustes da hud do site/pagina ##########################################

# Caminho da imagem PNG
imagem_cam = "identidade_visual/2 - elementos da Marca/PNG/Prancheta 1.png"

# Converte a imagem para base64
imagem_conver = imagem_fundo(imagem_cam)

# CSS personalizado para adicionar a imagem de fundo
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{imagem_conver}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Barlow';
        src: url('identidade_visual/3 - Fonts/Barlow-Regular.ttf') format('tff');
        font-weight: normal;
        font-style: normal;
    }

    body {
        font-family: 'Barlow', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Barlow', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)
