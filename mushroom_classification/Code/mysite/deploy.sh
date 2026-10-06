#!/bin/bash
# Deployment script for Mushroom Classification App

echo "🍄 Mushroom Classification App Deployment"
echo "======================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running migrations..."
python manage.py migrate

# Check Django setup
echo "🔍 Checking Django setup..."
python manage.py check

echo "✅ Deployment complete!"
echo "🚀 Start the server with: python manage.py runserver"
