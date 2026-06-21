import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page (toute la largeur)
st.set_page_config(layout="wide", page_title="Projet Géomatique - Tivaouane Peulh-Niaga")

# Masquer le menu Streamlit et le footer (le "truc GitHub")
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Ton code HTML complet (inclus ton CSS original)
html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://js.arcgis.com/4.26/esri/themes/light/main.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        body { margin: 0; font-family: sans-serif; background-color: #0d2a4f; color: white; scroll-behavior: smooth; }
        .top-bar { display: flex; justify-content: space-between; align-items: center; padding: 10px 20px; background-color: #0d2a4f; height: 70px; position: sticky; top: 0; z-index: 1000; }
        .logo { height: 50px; border-radius: 5px; }
        .video-container { position: relative; width: 100%; height: 500px; overflow: hidden; }
        .bg-video { width: 100%; height: 100%; object-fit: cover; }
        .overlay-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; }
        #viewDiv { height: 550px; width: 100%; border: 2px solid #1a4d8c; border-radius: 10px; margin-top: 25px; }
        .btn-pdf { background: #28a745; color: white; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; display: block; margin: 20px auto; font-weight: bold; }
    </style>
</head>
<body id="contenu-pdf">

    <header class="top-bar">
        <img src="https://cedtleg15.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-22-at-18.43.22-300x300.jpeg.webp" class="logo">
    </header>

    <section class="video-container">
        <video autoplay muted loop playsinline class="bg-video">
            <source src="https://d1p1y5pyxk2k6i.cloudfront.net/4medy%2Ffile%2Fec65fe6e8f3ecc3bce0f20f983350485_cb1c20077b06dd0f22bd78b96723212f.mp4" type="video/mp4">
        </video>
        <div class="overlay-text"><h1>Apport de la géomatique</h1><p>Commune de Tivaouane Peulh-Niaga</p></div>
    </section>

    <main style="max-width: 900px; margin: 0 auto; padding: 40px 20px;">
        <h2>Carte interactive</h2>
        <div id="viewDiv"></div>
        <button class="btn-pdf" onclick="generatePDF()">Télécharger le rapport (PDF)</button>
    </main>

    <script src="https://js.arcgis.com/4.26/init.js"></script>
    <script>
        function generatePDF() { html2pdf().from(document.getElementById('contenu-pdf')).save('Rapport.pdf'); }
        
        require(["esri/Map", "esri/views/MapView", "esri/layers/GeoJSONLayer"], (Map, MapView, GeoJSONLayer) => {
            const map = new Map({ basemap: "satellite" });
            const view = new MapView({ container: "viewDiv", map: map, center: [-17.24, 14.83], zoom: 13 });
            
            // Remplace ces liens par tes liens NPOINT.IO (fichiers JSON)
            const layers = [
                {url: 'https://api.npoint.io/TON_ID_PNR', color: 'green'},
                {url: 'https://api.npoint.io/TON_ID_PP', color: 'orange'}
            ];
            layers.forEach(l => map.add(new GeoJSONLayer({ url: l.url })));
        });
    </script>
</body>
</html>
"""

# Afficher le tout
components.html(html_code, height=1500)
