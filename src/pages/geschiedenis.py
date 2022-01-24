"""Home page shown when the user enters the application"""
import streamlit as st
import pandas as pd
import awesome_streamlit as ast
from PIL import Image

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
    st.markdown("<h1>Geschiedenis van de 19&#x1D49-eeuwse arbeiderswoningen in Brugge</h1>", unsafe_allow_html=True)
    st.markdown("## Arbeiderswoningen in Vlaanderen in de 19&#x1D49 eeuw")
    # st.image("images/erfgoed_brugge.jpeg")
    st.markdown("""
    <p style='text-align: justify'>
    Op het einde van de 18<sup>e</sup> eeuw drong in Vlaanderen, door de bevolkingsexplosie in verschillende steden, de sociale problematiek van de vraag naar arbeiderswoningen zich op. De woningen zouden onderdak bieden aan de vele arbeiders in de fabrieken. Dit woningvraagstuk werd niet meteen gezien als een materieel probleem. De woningen werden niet ontworpen vanuit een rechtvaardigheidsgevoel, maar vanuit een angst voor een arbeidersopstand. Er werd bij de woonconcepten gestreefd naar optimale controle, waarbij opvoeding en sociale disciplinering centraal stonden. De arbeiders gaven hierbij hun vrijheid voor een stuk op, in ruil voor materiële welstand.
    <br><br>
    Dergelijke arbeiderswijken, Beluiken, werden in de 19<sup>e</sup> eeuw in grote aantallen in de Vlaamse steden gebouwd. Nergens hadden deze woonwijken zo een omvang als in Gent, maar ook in Brugge kwamen ze tot stand. Naast de controlefunctie en de betere productIne Verhaegheiteit van de arbeiders zorgden deze kleine woningen ook voor opbrengsten. De woningen hadden slechts grondoppervlaktes van zo’n 15 tot 25m<sup>2</sup>. Doordat er vaak meerdere gezinnen in één woning samenleefden onder slechte leefomstandigheden, kwam de gezondheid van de arbeiders in het gedrang. Bij gebrek aan voorstellen, waagden artsen zich aan de bouw en inrichting van gezonde arbeiderswoningen. Eveneens werden in de tweede helft van de 19<sup>e</sup> eeuw initiatieven genomen om beluiken te onderzoeken en te registreren en kwam er de verplichting om een bouwaanvraag in te dienen (Devriese, 1970; Adriaensen, 1970; Devriese, 2015).
    </p>
    """,
    unsafe_allow_html=True)

    st.markdown("## De 19&#x1D49-eeuwse arbeiderswoningen in de Brugse binnenstad")
    st.markdown("""
    <p style='text-align: justify'>
    In Brugge kwam de industrialisatie maar traag op gang. Toch werden ook in deze binnenstad langzaam maar zeker meerdere arbeiderswijken gebouwd door de bevolkingsgroei omwille van de plattelandsvlucht rond 1840. Minder begoede mensen trokken naar de stad op zoek naar werk, waardoor ook daar de nood aan betaalbare woningen ontstond. De beluiken in Brugge werden in de volksmond ook ‘Fortjes’ genoemd. De Brugse Fortjes werden gebouwd door rijke burgers en middenstanders in functie van hun opbrengst. Ze bezaten meestal ruimte, een braakliggend perceel, waardoor ze de kans zagen om hiermee op korte termijn geld te verdienen.
    </p>
    """,
    unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <p style='text-align: justify'>
        De huisjes werden, net als in Gent en andere steden, gebouwd aan een pleintje, in een steeg of zelfs langs een smalle gang. De beschikbare grond werd zo vol mogelijk gepropt. Ze werden ‘geregulariseerd’ zonder bouwaanvraag, waardoor ze met minimaal comfort, zo goedkoop mogelijk werden gebouwd. Een waterput of pomp en enkele toiletten moesten door iedereen in het fort gedeeld worden. De huisjes hadden een kleine grondoppervlakte van gemiddeld 18m², waarin meerdere mensen samen woonden. Op vlak van hygiëne bracht dit heel wat problemen met zich mee. De Fortjes waren meestal slechts bereikbaar via een smal poortje.
        </p>
        """,
        unsafe_allow_html=True)

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.image("images/geschiedenis/fortje.png")
        st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 1: Het Wevershof in 1907. Bron: Erfgoedforum Brugge </strong></p>", unsafe_allow_html=True)
        # st.write("Het Wevershof in 1907 – Bron: Erfgoedforum Brugge")

    st.markdown("""
    <p style='text-align: justify'>
    Onder de rijke burgers en de middenklasse ontstonden er kleine kringen, door de aan- en verkoop van de Fortjes. Ze werden telkens als geheel verkocht, vaak meerdere keren op korte tijd, in functie van de opbrengsten. Er vonden dan ook weinig of geen ingrepen plaats om de levensomstandigheden van de inwoners te verbeteren.
    <br><br>
    Onder andere de Cholera uitbraken betekenden het einde voor vele wijken in Brugge. Meerdere krotwoningen werden, na controle van beschermingscomités, die een stadsingenieur en gezondheidsinspecteur aanstelden, opgekocht en afgebroken in de ‘strijd tegen de krotwoningen’. Door de strengere controles echter lag het sterftecijfer in Brugge veel lager dan bijvoorbeeld in Gent. Naast deze maatregelen, werden ook andere maatregelen getroffen in Brugge, zoals het reinigen van de waterlopen en greppels en het verplichten van aparte leidingen voor vervuilde waterlopen.
    <br><br>
    Veel van deze Fortjes werden dus gesloopt in de eerste helft van de 20<sup>e</sup> eeuw, sommigen iets later. Toch zijn naast een vergeten poortje, een oude pomp of een stuk muur ook nog heel wat Fortjes bewaard gebleven (Billiet et al., 2014).
    </p>
    """,
    unsafe_allow_html=True)

    st.markdown("## De huidige Fortjes in de Brugse binnenstad")
    st.image("images/geschiedenis/Afbeelding 2.png", use_column_width=True)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 2: Kaart gegenereerd via Snazzy Maps - Bewerkt via Adobe Photoshop. </strong></p>", unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align: justify'>
    De 19<sup>e</sup>-eeuwse arbeiderswoningen die bewaard bleven bezitten een erfgoedwaarde voor het stadsbeeld. Niet al deze 19<sup>e</sup>-eeuwse arbeiderswijken zijn opgenomen in de inventaris van het bouwkundig erfgoed, maar ze bezitten wel allemaal dezelfde erfgoedkenmerken, die van waardevolle betekenis zijn voor het stadsbeeld. Bij een renovatie ervan, moet dit uitzicht bewaard blijven met de volgende kenmerken:
    </p>
    """,
    unsafe_allow_html=True)

    st.markdown("""
    * Eenheidsbebouwing: De woningen zijn in serie gebouwd en worden best gerestaureerd naar hun oorspronkelijke uitzicht.
    * Meestal anderhalve bouwlaag met een repeterend of spiegelend schema van twee traveeën.
    * Zadeldak met Vlaamse pannen met meestal een wit- of geelbeschilderde bakstenen gevel en een grijze of zwarte plint.
    * Sommige huizen hebben een doorlopende dorpel onder het bovenvenster en een blind venster boven de deur.

    Enkele voorbeelden:
    """)

    @st.experimental_memo
    def load_image(img_pth):
        image = Image.open(img_pth)
        return image

    img3 = load_image("images/geschiedenis/Afbeelding 3.png")
    st.image(img3)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 3: Sint-Claradreef 20-34 (Foto: Ine Verhaeghe) </strong></p>", unsafe_allow_html=True)

    img4 = load_image("images/geschiedenis/Afbeelding 4.png")
    st.image(img4)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 4: Vlamingdam 59-79 (Foto: Ine Verhaeghe)</strong></p>", unsafe_allow_html=True)

    img5 = load_image("images/geschiedenis/Afbeelding 5.png")
    st.image(img5)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 5: Sint-Gilliskoorstraat 6-12 (Foto: Ine Verhaeghe)</strong></p>", unsafe_allow_html=True)

    img6 = load_image("images/geschiedenis/Afbeelding 6.png")
    st.image(img6)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 6: Wevershof 1-11 (Foto: Ine Verhaeghe)</strong></p>", unsafe_allow_html=True)

    img7 = load_image("images/geschiedenis/Afbeelding 7.png")
    st.image(img7)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 7: Sulferbergstraat 13-27 (Foto: Ine Verhaeghe)</strong></p>", unsafe_allow_html=True)

    img8 = load_image("images/geschiedenis/Afbeelding 8.png")
    st.image(img8)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 8: Bidderstraat (Foto: Ine Verhaeghe)</strong></p>", unsafe_allow_html=True)

    img9 = load_image("images/geschiedenis/Afbeelding 9.png")
    st.image(img9)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 9: Eiland (Foto: Ine Verhaeghe)</strong></p>", unsafe_allow_html=True)

    img10 = load_image("images/geschiedenis/Afbeelding 10.png")
    st.image(img10)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 10: Kleine Kuipersstraat (Foto: Ine Verhaeghe)</strong></p>", unsafe_allow_html=True)

    img11 = load_image("images/geschiedenis/Afbeelding 11.png")
    st.image(img11)
    st.markdown("<p style='font-size: 14px;'><strong>Afbeelding 11: Visspaanstraat (Foto: Ine Verhaeghe)</strong></p>", unsafe_allow_html=True)

    st.markdown("## Referenties")
    st.markdown("""
* Adriaensen, F., Dr.Adolphe Burggraeve (1970). Arbeider als patient, stad als panoptikum. _Tijdschrift Voor Geschiedenis van Techniek En Industriële Cultuur_, 9 (36), 5–24. https://doi.org/10.21825/tgtic.v9i36.7970
* Billiet, A., Coudeville, M., Vranken, B. (2014). _De fortjes van Brugge. De huisvesting van het 19e-eeuwse proletariaat._ Geraadpleegd op 20 oktober 2021 via https://www.academia.edu/21627892/De_fortjes_van_Brugge
* Devriese, L. (1970). De grote beluikenconcentratie in de Gentse overscheldewijk in de 18de en vroege 19de eeuw. _Tijdschrift Voor Industriële Cultuur_, 19(75), 13–32. https://doi.org/10.21825/tic.v19i75.8190
* Devriese, L. (2015). Dat eigenaardige Gentse woord “cité, citeetse” en zijn homologen: koer, gang, poortje en beluik. _Van Mensen En Dingen: Tijdschrift Voor Volkscultuur in Vlaanderen_, 13(1), 30–44. https://doi.org/10.21825/vmend.v13i1.5010    
    """)
