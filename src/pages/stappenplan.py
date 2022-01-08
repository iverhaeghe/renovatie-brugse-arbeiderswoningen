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
    data["Prioriteit-Groep-Element"] = pd.merge(data["Prioriteit-Groep-Element"], data["Prioriteit-Impact"], on="Prioriteit", how="inner")
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

    div[data-baseweb="select"] > div {
        border-style: solid;
        border-color: lightgrey;
    }

    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        set_png_as_page_bg('images/geschiedenis/fortje.png')
        st.markdown("# Stappenplan")
        data = load_data()
        st.markdown("""
        <h1> 1. Beginfase</h1>
        <p style='text-align: justify'>
        Voordat je begint met je renovatiekeuzes, is het belangrijk eerst stil te staan bij de <b>omvang</b> (grootte van de woning, mogelijkheden en beperkingen, budget) van je project, de huidige <b>kwaliteit</b> (bouwkundig, structureel, erfgoedkwaliteiten, comfort) van de woning en de <b>wensen</b> (eigen wensen, stedenbouwkundige eisen, normen en wettelijke verplichtingen) van het te bekomen resultaat. Deze zaken bepalen mee de keuzes die je zult maken op vlak van materialen en uitvoeringsmethoden.
        </p>
        <h1> 2. Uitwerkingsfase</h1>
        <p style='text-align: justify'>
        De uitwerkingsfase bestaat uit het schetsen van mogelijke oplossingen en het toetsen van deze oplossingen aan de wensen en doelen uit de beginfase. Het is hierbij belangrijk dat je wensen uit de beginfase kunnen vertaald worden naar een uitvoeringsplan op basis van de uitvoeringskeuzes die je maakt. In deze fase kun je best ook beroep doen op professioneel renovatieadvies. Dit advies biedt stad Brugge u gratis aan. Klik <a href='https://energieplatform.brugge.be/renovatiescan' target='_blank'>hier</a> voor meer informatie.
        </p>
        """, unsafe_allow_html=True)

        st.session_state.groep = st.selectbox(
            "1. Welke gebouwschil of technische installatie wil je renoveren?",
            tuple(data["Prioriteit-Groep-Element"]["Groep"].drop_duplicates())
        ) 
        
        st.write("Je hebt gekozen voor de groep:", st.session_state.groep)
        
        impact = data["Prioriteit-Groep-Element"].loc[data["Prioriteit-Groep-Element"]["Groep"] == st.session_state.groep, "Impact"].values[0]
        st.markdown(f"<p><em>{impact}</em></p>", unsafe_allow_html=True)

        st.session_state.element = st.selectbox(
            "2. Welk onderdeel kies je?",
            tuple(data["Prioriteit-Groep-Element"].loc[data["Prioriteit-Groep-Element"]["Groep"] == st.session_state.groep, "Element"])
        ) 
        
        adp = st.expander(label="Wat zijn de aandachtspunten?")
        with adp:
            data_adp = pd.merge(data["Prioriteit-Groep-Element"], data["Element-Aandachtspunt"], on="Element", how="inner")
            data_adp = data_adp[data_adp["Element"] == st.session_state.element].fillna("GEEN")
            for a in data_adp["Aandachtspunt"]:
                st.write(f""" * {a}""")

        # st.markdown("""
        # # 4. Uitwerkingsfase
        # """)

        data_ingreep = pd.merge(data_adp, data["Element-Ingreep"], on="Element", how="inner")
        data_afbeelding = data["Ingreep-Afbeelding"].fillna("")

        cols1, cols2 =st.columns(2)

        with cols1:
            st.session_state.ingreep = st.selectbox(
                "3. Welke techniek kies je?",
                tuple(data_ingreep["Ingreep"].drop_duplicates())
            ) 
            st.write("Je hebt gekozen voor de techniek:", st.session_state.ingreep)
        
        with cols2:
            afb = list(data_afbeelding.loc[data_afbeelding["Ingreep"] == st.session_state.ingreep, "Afbeelding"])
            # st.write(afb)
            if len(afb) > 0 and afb[0] != "":
                st.image(f"images/details/{afb[0]}.png", use_column_width=True)
            else:
                st.empty()
                # st.image("images/geschiedenis/fortje.png")

        eisen = st.expander(label="Wettelijke eisen")
        vw_ingreep = st.expander(label="Voorwaarden")
        plusmin = st.expander(label="Voor- en nadelen")
        premies = st.expander(label="Premies")
        groepsaankopen = st.expander(label="Groepsaankopen")

        data_eis = data['Element-Ingreep-Eis'][data['Element-Ingreep-Eis']["Ingreep"] == st.session_state.ingreep].fillna("")
        data_vw = data['Ingreep-Voorwaarde'][data['Ingreep-Voorwaarde']["Ingreep"] == st.session_state.ingreep].fillna("")
        data_vdl = data['Ingreep-Voordeel'][data['Ingreep-Voordeel']["Ingreep"] == st.session_state.ingreep].fillna("")
        data_ndl = data['Ingreep-Nadeel'][data['Ingreep-Nadeel']["Ingreep"] == st.session_state.ingreep].fillna("")
        data_prm = data['Ingreep-Premie'][data['Ingreep-Premie']["Ingreep"] == st.session_state.ingreep].fillna("")
        data_gak = data['Ingreep-Groepsaankoop-Link'][data['Ingreep-Groepsaankoop-Link']["Ingreep"] == st.session_state.ingreep].fillna("")


        col_eis = [c for c in data_eis if "Eis" in c and "Detail" not in c]
        dtl_eis = [c for c in data_eis if "Eis" in c and "Detail" in c]

        with eisen:            
            for c, d in zip(col_eis, dtl_eis):
                st.write(f"""
                ###### {c}
                """)
                for e, f in zip(data_eis[c], data_eis[d]):
                    if e != "" and f != "":
                        st.write(f"* {e} ({f})")
                    elif f != "":
                        st.write(f"({e})")

        with vw_ingreep:
            st.write("##### Voorwaarden om de techniek uit te voeren")
            for v in data_vw["Voorwaarde"]:
                if v != "":
                    st.write(f"* {v}")

        with plusmin:
            st.write("##### Voordelen")
            for v in data_vdl["Voordeel"]:
                if v != "":
                    st.write(f"* {v}")
            st.write("##### Nadelen")
            for v in data_ndl["Nadeel"]:
                if v != "":
                    st.write(f"* {v}")

        with premies:
            st.write("##### Premies")
            # st.write("Deze techniek komt in aanmerking voor de volgende premies:")

            st.session_state.premie = st.selectbox(
                "Deze techniek komt in aanmerking voor de volgende premies:",
                tuple(data_prm["Premie"].drop_duplicates())
            ) 

            data_prm_vw = data["Premie-Voorwaarde"].loc[data["Premie-Voorwaarde"]["Premie"] == st.session_state.premie]
            data_bdg = data["Premie-Bedrag"].loc[data["Premie-Bedrag"]["Premie"] == st.session_state.premie]
            data_link = data["Premie-Aanvraag-Link"].loc[data["Premie-Aanvraag-Link"]["Premie"] == st.session_state.premie]

            st.markdown("<p style='font-size: 17px'> <strong>Premie: Voorwaarden </strong><p>", unsafe_allow_html=True)
            for v in data_prm_vw["Voorwaarde"]:
                st.write(f"* {v}")

            st.markdown("<p style='font-size: 17px'> <strong>Premie: Bedragen</strong><p>", unsafe_allow_html=True)
            for v in data_bdg["Bedrag"]:
                st.write(f"* {v}")

            st.markdown("<p style='font-size: 17px'> <strong>Premie: Aanvraag Links</strong><p>", unsafe_allow_html=True)
            for a, l in zip(data_link["Aanvraag"], data_link["Link"]):
                st.markdown(f"* [{a}]({l})")

            st.markdown("<p style='font-size: 17px'> <strong>Meer informatie</strong><p>", unsafe_allow_html=True)
            st.markdown("""
           *  <p style='font-size: 16px' >Voor een overzicht van alle premies: ga naar de <strong><u>premies</u></strong> links in de navigatiebalk<p>""", unsafe_allow_html=True)

        with groepsaankopen:
            st.write("#### Groepsaankopen")
            st.write("Voor deze techniek kan je beroep doen op de volgende groepsaankopen:")
            for g, l in zip(data_gak["Groepsaankoop"], data_gak["Link"]):
                st.markdown(f"* [{g}]({l})")
    
        st.markdown("""
                <h1> 3. Uitvoeringsfase</h1>
                <p style='text-align: justify'>
                Bij de uitvoeringsfase maak je eventuele aanpassingen op basis van de individuele prioriteiten van het project en het budget. Zowel de verschillende mogelijke premies (zie tabblad premies) als mogelijkheden op vlak van groepsaankopen (zie tabblad groepsaankopen) kunnen hierbij helpen.
                </p>
                """, unsafe_allow_html=True)
