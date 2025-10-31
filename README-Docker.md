# LogNotebook Docker Setup

This project can be run in Docker containers with two interface options:
- **Web Interface** (Streamlit) - Modern, user-friendly web UI
- **Jupyter Notebook** - Classic notebook interface for development

## Prerequisites

1. Docker and Docker Compose installed on your system
2. Your Humio token

## Quick Start

### Using the Start Script (Recommended)

The easiest way to get started:

```bash
./start-docker.sh
```

This script will:
1. Check for required dependencies
2. Create `.env` file if needed
3. Prompt you to select which interface to run:
   - **Web Interface** (Streamlit) - Recommended for end users
   - **Jupyter Notebook** - For development and experimentation
   - **Both** - Run both interfaces simultaneously
4. Build and start the selected container(s)
5. Automatically open the interface(s) in your browser

## Manual Setup

### 1. Environment Variables

Copy the example environment file and add your Humio token:

```bash
cp example.env .env
```

Then edit `.env` and replace `your_humio_token_here` with your actual Humio token:

```
HUMIO_TOKEN=your_actual_humio_token_here
```

### 2. Build and Run with Docker Compose

**Run Web Interface Only:**
```bash
docker-compose up --build web
```

**Run Jupyter Notebook Only:**
```bash
docker-compose up --build jupyter
```

**Run Both Interfaces:**
```bash
docker-compose up --build
```

**Run in Background (Detached):**
```bash
docker-compose up -d --build
```

### 3. Alternative: Build and Run with Docker Directly

**Web Interface:**
```bash
# Build the image
docker build -f Dockerfile.web -t lognotebook-web .

# Run the container
docker run -p 8501:8501 -v $(pwd):/app --env-file .env lognotebook-web
```

**Jupyter Notebook:**
```bash
# Build the image
docker build -t lognotebook-jupyter .

# Run the container
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work --env-file .env lognotebook-jupyter
```

## Accessing the Interfaces

Once the containers are running:

**Web Interface (Streamlit):**
```
http://localhost:8501
```

**Jupyter Notebook:**
```
http://localhost:8888
```

## Features

### Web Interface (Streamlit)
- **User-Friendly UI**: Clean, intuitive interface for non-technical users
- **Interactive Controls**: Pan, zoom, and explore flowcharts with mouse/keyboard
- **Theme Selection**: Choose from 11 visual themes
- **Download SVG**: Save flowcharts for documentation
- **Real-time Queries**: Direct Humio API integration

### Jupyter Notebook
- **Development Environment**: Full Python notebook for experimentation
- **Code Access**: Modify and extend functionality
- **Interactive Outputs**: View results inline
- **Research & Analysis**: Advanced data exploration

### Both Interfaces
- **All Dependencies Included**: Python packages, Graphviz, and system dependencies pre-installed
- **Persistent Storage**: Changes and output files are preserved
- **Environment Variables**: Humio token automatically loaded from `.env` file
- **Hot Reload**: Code changes immediately reflected (volume mounted)
- **Isolated Environments**: Each interface runs in its own container

## Container Management

### Viewing Logs

**Web Interface:**
```bash
docker-compose logs -f web
```

**Jupyter Notebook:**
```bash
docker-compose logs -f jupyter
```

**Both:**
```bash
docker-compose logs -f
```

### Stopping Containers

**Stop all:**
```bash
docker-compose down
```

**Stop specific service:**
```bash
docker-compose stop web
# or
docker-compose stop jupyter
```

**Stop and remove volumes:**
```bash
docker-compose down --volumes
```

### Restarting Containers

```bash
# Restart all
docker-compose restart

# Restart specific service
docker-compose restart web
docker-compose restart jupyter
```

### Shell Access

**Web Interface:**
```bash
docker-compose exec web bash
```

**Jupyter Notebook:**
```bash
docker-compose exec jupyter bash
```

## Troubleshooting

### Port Conflicts

**Port 8501 (Web Interface) already in use:**
Edit `docker-compose.yml` and change:
```yaml
ports:
  - "8502:8501"  # Use port 8502 instead
```
Then access via `http://localhost:8502`

**Port 8888 (Jupyter) already in use:**
Edit `docker-compose.yml` and change:
```yaml
ports:
  - "8889:8888"  # Use port 8889 instead
```
Then access via `http://localhost:8889`

### Permission Issues

If you encounter permission errors with mounted volumes:

**For Web Interface:**
```bash
sudo chown -R $(id -u):$(id -g) .
```

**For Jupyter Notebook:**
```bash
sudo chown -R 1000:100 .
```

### Missing Humio Token

Make sure your `.env` file exists and contains:
```
HUMIO_TOKEN=your_actual_humio_token_here
```

Restart containers after updating:
```bash
docker-compose restart
```

### Container Won't Start

Check logs for errors:
```bash
docker-compose logs web
docker-compose logs jupyter
```

Rebuild containers:
```bash
docker-compose down
docker-compose up --build
```

### Streamlit Health Check Failing

The web container includes a health check. If it fails:
```bash
# Check container status
docker-compose ps

# View detailed logs
docker-compose logs web

# Manually test health endpoint
curl http://localhost:8501/_stcore/health
```

## Development

The containers automatically mount your local directory:

**Web Interface:**
- Local directory mounted at `/app`
- Changes to `app.py` or `web/` trigger auto-reload
- Output files saved to `./output/`

**Jupyter Notebook:**
- Local directory mounted at `/home/jovyan/work`
- Changes to notebooks or Python files immediately available
- Output files saved to `./output/`

## Comparison

| Feature | Web Interface | Jupyter Notebook |
|---------|---------------|------------------|
| User Experience | Simple, guided UI | Code-based, technical |
| Setup Time | Instant | Requires notebook knowledge |
| Customization | Limited to UI options | Full Python code access |
| Best For | End users, demos, production | Development, research |
| Port | 8501 | 8888 |
| Auto-reload | Yes (Streamlit) | Manual refresh |

## Advanced Usage

### Running Specific Services

**Development workflow (both interfaces):**
```bash
docker-compose up -d
```

**Production deployment (web only):**
```bash
docker-compose up -d web
```

**Research work (Jupyter only):**
```bash
docker-compose up -d jupyter
```

### Custom Configuration

**Streamlit Configuration:**
Create `.streamlit/config.toml` in project root for custom Streamlit settings.

**Jupyter Configuration:**
Modify the `command` section in `docker-compose.yml` for Jupyter options.

### Resource Limits

Add resource limits in `docker-compose.yml`:
```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
```
