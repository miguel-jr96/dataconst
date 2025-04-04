import streamlit as st
import pandas as pd
import base64

# Função para carregar a imagem como base64
def imagem_fundo(imagem_cam):
    with open(imagem_cam, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()




