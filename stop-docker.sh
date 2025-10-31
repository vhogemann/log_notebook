#!/bin/bash

# LogNotebook Docker Stop Script

set -e

echo "🛑 Stopping LogNotebook Docker Setup"
echo "===================================="

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed."
    exit 1
fi

# Check if docker-compose.yml exists
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ docker-compose.yml not found in current directory."
    exit 1
fi

echo "🔍 Checking container status..."
WEB_RUNNING=$(docker-compose ps | grep -c "lognotebook-web" || true)
JUPYTER_RUNNING=$(docker-compose ps | grep -c "lognotebook-jupyter" || true)

if [ "$WEB_RUNNING" -gt 0 ] || [ "$JUPYTER_RUNNING" -gt 0 ]; then
    echo "📦 Found running LogNotebook container(s):"
    [ "$WEB_RUNNING" -gt 0 ] && echo "   - Web Interface (lognotebook-web)"
    [ "$JUPYTER_RUNNING" -gt 0 ] && echo "   - Jupyter Notebook (lognotebook-jupyter)"
    echo ""

    echo "🛑 Stopping and removing containers..."
    docker-compose down

    echo "✅ LogNotebook containers have been stopped and removed."
    echo ""
    echo "📋 Container cleanup complete!"
    echo "   To start again, run: ./start-docker.sh"
else
    echo "ℹ️  No running LogNotebook containers found."
    echo "   If you want to remove any stopped containers, run: docker-compose down"
fi

echo ""
echo "🧹 Optional cleanup commands:"
echo "   Remove images:       docker-compose down --rmi all"
echo "   Remove volumes:      docker-compose down --volumes"
echo "   Full cleanup:        docker-compose down --rmi all --volumes --remove-orphans"
