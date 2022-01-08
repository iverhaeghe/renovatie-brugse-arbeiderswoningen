"""Home page shown when the user enters the application"""
import streamlit as st
import pandas as pd
import awesome_streamlit as ast

@st.experimental_memo
def load_data():
    data = pd.read_excel("data/BAP-matrix-versie2.xlsx", sheet_name=None)
    lookup_detail = {eis: detail for eis, detail in zip(data['Eis-Detail']["Eis"], data['Eis-Detail']["Detail"])}
    col_eis = [e for e in data['Element-Ingreep-Eis'].columns if "Eis" in e]
    for c in col_eis:
        data["Element-Ingreep-Eis"]["Detail-" + c] = [lookup_detail[e] if e in lookup_detail.keys() else ""for e in data['Element-Ingreep-Eis'].fillna("")[c]]
    return data

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""

    data = load_data()
    with st.spinner("Loading Home ..."):
        st.markdown("<h1>Geschiedenis van de 19e-eeuwse arbeiderswoningen in Brugge</h1>", unsafe_allow_html=True)
        st.markdown("## Arbeiderswoningen in Vlaanderen in de 19e eeuw")
        # st.image("images/erfgoed_brugge.jpeg")
        st.markdown("""
        <p style='text-align: justify'>
        Op het einde van de 18<sup>e</sup> eeuw drong in Vlaanderen, door de bevolkingsexplosie in verschillende steden, de sociale problematiek van de vraag naar arbeiderswoningen zich op. Het waren artsen die de eerste voorstellen deden tot de bouw en inrichting van gezonde arbeiderswoningen. Een aanleiding hiervoor was de Cholera uitbraak in 1832. De woningen zouden de levensomstandigheden moeten verbeteren en vooral de hygiënische omstandigheden van de vele arbeiders in de fabrieken. Bij gebrek aan voorstellen, waagden artsen zich zelf aan het ontwerpen van woonconcepten.
        <br><br>
        Het woningvraagstuk werd niet meteen gezien als een materieel probleem. De woningen werden niet ontworpen vanuit een rechtvaardigheidsgevoel, maar vanuit een angst voor een arbeidersopstand. Er werd bij de woonconcepten gestreefd naar optimale controle, waarbij opvoeding en sociale disciplinering centraal stonden. De arbeiders gaven hierbij hun vrijheid voor een stuk op, in ruil voor materiële welstand. Daarnaast zorgden de betere leefomstandigheden ook voor een betere productiviteit op de werkvloer.
        <br><br>
        Dergelijke arbeiderswijken, Beluiken, werden in de 19<sup>e</sup> eeuw in grote aantallen in de Vlaamse steden gebouwd. Nergens hadden deze woonwijken zo een omvang als in Gent, maar ook in Brugge kwamen ze tot stand. Naast de controlefunctie en de betere productiviteit van de arbeiders zorgden deze kleine woningen ook voor opbrengsten. De woningen hadden slechts oppervlaktes van zo’n 15 tot 25m<sup>2</sup>.
        </p>
        """,
        unsafe_allow_html=True)

        st.markdown("## De 19e-eeuwse arbeiderswoningen in de Brugse binnenstad")
        st.markdown("""
        <p style='text-align: justify'>
        In Brugge kwam de industrialisatie maar traag op gang. Toch werden ook in deze binnenstad langzaam maar zeker meerdere arbeiderswijken gebouwd door de bevolkingsgroei omwille van de plattelandsvlucht rond 1840. Minder begoede mensen trokken naar de stad op zoek naar werk, waardoor ook daar de nood aan betaalbare woningen ontstond. De beluiken in Brugge werden in de volksmond ook ‘Fortjes’ genoemd. De Brugse Fortjes werden gebouwd door rijke burgers en welgestelde middenstanders in functie van hun opbrengst. Ze bezaten meestal ruimte, zoals een koer, waardoor ze de kans zagen om hiermee op korte termijn geld te verdienen.
        </p>
        """,
        unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <p style='text-align: justify'>
            De huisjes werden, net als in Gent en andere steden, gebouwd aan een pleintje, in een steeg of zelfs langs een smalle gang. De beschikbare grond, vaak het erf van de bouwheer, werd zo vol mogelijk gepropt. Ze werden ‘geregulariseerd’ zonder bouwaanvraag, waardoor ze met minimaal comfort, zo goedkoop mogelijk werden gebouwd. Een waterput of pomp en enkele toiletten moesten door iedereen in het fort gedeeld worden. De huisjes hadden een kleine oppervlakte van gemiddeld 18m<sup>2</sup>, waarin meerdere mensen samen woonden. Op vlak van hygiëne bracht dit heel wat problemen met zich mee. De Fortjes waren meestal slechts bereikbaar via een smal poortje.
            </p>
            """,
            unsafe_allow_html=True)

        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image("images/geschiedenis/fortje.png")
            st.markdown("<p style='font-size: 14px;'><strong>Het Wevershof in 1907 – Bron: Erfgoedforum Brugge </strong></p>", unsafe_allow_html=True)
            # st.write("Het Wevershof in 1907 – Bron: Erfgoedforum Brugge")

        st.markdown("""
        <p style='text-align: justify'>
        Onder de rijke burgers en welgestelde middenklasse ontstonden er kleine kringen, door de aan- en verkoop van de Fortjes. Ze werden telkens als geheel verkocht, vaak meerdere keren op korte tijd, in functie van de opbrengsten. Er vonden dan ook weinig of geen ingrepen plaats om de levensomstandigheden van de inwoners te verbeteren.

        Hoewel de Cholera uitbraken een aanleiding waren tot het bouwen van deze woningen in Vlaanderen, betekenden deze uitbraken ook het einde voor vele wijken in Brugge. Meerdere krotwoningen werden, na controle van beschermingscomités, die een stadsingenieur en gezondheidsinspecteur aanstelden, opgekocht en afgebroken in de ‘strijd tegen de krotwoningen’. Door de strengere controles echter lag het sterftecijfer in Brugge veel lager dan bijvoorbeeld in Gent. Naast deze maatregelen, werden ook andere maatregelen getroffen in Brugge, zoals het reinigen van de waterlopen en greppels en het verplichten van aparte leidingen voor vervuilde waterlopen.

        Veel van deze Fortjes werden dus gesloopt in de eerste helft van de 20<sup>e</sup> eeuw, sommigen iets later. Toch zijn naast een vergeten poortje, een oude pomp of een stuk muur ook nog enkele Fortjes bewaard gebleven.

        </p>
        """,
        unsafe_allow_html=True)

