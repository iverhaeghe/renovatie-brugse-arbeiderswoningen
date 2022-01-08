"""Home page shown when the user enters the application"""
import streamlit as st
import base64
import awesome_streamlit as ast

from . import stappenplan


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        st.markdown("<h1>Renovatie en restauratie van 19e-eeuwse arbeiderswoningen in de Brugse binnenstad</h1>", unsafe_allow_html=True)
        
        st.markdown("""
        <p style='text-align: justify'>
        Welkom op de website voor het renoveren en restaureren van 19e-eeuwse arbeiderswoningen (cf. Geschiedenis) in de Brugse binnenstad.
        <br><br>
        In de Brugse binnenstad zijn heel wat 19e-eeuwse arbeiderswoningen terug te vinden. Sommigen zijn terug te vinden in de <a href='https://inventaris.onroerenderfgoed.be/' target='_blank'>inventaris van het vastgesteld bouwkundig erfgoed </a>, maar ze bezitten allemaal een belangrijke erfgoedwaarde voor het stadsbeeld. Hun gevels hebben typische gelijkaardige kenmerken die bij een renovatie behouden moeten blijven.
        <br><br>
        De 19e-eeuwse arbeiderswoningen zijn gezellige kleine rijwoningen, maar voldoen niet allemaal meer aan de huidige <a href='https://www.wonenvlaanderen.be/woningkwaliteit/welke-zijn-de-woningkwaliteitsnormen' target='_blank'> woningkwaliteitsnormen</a>. Op vlak van gezondheid (vocht, verluchting…), maar ook op vlak van comfort (verwarming, akoestiek…) en energieprestatie vormt de renovatie van deze woningen een uitdaging. <p>
        
        <p>
        Ga naar <strong><u>het stappenplan</u></strong> links in de navigatiebalk voor hulp en tips. (Op smartphone klik op pijl links boven.)
        </p>
        """,
        unsafe_allow_html=True)

        # if st.button("Start het stappenplan"):
        #     st.session_state.selection = "Stappenplan"

        # ast.shared.components.video_youtube(
        #     src="https://www.youtube.com/embed/E7pt2Zwg79g"
        # )