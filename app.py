import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration : page en mode large, sans sidebar
st.set_page_config(layout="wide", page_title="Géomatique - Tivaouane Peulh-Niaga")

# 2. Masquage TOTAL de l'interface Streamlit (Menu, Sidebar, Header, Footer)
# On force le padding à 0 pour que le contenu touche les bords
hide_everything = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .main .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
"""
st.markdown(hide_everything, unsafe_allow_html=True)

# 3. Ton contenu HTML complet (le même que précédemment)
html_content = """
<!DOCTYPE html>
<html lang="fr" style="width: 100%; height: 100%;">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://js.arcgis.com/4.26/esri/themes/light/main.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        body { margin: 0; font-family: sans-serif; background: #0d2a4f; color: white; }
        .top-bar { display: flex; padding: 15px 40px; background: #0d2a4f; align-items: center; gap: 20px; }
        .video-box { width: 100%; height: 500px; overflow: hidden; }
        .bg-video { width: 100%; height: 100%; object-fit: cover; }
        .content { max-width: 1200px; margin: auto; padding: 40px 20px; }
        #viewDiv { height: 600px; width: 100%; border: 3px solid #1a4d8c; border-radius: 10px; }
        .grid-img { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px; }
        .grid-img img { width: 100%; height: 200px; object-fit: cover; border-radius: 5px; }
    </style>
</head>
<body id="pdf-content">
    <header class="top-bar">
        <img src="https://cedtleg15.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-22-at-18.43.22-300x300.jpeg.webp" style="height:50px;">
        <img src="https://sonaged.sn/wp-content/uploads/2025/01/cropped-logo_siteWeb-3.png" style="height:50px;">
    </header>

    <div class="video-box">
        <video autoplay muted loop playsinline class="bg-video">
            <source src="https://d1p1y5pyxk2k6i.cloudfront.net/4medy%2Ffile%2Fec65fe6e8f3ecc3bce0f20f983350485_cb1c20077b06dd0f22bd78b96723212f.mp4" type="video/mp4">
        </video>
    </div>

    <div class="content">
        <h2>Présentation & Historique</h2>
        <p>Projet de cartographie des déchets - Commune de Tivaouane Peulh-Niaga.</p>
        <div class="grid-img">
            <img src="https://www.dgpu.org/wp-content/uploads/2021/10/ZOOM-RETBA-SUD_Page_22-scaled-e1634153969504.jpg">
            <img src="https://www.dgpu.org/wp-content/uploads/2021/10/ZOOM-RETBA-SUD_Page_05-scaled-e1634153688549.jpg">
            <img src="https://actu.rts.sn/wp-content/uploads/2025/12/vill.jpg">
        </div>
        
        <h2 style="margin-top:40px;">Carte Interactive</h2>
        <div id="viewDiv"></div>
        <button onclick="html2pdf().from(document.getElementById('pdf-content')).save()" style="margin-top:20px; padding:15px; background:#28a745; color:white; border:none; border-radius:5px; cursor:pointer; font-weight:bold;">Télécharger le rapport PDF</button>
    </div>

    <script src="https://js.arcgis.com/4.26/init.js"></script>
    <script>
        require(["esri/Map", "esri/views/MapView", "esri/layers/GeoJSONLayer"], (Map, MapView, GeoJSONLayer) => {
            const map = new Map({ basemap: "satellite" });
            const view = new MapView({ container: "viewDiv", map: map, center: [-17.24, 14.83], zoom: 13 });
            // Remplacer avec tes liens npoint
            const url = 'https://api.npoint.io/TON_ID_ICI';
            map.add(new GeoJSONLayer({ url: url }));
        });
    </script>
</body>
</html>
"""

# Rendu sans scroll interne pour une fluidité totale
components.html(html_content, height=2000, scrolling=False)
