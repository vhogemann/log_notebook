# Use the official Jupyter base notebook image
FROM quay.io/jupyter/base-notebook:latest

# Set the working directory
WORKDIR /home/jovyan/work

# Switch to root to install system dependencies
USER root

# Install system dependencies for Graphviz
RUN apt-get update && apt-get install -y \
    graphviz \
    graphviz-dev \
    && rm -rf /var/lib/apt/lists/*

# Switch back to jovyan user
USER jovyan

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional Jupyter dependencies that might be needed
RUN pip install --no-cache-dir \
    jupyter \
    jupyterlab \
    notebook \
    ipywidgets \
    ollama

# Copy the entire project
COPY --chown=jovyan:users . .

# Create output directory if it doesn't exist
RUN mkdir -p output

# Expose the Jupyter port
EXPOSE 8888

# Set environment variables
ENV JUPYTER_ENABLE_LAB=yes

# Start Jupyter Lab
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.allow_root=True", "--ip=0.0.0.0", "--port=8888"]
