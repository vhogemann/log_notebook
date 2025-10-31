#!/bin/bash

# LogNotebook Docker Quick Start Script

set -e

echo "🐳 LogNotebook Docker Setup"
echo "=========================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from example..."
    cp example.env .env
    echo "⚠️  Please edit .env file and add your HUMIO_TOKEN before continuing."
    echo "   Current content:"
    cat .env
    echo ""
    read -p "Have you updated the .env file with your Humio token? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Please update the .env file and run this script again."
        exit 1
    fi
fi

# Prompt user to select which interface to start
echo ""
echo "Which interface would you like to start?"
echo "  1) Web Interface (Streamlit - Recommended)"
echo "  2) Jupyter Notebook (Classic)"
echo "  3) Both"
echo ""
read -p "Enter your choice (1/2/3): " -n 1 -r
echo ""

case $REPLY in
    1)
        SERVICES="web"
        SERVICE_NAME="Streamlit Web Interface"
        URL="http://localhost:8501"
        ;;
    2)
        SERVICES="jupyter"
        SERVICE_NAME="Jupyter Notebook"
        URL="http://localhost:8888/notebooks/LogToGraph.ipynb"
        ;;
    3)
        SERVICES=""
        SERVICE_NAME="Both Interfaces"
        URL_WEB="http://localhost:8501"
        URL_JUPYTER="http://localhost:8888"
        ;;
    *)
        echo "Invalid choice. Defaulting to Web Interface."
        SERVICES="web"
        SERVICE_NAME="Streamlit Web Interface"
        URL="http://localhost:8501"
        ;;
esac

echo "🔨 Building Docker image(s)..."
if [ -z "$SERVICES" ]; then
    docker-compose build
else
    docker-compose build $SERVICES
fi

echo "🚀 Starting $SERVICE_NAME..."
if [ -z "$SERVICES" ]; then
    docker-compose up -d
else
    docker-compose up -d $SERVICES
fi

echo "✅ LogNotebook is now running!"
echo ""

# Wait a moment for the container(s) to fully start
sleep 3

# Open in browser based on selection
if [ "$REPLY" = "3" ]; then
    echo "🌐 Opening interfaces in your default browser..."
    echo "   Web Interface: $URL_WEB"
    echo "   Jupyter Notebook: $URL_JUPYTER"
    open "$URL_WEB"
    sleep 1
    open "$URL_JUPYTER"
elif [ -n "$URL" ]; then
    echo "🌐 Opening $SERVICE_NAME in your default browser..."
    echo "   URL: $URL"
    open "$URL"
fi

echo ""
echo "📋 Useful commands:"
echo "   View logs:              docker-compose logs -f"
echo "   Stop containers:        docker-compose down"
echo "   Restart containers:     docker-compose restart"
echo "   Shell into web:         docker-compose exec web bash"
echo "   Shell into jupyter:     docker-compose exec jupyter bash"
echo ""
echo "🌐 Access URLs:"
echo "   Web Interface:          http://localhost:8501"
echo "   Jupyter Notebook:       http://localhost:8888"
echo ""
echo "📁 Your files are mounted from the current directory."
echo "   Any changes you make will be preserved."
