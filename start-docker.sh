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

echo "🔨 Building Docker image..."
docker-compose build

echo "🚀 Starting LogNotebook container..."
docker-compose up -d

echo "✅ LogNotebook is now running!"
echo ""
echo "🌐 Opening LogToGraph notebook in your default browser..."
echo "   URL: http://localhost:8888/notebooks/LogToGraph.ipynb"

# Wait a moment for the container to fully start
sleep 3

# Open the notebook directly in the default macOS browser
open "http://localhost:8888/notebooks/LogToGraph.ipynb"
echo ""
echo "📋 Useful commands:"
echo "   View logs:           docker-compose logs -f"
echo "   Stop container:      docker-compose down"
echo "   Restart container:   docker-compose restart"
echo "   Shell into container: docker-compose exec lognotebook bash"
echo ""
echo "📁 Your notebook and files are mounted from the current directory."
echo "   Any changes you make will be preserved."
