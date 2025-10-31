"""
LogNotebook Web Interface
A Streamlit application for querying Humio logs and visualizing flowcharts.
"""
import streamlit as st
import os
from dotenv import load_dotenv
from web.app_logic import generate_flowchart_svg
from log_to_graph.flowchart import (
    LIGHT_THEME, UNICORN_THEME, HOTDOG_THEME, VAPORWAVE_THEME,
    GAMEBOY_THEME, OCEANIC_THEME, MATRIX_THEME, AUTUMN_LEAVES_THEME,
    CYBERPUNK_THEME, RAINBOW_THEME, SOLARIZED_THEME
)

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="LogNotebook - Humio Log Visualizer",
    page_icon="\U0001F4CA",
    layout="wide"
)

# Theme mapping
THEMES = {
    "Light": LIGHT_THEME,
    "Unicorn": UNICORN_THEME,
    "Hotdog": HOTDOG_THEME,
    "Vaporwave": VAPORWAVE_THEME,
    "Gameboy": GAMEBOY_THEME,
    "Oceanic": OCEANIC_THEME,
    "Matrix": MATRIX_THEME,
    "Autumn Leaves": AUTUMN_LEAVES_THEME,
    "Cyberpunk": CYBERPUNK_THEME,
    "Rainbow": RAINBOW_THEME,
    "Solarized": SOLARIZED_THEME
}

# Title and description
st.title("\U0001F4CA LogNotebook - Humio Log Visualizer")
st.markdown("Query Humio logs by correlation ID and visualize event flows as interactive flowcharts.")

# Check for Humio token
user_token = os.getenv("HUMIO_TOKEN")
if not user_token:
    st.error("\u26A0\uFE0F **HUMIO_TOKEN not found!** Please set your Humio token in the `.env` file.")
    st.stop()

# Create input form
st.subheader("\U0001F4DD Query Parameters")

col1, col2 = st.columns(2)

with col1:
    correlation_id = st.text_input(
        "Correlation ID",
        placeholder="Enter correlation ID (e.g., 33f9301e43744d56f34cebc74690fc4d)",
        help="The correlation ID to filter logs"
    )

    repo = st.selectbox(
        "Repository",
        options=["sb-demo", "sb-production"],
        help="Select the Humio repository to query"
    )

with col2:
    start = st.selectbox(
        "Time Range",
        options=["3h", "12h", "1d", "2d", "7d", "30d"],
        index=2,  # Default to "1d"
        help="How far back to search for logs"
    )

    theme_name = st.selectbox(
        "Theme",
        options=list(THEMES.keys()),
        index=0,  # Default to "Light"
        help="Visual theme for the flowchart"
    )

# Query button
query_button = st.button("\U0001F680 Generate Flowchart", type="primary", use_container_width=True)

