#!/bin/bash
# Deployment script for Artist Sculpture Cost Prediction

echo "🚀 Deploying Artist Sculpture Cost Prediction Application..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Check Django configuration
echo "🔍 Checking Django configuration..."
python manage.py check

echo "✅ Deployment completed successfully!"
echo ""
echo "🌐 To start the application:"
echo "   source venv/bin/activate"
echo "   python manage.py runserver 0.0.0.0:8000"
echo ""
echo "🐳 For Docker deployment:"
echo "   docker build -t artist-sculpture-prediction ."
echo "   docker run -p 8000:8000 artist-sculpture-prediction"
