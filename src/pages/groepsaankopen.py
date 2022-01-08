"""Home page shown when the user enters the application"""
import streamlit as st
import pandas as pd
import awesome_streamlit as ast
import base64

@st.experimental_memo
def load_data():
    data = pd.read_excel("data/BAP-matrix-versie2.xlsx", sheet_name=None)
    lookup_detail = {eis: detail for eis, detail in zip(data['Eis-Detail']["Eis"], data['Eis-Detail']["Detail"])}
    col_eis = [e for e in data['Element-Ingreep-Eis'].columns if "Eis" in e]
    for c in col_eis:
        data["Element-Ingreep-Eis"]["Detail-" + c] = [lookup_detail[e] if e in lookup_detail.keys() else ""for e in data['Element-Ingreep-Eis'].fillna("")[c]]
    return data

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

    .main .block-container {
        background: rgba(255,255,255,0.7);
        # background: rgba(240, 242, 246,0.5);
    }

    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""

    data = load_data()
    with st.spinner("Loading Home ..."):
        set_png_as_page_bg('images/geschiedenis/fortje.png')
        st.markdown("<h1>Groepsaankopen</h1>", unsafe_allow_html=True)
        data_gak = data['Ingreep-Groepsaankoop-Link'].drop(columns=["Ingreep"]).drop_duplicates()
        # data_gak = data['ingreep-groepsaankoop-link']["Ingreep"].fillna("")

        for g, l in zip(data_gak["Groepsaankoop"], data_gak["Link"]):
            st.markdown(f"* [{g}]({l})")

