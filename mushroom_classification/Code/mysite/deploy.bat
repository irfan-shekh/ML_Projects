@echo off
REM Deployment script for Mushroom Classification App (Windows)

echo 🍄 Mushroom Classification App Deployment
echo ======================================

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Collect static files
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

REM Run migrations
echo 🗄️ Running migrations...
python manage.py migrate

REM Check Django setup
echo 🔍 Checking Django setup...
python manage.py check

echo ✅ Deployment complete!
echo 🚀 Start the server with: python manage.py runserver
pause