# Handle query execution
if query_button:
    if not correlation_id:
        st.warning("\u26A0\uFE0F Please enter a correlation ID.")
    else:
        with st.spinner("Querying Humio logs and generating flowchart..."):
            try:
                # Get selected theme
                selected_theme = THEMES[theme_name]

                # Generate flowchart
                svg_output = generate_flowchart_svg(
                    user_token=user_token,
                    repo=repo,
                    start=start,
                    correlation_id=correlation_id,
                    theme=selected_theme
                )

                if svg_output:
                    st.success(f"\u2705 Flowchart generated successfully for correlation ID: `{correlation_id}`")

                    # Display the SVG with pan and zoom controls
                    st.subheader("\U0001F4C8 Flowchart Visualization")

                    # Create HTML wrapper with svg-pan-zoom library
                    html_with_controls = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
                        <style>
                            body {{
                                margin: 0;
                                padding: 0;
                                overflow: hidden;
                            }}
                            #svg-container {{
                                width: 100%;
                                height: 100vh;
                                border: 1px solid #ddd;
                                background: #f9f9f9;
                            }}
                            .controls {{
                                position: absolute;
                                top: 10px;
                                right: 10px;
                                background: white;
                                padding: 10px;
                                border-radius: 5px;
                                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
                                z-index: 1000;
                            }}
                            .controls button {{
                                margin: 2px;
                                padding: 8px 12px;
                                border: 1px solid #ccc;
                                background: white;
                                cursor: pointer;
                                border-radius: 3px;
                                font-size: 14px;
                            }}
                            .controls button:hover {{
                                background: #f0f0f0;
                            }}
                            .controls button:active {{
                                background: #e0e0e0;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="controls">
                            <button onclick="panZoomInstance.zoomIn()" title="Zoom In">🔍+</button>
                            <button onclick="panZoomInstance.zoomOut()" title="Zoom Out">🔍−</button>
                            <button onclick="panZoomInstance.resetZoom()" title="Reset Zoom">↺ Reset</button>
                            <button onclick="panZoomInstance.fit()" title="Fit to Screen">⛶ Fit</button>
                            <button onclick="panZoomInstance.center()" title="Center">⊙ Center</button>
                        </div>
                        <div id="svg-container">
                            {svg_output}
                        </div>
                        <script>
                            // Initialize svg-pan-zoom
                            var panZoomInstance = svgPanZoom('#svg-container svg', {{
                                zoomEnabled: true,
                                controlIconsEnabled: false,
                                fit: true,
                                center: true,
                                minZoom: 0.1,
                                maxZoom: 10,
                                zoomScaleSensitivity: 0.3,
                                dblClickZoomEnabled: true,
                                mouseWheelZoomEnabled: true,
                                preventMouseEventsDefault: true
                            }});

                            // Keyboard shortcuts
                            document.addEventListener('keydown', function(e) {{
                                if (e.key === '+' || e.key === '=') {{
                                    panZoomInstance.zoomIn();
                                }} else if (e.key === '-' || e.key === '_') {{
                                    panZoomInstance.zoomOut();
                                }} else if (e.key === '0') {{
                                    panZoomInstance.resetZoom();
                                }} else if (e.key === 'f') {{
                                    panZoomInstance.fit();
                                }} else if (e.key === 'c') {{
                                    panZoomInstance.center();
                                }}
                            }});
                        </script>
                    </body>
                    </html>
                    """

                    st.components.v1.html(html_with_controls, height=800, scrolling=False)

                    # Controls help text
                    st.info("💡 **Controls**: Use mouse wheel to zoom, drag to pan. Keyboard: +/- (zoom), 0 (reset), F (fit), C (center)")

                    # Add download button
                    st.download_button(
                        label="\U0001F4BE Download SVG",
                        data=svg_output,
                        file_name=f"{correlation_id}.svg",
                        mime="image/svg+xml"
                    )
                else:
                    st.warning(f"\u26A0\uFE0F No events found for correlation ID: `{correlation_id}`")

            except Exception as e:
                st.error(f"\u274C Error generating flowchart: {str(e)}")
                st.exception(e)

# Footer with usage instructions
with st.expander("\U0001F4A1 How to Use"):
    st.markdown("""
    ### Steps:
    1. **Enter Correlation ID**: Paste the correlation ID you want to analyze
    2. **Select Repository**: Choose between `sb-demo` (DEMO) or `sb-production` (PROD)
    3. **Choose Time Range**: Select how far back to search (3 hours to 30 days)
    4. **Pick a Theme**: Select your preferred visual theme for the flowchart
    5. **Click Generate**: The flowchart will be displayed below

    ### Features:
    - **Interactive Visualization**: Pan and zoom the flowchart
    - **Download**: Save the SVG file for offline viewing or documentation
    - **Multiple Themes**: 11 different visual themes to choose from
    - **Real-time Queries**: Directly queries Humio API for fresh data

    ### Requirements:
    - Valid `HUMIO_TOKEN` in `.env` file
    - Access to the selected Humio repository
    - Valid correlation ID with existing log events
    """)
