import streamlit as st
import pandas as pd
import base64

# Função para carregar a imagem como base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()




