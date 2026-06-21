import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(layout="wide", page_title="Projet Géomatique - Aly Momar Diallo")

# Le HTML complet intégrant toute ton interface
html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://js.arcgis.com/4.26/esri/themes/light/main.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        body { margin: 0; font-family: sans-serif; background-color: #0d2a4f; color: white; }
        .top-bar { display: flex; justify-content: space-between; align-items: center; padding: 10px 20px; background-color: #0d2a4f; }
        .logo { height: 50px; border-radius: 5px; }
        .video-container { width: 100%; height: 500px; overflow: hidden; position: relative; }
        .bg-video { width: 100%; height: 100%; object-fit: cover; }
        .overlay-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; }
        #viewDiv { height: 550px; width: 100%; border: 2px solid #4fa3d1; margin-top: 20px; border-radius: 10px; }
        .historique-images { display: flex; gap: 10px; margin-top: 20px; }
        .historique-images img { width: 33%; height: 200px; object-fit: cover; border-radius: 8px; }
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

    <main style="padding: 20px;">
        <h2>Carte interactive</h2>
        <div id="viewDiv"></div>
        
        <h2>Historique</h2>
        <p>La commune trouve ses racines dans un ensemble de villages historiques... (ton texte ici).</p>
        <div class="historique-images">
            <img src="https://www.dgpu.org/wp-content/uploads/2021/10/ZOOM-RETBA-SUD_Page_22-scaled-e1634153969504.jpg">
            <img src="https://www.dgpu.org/wp-content/uploads/2021/10/ZOOM-RETBA-SUD_Page_05-scaled-e1634153688549.jpg">
            <img src="https://actu.rts.sn/wp-content/uploads/2025/12/vill.jpg">
        </div>
        
        <button class="btn-pdf" onclick="generatePDF()">Télécharger le rapport (PDF)</button>
    </main>

    <script src="https://js.arcgis.com/4.26/init.js"></script>
    <script>
        function generatePDF() { html2pdf().from(document.body).save('Rapport_Geomatique.pdf'); }
        
        require(["esri/Map", "esri/views/MapView", "esri/layers/GeoJSONLayer"], (Map, MapView, GeoJSONLayer) => {
            const map = new Map({ basemap: "satellite" });
            const view = new MapView({ container: "viewDiv", map: map, center: [-17.24, 14.83], zoom: 13 });
            
            // IMPORTANT : Tes URLs npoint ici
            const urls = [
                'https://api.npoint.io/VOTRE_ID_PNR',
                'https://api.npoint.io/VOTRE_ID_PP'
            ];
            urls.forEach(url => map.add(new GeoJSONLayer({ url: url })));
        });
    </script>
</body>
</html>
"""

# Intégration
components.html(html_code, height=1800)
