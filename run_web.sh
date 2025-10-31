#!/bin/bash
# LogNotebook Web Interface Startup Script

echo "Starting LogNotebook Web Interface..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "   Please create .env file with your HUMIO_TOKEN"
    echo "   Example: cp example.env .env"
    echo ""
fi

# Check if streamlit is installed
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "📦 Streamlit not found. Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

# Run the Streamlit app
echo "🚀 Starting Streamlit application..."
echo "   The web interface will open in your browser"
echo ""
streamlit run app.py
