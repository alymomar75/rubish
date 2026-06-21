import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration plein écran
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 2. Injection des variables JSON directement dans le script
# Remplace les {} par le contenu de tes fichiers JSON
json_pnr = {"type": "FeatureCollection", "features": []}
json_pp = {"type": "FeatureCollection", "features": []}

# 3. Masquer interface Streamlit
st.markdown("""<style>
    [data-testid="stSidebar"] {display: none;}
    .main {padding: 0 !important;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>""", unsafe_allow_html=True)

# 4. Le HTML en mode 100% écran
html_content = f"""
<!DOCTYPE html>
<html lang="fr" style="height: 100%; width: 100%;">
<body style="margin: 0; height: 100%; width: 100%; background-color: #0d2a4f; color: white;">
    <div id="viewDiv" style="height: 100vh; width: 100vw;"></div>
    
    <script src="https://js.arcgis.com/4.26/init.js"></script>
    <script>
        // Passage des variables Python vers JS
        const dataPNR = {json_pnr};
        const dataPP = {json_pp};

        require(["esri/Map", "esri/views/MapView", "esri/layers/GeoJSONLayer"], (Map, MapView, GeoJSONLayer) => {
            const map = new Map({ basemap: "satellite" });
            const view = new MapView({ container: "viewDiv", map: map, center: [-17.24, 14.83], zoom: 13 });
            
            function addLocalData(data, color) {{
                const blob = new Blob([JSON.stringify(data)], {{type: "application/json"}});
                map.add(new GeoJSONLayer({{
                    url: URL.createObjectURL(blob),
                    renderer: {{ type: "simple", symbol: {{ type: "simple-marker", color: color, size: 8 }} }}
                }}));
            }}
            
            addLocalData(dataPNR, 'green');
            addLocalData(dataPP, 'orange');
        });
    </script>
</body>
</html>
"""

components.html(html_content, height=1000)
