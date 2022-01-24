"""Main module for the renovation app"""

import os, sys
import pandas as pd 

import streamlit as st
import base64

import awesome_streamlit as ast
import src.pages.home
import src.pages.stappenplan
import src.pages.geschiedenis
import src.pages.premies
import src.pages.groepsaankopen

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home,
    "19ᵉ-Eeuwse arbeiderswoningen": src.pages.geschiedenis,
    "STAPPENPLAN": src.pages.stappenplan,
    "Premies": src.pages.premies,
    "Groepsaankopen": src.pages.groepsaankopen,
}

def render_page():
    if "selection" not in st.session_state:
        st.session_state.selection = "Home"
    st.session_state.page = PAGES[st.session_state.selection]

import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: linear-gradient(rgba(255,255,255,0.7), rgba(255,255,255,0.7)), url("data:image/png;base64,%s");
        background-size: cover;
    }

    # .main .block-container {
    #     # background: rgba(255,255,255,0.5);
    #     background: rgba(240, 242, 246,0.5);
    # }

    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def main():
    """Main function of the App"""
    set_png_as_page_bg('images/geschiedenis/fortje.png')
    st.sidebar.markdown("<p style='font-size: 16px'>Bachelorproef in samenwerking met</p>", unsafe_allow_html=True)
    st.sidebar.image("images/Logo's Howest en Brugge - ZONDER ACHTERGROND.png", width=150)
    st.sidebar.markdown("<p style='font-size: 14px;'><strong><em>(Dit is geen officiële website)</em></strong></p>", unsafe_allow_html=True)
    st.sidebar.title("Navigatie")
    st.session_state.selection = st.sidebar.radio("Ga Naar", list(PAGES.keys()), on_change = render_page())
    st.session_state.page = PAGES[st.session_state.selection]
    with st.spinner(f"Loading {st.session_state.selection} ..."):
        ast.shared.components.write_page(st.session_state.page)
    st.sidebar.title("About")
    st.sidebar.info(
    """
    Deze website is geschreven door Ine Verhaeghe voor de [Bacheloropleiding Toegepaste Architectuur (Howest Brugge)](https://www.howest.be/nl/opleidingen/bachelor/toegepaste-architectuur).
    """)
    

if __name__ == "__main__":
    main()
