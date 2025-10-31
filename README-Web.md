# LogNotebook Web Interface

A simple web interface for querying Humio logs and visualizing event flows as flowcharts.

## Features

- **Interactive Query Interface**: Enter correlation IDs, select repositories, and configure time ranges
- **Real-time Visualization**: Generate flowcharts directly from Humio logs
- **11 Visual Themes**: Choose from Light, Unicorn, Matrix, Vaporwave, and more
- **Download SVG**: Save flowcharts for documentation or offline viewing
- **Clean UI**: Built with Streamlit for a responsive, modern interface

## Prerequisites

1. **Python 3.8+**
2. **Graphviz system library** (required for rendering)
3. **Your Humio token**

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Graphviz (System Dependency)

**macOS:**
```bash
brew install graphviz
```

**Ubuntu/Debian:**
```bash
sudo apt-get install graphviz graphviz-dev
```

**Windows:**
Download from [graphviz.org](https://graphviz.org/download/)

### 3. Configure Environment Variables

Copy the example environment file and add your Humio token:

```bash
cp example.env .env
```

Edit `.env` and add your actual Humio token:

```
HUMIO_TOKEN=your_actual_humio_token_here
```

## Running the Web Interface

Start the Streamlit application:

```bash
streamlit run app.py
```

The web interface will automatically open in your browser at `http://localhost:8501`

## Usage

### 1. Enter Query Parameters

- **Correlation ID**: The correlation ID you want to analyze
- **Repository**: Choose between `sb-demo` (DEMO) or `sb-production` (PROD)
- **Time Range**: Select how far back to search (3h, 12h, 1d, 2d, 7d, 30d)
- **Theme**: Select your preferred visual theme

### 2. Generate Flowchart

Click the "Generate Flowchart" button. The application will:
1. Query Humio for logs matching your correlation ID
2. Process the events and create a flowchart
3. Display the interactive SVG visualization

### 3. Download Results

Use the "Download SVG" button to save the flowchart for:
- Documentation
- Sharing with team members
- Offline analysis
- Embedding in reports

## Available Themes

Choose from 11 different visual themes:

1. **Light** - Clean, professional light theme (default)
2. **Unicorn** - Colorful, playful theme
3. **Hotdog** - High contrast retro theme
4. **Vaporwave** - Pink and cyan aesthetic
5. **Gameboy** - Green monochrome retro
6. **Oceanic** - Blue ocean-inspired theme
7. **Matrix** - Green on black hacker aesthetic
8. **Autumn Leaves** - Warm fall colors
9. **Cyberpunk** - Neon futuristic theme
10. **Rainbow** - Full spectrum colors
11. **Solarized** - Popular developer theme

## Troubleshooting

### "HUMIO_TOKEN not found" Error

Make sure:
- You've created a `.env` file in the project root
- The file contains: `HUMIO_TOKEN=your_actual_token`
- You've restarted the Streamlit app after creating the file

### "No events found" Warning

This means no log events were found for the correlation ID. Check:
- The correlation ID is correct
- The selected repository has access to these logs
- The time range is appropriate (events might be older)

### Graphviz Errors

If flowchart generation fails:
- Ensure Graphviz system library is installed
- Verify installation: `dot -V` in terminal
- Restart the Streamlit app after installing Graphviz

### Port Already in Use

If port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

## Configuration Options

You can customize Streamlit behavior with command-line flags:

```bash
# Custom port
streamlit run app.py --server.port 8080

# Disable auto-reload
streamlit run app.py --server.runOnSave false

# Custom browser
streamlit run app.py --browser.gatherUsageStats false
```

## Development

The web interface consists of:

- `app.py` - Main Streamlit application (UI)
- `web/app_logic.py` - Backend logic (queries and flowchart generation)
- `log_to_graph/` - Core library (shared with Jupyter notebooks)

All changes to `app.py` are automatically detected and the app will reload.

## Comparison with Jupyter Notebooks

| Feature | Web Interface | Jupyter Notebooks |
|---------|---------------|-------------------|
| Setup | Simple - just run `streamlit run app.py` | Requires Jupyter environment |
| UI | Clean, user-friendly web interface | Code-based, technical |
| Sharing | Share URL, no code knowledge needed | Requires Jupyter to run |
| Customization | Limited to UI options | Full Python code access |
| Best For | End users, quick queries, demos | Development, experimentation |

## Next Steps

- Customize themes by editing files in `log_to_graph/flowchart/theme/`
- Add more repositories to the dropdown in `app.py`
- Extend query capabilities in `web/app_logic.py`
- Deploy to cloud platforms (Streamlit Cloud, Heroku, etc.)

## Support

For issues or questions:
- Check the main project documentation
- Review Humio API documentation
- Verify your Humio token has correct permissions
