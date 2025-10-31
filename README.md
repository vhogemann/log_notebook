# LogNotebook

A powerful tool for querying Humio logs and visualizing event flows as interactive flowcharts. Track distributed system events by correlation ID and generate beautiful visual diagrams with customizable themes.

![Language](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Humio Integration**: Direct API integration to query logs by correlation ID
- **Interactive Flowcharts**: Visualize event sequences with pan/zoom controls
- **11 Visual Themes**: Customize appearance with built-in themes (Light, Matrix, Vaporwave, Cyberpunk, and more)
- **Multiple Interfaces**: Choose from web UI, Jupyter notebooks, or VS Code
- **Docker Support**: Containerized deployment with Docker Compose
- **SVG Export**: Download flowcharts for documentation and sharing
- **Real-time Queries**: Fresh data directly from Humio repositories

## Quick Start

### Option 1: Docker (Recommended)

The fastest way to get started:

```bash
# Clone the repository
git clone https://github.com/vhogemann/log_notebook.git
cd log_notebook

# Set up your Humio token
cp example.env .env
# Edit .env and add your HUMIO_TOKEN

# Start with Docker
./start-docker.sh
```

Choose your interface:
- **Web Interface** (port 8501) - User-friendly Streamlit UI
- **Jupyter Notebook** (port 8888) - Development environment
- **Both** - Run both simultaneously

### Option 2: Web Interface (Native)

For running the Streamlit web interface locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Install Graphviz (macOS)
brew install graphviz

# Configure environment
cp example.env .env
# Edit .env with your HUMIO_TOKEN

# Run the web interface
streamlit run app.py
```

Access at `http://localhost:8501`

### Option 3: Jupyter Notebook

For development and experimentation:

```bash
# Install dependencies
pip install -r requirements.txt

# Install Graphviz (macOS)
brew install graphviz

# Configure environment
cp example.env .env

# Open in Jupyter
jupyter notebook LogToGraph.ipynb
```

## Interfaces Comparison

| Feature | Web Interface | Jupyter Notebook | Docker |
|---------|---------------|------------------|--------|
| **Setup Time** | Quick | Medium | Fastest |
| **User Experience** | Simple UI | Code-based | Simple UI |
| **Best For** | End users, demos | Development, research | Quick start, deployment |
| **Customization** | Limited | Full Python access | Limited |
| **Dependencies** | Manual install | Manual install | Auto-installed |
| **Port** | 8501 | 8888 | Both available |

## Usage

### Web Interface

1. Enter your **Correlation ID**
2. Select **Repository** (sb-demo or sb-production)
3. Choose **Time Range** (3h, 12h, 1d, 2d, 7d, 30d)
4. Pick a **Theme** from 11 options
5. Click **Generate Flowchart**

**Interactive Controls:**
- Mouse wheel to zoom
- Click and drag to pan
- Buttons: Zoom In/Out, Reset, Fit, Center
- Keyboard: +/- (zoom), 0 (reset), F (fit), C (center)

### Jupyter Notebook

```python
from log_to_graph.humio import query_logs
from log_to_graph.flowchart import node_factory, FlowChart, LIGHT_THEME
from dotenv import load_dotenv
import os

load_dotenv()
user_token = os.getenv("HUMIO_TOKEN")

# Query logs
event_map = query_logs(
    user_token,
    repo="sb-demo",
    start="2d",
    correlation_id="your-correlation-id-here"
)

# Generate flowchart
correlation_id = list(event_map.keys())[0]
nodes = [node_factory(event) for event in event_map[correlation_id]]
flowchart = FlowChart(correlation_id, nodes, theme=LIGHT_THEME)

# Render
flowchart.to_graphviz().render('./output/flowchart')
```

## Available Themes

Choose from 11 carefully designed themes:

1. **Light** - Clean, professional (default)
2. **Dark** - High contrast dark mode
3. **Matrix** - Green on black hacker aesthetic
4. **Vaporwave** - Pink and cyan retro
5. **Cyberpunk** - Neon futuristic
6. **Unicorn** - Colorful and playful
7. **Hotdog** - High contrast retro
8. **Gameboy** - Green monochrome
9. **Oceanic** - Blue ocean-inspired
10. **Autumn Leaves** - Warm fall colors
11. **Rainbow** - Full spectrum
12. **Solarized** - Popular developer theme

## Project Structure

```
LogNotebook/
├── app.py                      # Streamlit web interface
├── web/
│   ├── app_logic.py           # Backend logic for web interface
├── log_to_graph/
│   ├── humio.py               # Humio API client
│   ├── flowchart/
│   │   ├── flowchart.py       # Flowchart generation
│   │   ├── node/              # Node types and factory
│   │   └── theme/             # Visual themes
├── LogToGraph.ipynb           # Main Jupyter notebook
├── LogToGraph_withAISummary.ipynb  # With AI summary generation
├── Dockerfile                 # Jupyter container
├── Dockerfile.web             # Web interface container
├── docker-compose.yml         # Multi-container setup
├── start-docker.sh            # Docker startup script
├── run_web.sh                 # Web interface launcher
└── requirements.txt           # Python dependencies
```

## Setup Guides

Detailed setup instructions for different environments:

- **[Docker Setup](README-Docker.md)** - Run with Docker Compose (recommended)
- **[Web Interface](README-Web.md)** - Streamlit web UI setup
- **[VS Code Setup](README-VSCode.md)** - Run Jupyter notebooks in VS Code

## Requirements

### System Requirements
- Python 3.8 or higher
- Graphviz (system package)
- Docker and Docker Compose (for containerized deployment)

### Python Dependencies
- `streamlit` - Web interface
- `graphviz` - Flowchart rendering
- `humiolib` - Humio API client
- `humanize` - Date/time formatting
- `python-dotenv` - Environment configuration
- `ipykernel`, `ipython` - Jupyter support (optional)

### Installing Graphviz

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

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
cp example.env .env
```

Edit `.env` and add your Humio token:

```
HUMIO_TOKEN=your_actual_humio_token_here
```

### Repositories

The default configuration supports two repositories:
- `sb-demo` - Demo environment
- `sb-production` - Production environment

To add more repositories, edit `app.py` or modify the notebook code.

## Troubleshooting

### Common Issues

**"HUMIO_TOKEN not found" Error**
- Ensure `.env` file exists in project root
- Verify the file contains `HUMIO_TOKEN=your_token`
- Restart the application after creating/modifying `.env`

**"No events found" Warning**
- Verify the correlation ID is correct
- Check repository access permissions
- Ensure time range includes the events

**Graphviz Errors**
- Install Graphviz system package
- Verify with `dot -V` in terminal
- Restart application after installation

**Port Already in Use**
- Web interface: Change from 8501 to another port
- Jupyter: Change from 8888 to another port
- Update `docker-compose.yml` or use different port flags

### Docker Issues

**Container won't start:**
```bash
docker-compose logs web      # Check web interface logs
docker-compose logs jupyter  # Check Jupyter logs
docker-compose down          # Stop all containers
docker-compose up --build    # Rebuild and restart
```

**Permission issues:**
```bash
sudo chown -R $(id -u):$(id -g) .
```

## Development

### Running Tests

Tests have been removed in the latest version. For development:

```bash
# Install dependencies
pip install -r requirements.txt

# Run web interface in development mode
streamlit run app.py

# Or use Jupyter for experimentation
jupyter notebook
```

### Adding Custom Themes

Create a new theme file in `log_to_graph/flowchart/theme/`:

```python
from .theme import Theme, GraphStyle, NodeStyle, EdgeStyle

MY_THEME = Theme(
    graph=GraphStyle(bgcolor="#000000", fontcolor="#FFFFFF"),
    node=NodeStyle(fillcolor="#333333", fontcolor="#FFFFFF"),
    edge=EdgeStyle(color="#666666"),
    # ... configure other styles
)
```

Register it in `log_to_graph/flowchart/theme/__init__.py`.

### Extending Node Types

Add custom node handlers in `log_to_graph/flowchart/node/` and update the factory in `node_factory.py`.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Use Cases

- **Debugging Distributed Systems**: Trace requests across microservices
- **Performance Analysis**: Visualize event timing and bottlenecks
- **Documentation**: Generate diagrams for technical documentation
- **Incident Response**: Quickly understand error flows
- **System Monitoring**: Analyze production event patterns

## License

This project is licensed under the MIT License.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Uses [Graphviz](https://graphviz.org/) for flowchart rendering
- Integrates with [Humio](https://www.humio.com/) for log management
- Powered by [HumioLib](https://github.com/humio/python-humio) Python client

## Support

For issues, questions, or feature requests:
1. Check the [troubleshooting section](#troubleshooting)
2. Review the detailed setup guides
3. Open an issue on GitHub

## Quick Reference

### Ports
- **8501** - Web Interface (Streamlit)
- **8888** - Jupyter Notebook

### URLs
- Web Interface: `http://localhost:8501`
- Jupyter Notebook: `http://localhost:8888`

### Scripts
- `./start-docker.sh` - Start Docker containers
- `./stop-docker.sh` - Stop Docker containers
- `./run_web.sh` - Run web interface (native)

### Commands
```bash
# Docker
docker-compose up -d web          # Start web interface
docker-compose up -d jupyter      # Start Jupyter
docker-compose up -d              # Start both
docker-compose down               # Stop all containers
docker-compose logs -f web        # View web logs

# Native
streamlit run app.py              # Start web interface
jupyter notebook                  # Start Jupyter
pip install -r requirements.txt   # Install dependencies
```

---

**Made with ❤️ for better log analysis**
