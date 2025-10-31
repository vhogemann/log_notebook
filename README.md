# LogNotebook

Query Humio logs and visualize event flows as interactive flowcharts. Track distributed system events by correlation ID and generate visual diagrams with customizable themes.

![Language](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Humio Integration** - Direct API queries by correlation ID
- **Interactive Flowcharts** - Pan/zoom controls for exploring event flows
- **11 Visual Themes** - Light, Matrix, Vaporwave, Cyberpunk, and more
- **Multiple Interfaces** - Web UI (Streamlit), Jupyter notebooks, or VS Code
- **Docker Support** - Containerized deployment with Docker Compose
- **SVG Export** - Download flowcharts for documentation

## Quick Start

```bash
# Clone and setup
git clone https://github.com/vhogemann/log_notebook.git
cd log_notebook
cp example.env .env
# Edit .env and add your HUMIO_TOKEN

# Run with Docker (recommended)
./start-docker.sh

# Or run web interface natively
pip install -r requirements.txt
brew install graphviz  # macOS
streamlit run app.py
```

## Setup Guides

- **[Docker Setup](README-Docker.md)** - Run with Docker Compose (recommended)
- **[Web Interface](README-Web.md)** - Streamlit web UI setup and usage
- **[VS Code Setup](README-VSCode.md)** - Run Jupyter notebooks in VS Code

## Quick Reference

### Ports
- **8501** - Web Interface (Streamlit)
- **8888** - Jupyter Notebook

### URLs
- Web Interface: `http://localhost:8501`
- Jupyter Notebook: `http://localhost:8888`

### Scripts
- `./start-docker.sh` - Start Docker containers (interactive menu)
- `./stop-docker.sh` - Stop Docker containers
- `./run_web.sh` - Run web interface (native)

### Commands
```bash
# Docker
docker-compose up -d web          # Start web interface only
docker-compose up -d jupyter      # Start Jupyter only
docker-compose up -d              # Start both
docker-compose down               # Stop all containers
docker-compose logs -f web        # View web logs

# Native
streamlit run app.py              # Start web interface
jupyter notebook                  # Start Jupyter
pip install -r requirements.txt   # Install dependencies
```

### Configuration

Create `.env` file with your Humio token:
```
HUMIO_TOKEN=your_actual_humio_token_here
```

## License

MIT License

---

**Made with ❤️ for better log analysis**
