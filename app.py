import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURATION PLEIN ÉCRAN
st.set_page_config(layout="wide", page_title="Gestion des Déchets - Tivaouane Peulh-Niaga")

# 2. MASQUER L'INTERFACE STREAMLIT (POUR LE PLEIN ÉCRAN)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            section[data-testid="stSidebar"] {display: none;}
            .main .block-container {padding: 0;}
            iframe {border: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. LE CODE HTML/CSS/JS COMPLET
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://js.arcgis.com/4.26/esri/themes/light/main.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0d2a4f; color: white; scroll-behavior: smooth; }
        
        /* Barre de navigation */
        .top-bar { display: flex; justify-content: space-between; align-items: center; padding: 10px 40px; background-color: #0d2a4f; height: 80px; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.3); }
        .logo-container { display: flex; gap: 20px; align-items: center; }
        .logo { height: 60px; width: auto; cursor: pointer; transition: 0.3s; }
        .logo:hover { transform: scale(1.05); }
        .action-btn { background: #1a4d8c; color: white; border: none; padding: 10px 20px; cursor: pointer; border-radius: 5px; font-weight: bold; font-size: 14px; text-transform: uppercase; }

        /* Vidéo Hero Section */
        .video-container { position: relative; width: 100%; height: 80vh; overflow: hidden; }
        .bg-video { width: 100%; height: 100%; object-fit: cover; }
        .overlay-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; width: 90%; text-shadow: 2px 2px 10px rgba(0,0,0,0.8); }
        .overlay-text h1 { font-size: 50px; margin-bottom: 10px; }
        .overlay-text p { font-size: 24px; color: #4fa3d1; }

        /* Contenu Principal */
        main { max-width: 1000px; margin: 0 auto; padding: 60px 20px; }
        h2 { color: #4fa3d1; font-size: 32px; border-bottom: 2px solid #1a4d8c; padding-bottom: 10px; text-align: center; }
        p { line-height: 1.8; color: #e0e0e0; font-size: 17px; }
        
        /* Sections Images */
        .img-zone { display: block; width: 100%; border-radius: 15px; margin: 30px 0; border: 3px solid #1a4d8c; }
        .historique-images { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 30px 0; }
        .historique-images img { width: 100%; height: 220px; object-fit: cover; border-radius: 10px; border: 2px solid #4fa3d1; }

        /* Carte ArcGIS */
        #viewDiv { height: 600px; width: 100%; border-radius: 15px; border: 3px solid #1a4d8c; margin: 30px 0; }

        /* Footer & Boutons */
        .footer { background: #0a213e; padding: 40px; text-align: center; border-top: 3px solid #4fa3d1; margin-top: 40px; }
        .btn-pdf { background: #28a745; color: white; padding: 18px 40px; border: none; border-radius: 8px; cursor: pointer; font-size: 18px; font-weight: bold; transition: 0.3s; }
        .btn-pdf:hover { background: #218838; transform: translateY(-2px); }
    </style>
</head>
<body id="contenu-pdf">

    <header class="top-bar">
        <div class="logo-container">
            <a href="https://cedtleg15.com/" target="_blank">
                <img src="https://cedtleg15.com/wp-content/uploads/2026/03/WhatsApp-Image-2026-03-22-at-18.43.22-300x300.jpeg.webp" alt="CEDT" class="logo">
            </a>
            <a href="https://sonaged.sn/" target="_blank">
                <img src="https://sonaged.sn/wp-content/uploads/2025/01/cropped-logo_siteWeb-3.png" alt="SONAGED" class="logo">
            </a>
        </div>
        <div class="actions-container">
            <button class="action-btn" onclick="window.scrollTo({top:0, behavior:'smooth'})">Accueil</button>
            <button class="action-btn" onclick="document.getElementById('carte').scrollIntoView({behavior:'smooth'})">Carte</button>
        </div>
    </header>

    <section class="video-container">
        <video autoplay muted loop playsinline class="bg-video">
            <source src="https://d1p1y5pyxk2k6i.cloudfront.net/4medy%2Ffile%2Fec65fe6e8f3ecc3bce0f20f983350485_cb1c20077b06dd0f22bd78b96723212f.mp4" type="video/mp4">
        </video>
        <div class="overlay-text">
            <h1>Apport de la géomatique</h1>
            <p>Gestion des déchets ménagers à Tivaouane Peulh-Niaga</p>
        </div>
    </section>

    <main>
        <section id="presentation">
            <h2>Présentation du Projet</h2>
            <p>Ce projet vise à moderniser la gestion des déchets dans la commune de Tivaouane Peulh-Niaga en utilisant les outils du Système d'Information Géographique (SIG). Nous cartographions les points de collecte et les zones critiques pour optimiser le ramassage.</p>
            <img src="https://cdn.corenexis.com/f/kRtzT6vWzHM.png" alt="Zone d'étude" class="img-zone">
        </section>

        <section id="historique">
            <h2>Historique de la Commune</h2>
            <p>Tivaouane Peulh-Niaga est une commune en forte expansion démographique. Historiquement composée de villages traditionnels, elle accueille aujourd'hui de grands projets urbains comme la Cité Apix, nécessitant une gestion environnementale rigoureuse.</p>
            <div class="historique-images">
                <img src="https://www.dgpu.org/wp-content/uploads/2021/10/ZOOM-RETBA-SUD_Page_22-scaled-e1634153969504.jpg" alt="Hist 1">
                <img src="https://www.dgpu.org/wp-content/uploads/2021/10/ZOOM-RETBA-SUD_Page_05-scaled-e1634153688549.jpg" alt="Hist 2">
                <img src="https://actu.rts.sn/wp-content/uploads/2025/12/vill.jpg" alt="Hist 3">
            </div>
        </section>

        <section id="carte">
            <h2>Carte Interactive des Déchets</h2>
            <div id="viewDiv"></div>
        </section>

        <div style="text-align: center; margin-top: 50px;">
            <button class="btn-pdf" onclick="generatePDF()">Télécharger le Rapport Complet (PDF)</button>
        </div>
    </main>

    <footer class="footer">
        <p>© 2026 - Réalisé par <strong>Aly Momar Diallo</strong> | BTS Géomatique CEDT G15</p>
    </footer>

    <script src="https://js.arcgis.com/4.26/init.js"></script>
    <script>
        function generatePDF() {
            const element = document.getElementById('contenu-pdf');
            html2pdf().from(element).set({
                margin: 5,
                filename: 'Rapport_Geomatique_Diallo.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            }).save();
        }

        require(["esri/Map", "esri/views/MapView", "esri/layers/GeoJSONLayer"], (Map, MapView, GeoJSONLayer) => {
            const map = new Map({ basemap: "satellite" });
            const view = new MapView({
                container: "viewDiv",
                map: map,
                center: [-17.24, 14.83],
                zoom: 13
            });

            // Remplacez ces liens par vos liens npoint.io ou liens RAW GitHub
            const layers = [
                {url: 'https://api.npoint.io/TON_ID_PNR', color: 'green', title: 'PNR'},
                {url: 'https://api.npoint.io/TON_ID_PP', color: 'orange', title: 'PP'}
            ];

            layers.forEach(l => {
                const layer = new GeoJSONLayer({
                    url: l.url,
                    title: l.title,
                    renderer: {
                        type: "simple",
                        symbol: { type: "simple-marker", color: l.color, size: 8, outline: { color: "white", width: 1 } }
                    }
                });
                map.add(layer);
            });
        });
    </script>
</body>
</html>
"""

# AFFICHAGE DU COMPOSANT HTML (Ajustement de la hauteur pour éviter le double scroll)
components.html(html_content, height=2800, scrolling=False)
