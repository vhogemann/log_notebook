# LogNotebook Docker Setup

This project can be run in a Docker container that serves the Jupyter notebook in a browser interface.

## Prerequisites

1. Docker and Docker Compose installed on your system
2. Your Humio token

## Setup Instructions

### 1. Environment Variables

Copy the example environment file and add your Humio token:

```bash
cp example.env .env
```

Then edit `.env` and replace `your_humio_token_here` with your actual Humio token:

```
HUMIO_TOKEN=your_actual_humio_token_here
```

### 2. Build and Run with Docker Compose (Recommended)

```bash
# Build and start the container
docker-compose up --build

# Or run in detached mode (background)
docker-compose up -d --build
```

### 3. Alternative: Build and Run with Docker directly

```bash
# Build the image
docker build -t lognotebook .

# Run the container
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work --env-file .env lognotebook
```

## Accessing the Notebook

Once the container is running, open your web browser and navigate to:

```
http://localhost:8888
```

You should see the Jupyter Lab interface with your `LogToGraph.ipynb` notebook ready to use.

## Features

- **Jupyter Lab Interface**: Modern web-based interface for running notebooks
- **All Dependencies Included**: Python packages, Graphviz, and system dependencies are pre-installed
- **Persistent Storage**: Your changes and output files are preserved
- **Environment Variables**: Humio token is automatically loaded from your `.env` file
- **Hot Reload**: Changes to your code are immediately reflected (volume mounted)

## Stopping the Container

```bash
# If running with docker-compose
docker-compose down

# If running with docker directly
docker stop <container_name>
```

## Troubleshooting

1. **Port 8888 already in use**: Change the port mapping in `docker-compose.yml` from `8888:8888` to something like `8889:8888`, then access via `http://localhost:8889`

2. **Permission issues**: The container runs as the `jovyan` user. If you encounter permission issues with mounted volumes, you may need to adjust file permissions:
   ```bash
   sudo chown -R 1000:100 .
   ```

3. **Missing Humio token**: Make sure your `.env` file exists and contains the correct `HUMIO_TOKEN` value.

## Development

The container automatically mounts your local directory, so any changes you make to the notebook or Python files will be immediately available in the container. The `output/` directory is also mounted to preserve generated graphs and files.
