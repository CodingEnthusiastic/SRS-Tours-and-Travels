# Local Setup Guide - Shree Tours and Travel

Complete step-by-step guide to run the application on your local machine.

## Prerequisites ✅

### Windows
- **Python 3.8+** - Download from [python.org](https://www.python.org/downloads/)
- **MySQL 8.0+** - Download from [mysql.com](https://dev.mysql.com/downloads/mysql/)
- **Git** - Download from [git-scm.com](https://git-scm.com/download/win)
- **Text Editor/IDE** - VS Code, PyCharm, or similar

### macOS
```bash
# Install Homebrew first if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.10

# Install MySQL
brew install mysql

# Install Git
brew install git
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3.10 python3-pip mysql-server git
```

---

## Step 1: Clone the Repository

### Via HTTPS
```bash
git clone https://github.com/CodingEnthusiastic/SRS-Tours-and-Travels.git
cd Travel-And-Tourism
```

### Via SSH (if configured)
```bash
git clone git@github.com:CodingEnthusiastic/SRS-Tours-and-Travel.git
cd Travel-And-Tourism
```

---

## Step 2: Create and Activate Virtual Environment

### Windows
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

**You should see `(venv)` at the beginning of your terminal prompt.**

---

## Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

**Dependencies installed:**
- Django 4.0
- mysqlclient 2.1.0
- numpy & pandas for data processing
- Chart.js for visualizations
- And 30+ more packages

---

## Step 4: Setup MySQL Database

### Start MySQL Service

**Windows:**
```bash
# MySQL should auto-start, or use:
net start MySQL80
```

**macOS:**
```bash
# If installed via Homebrew
brew services start mysql
# Or manually
mysql.server start
```

**Linux:**
```bash
sudo systemctl start mysql
```

### Create Database

```bash
# Login to MySQL
mysql -u root -p

# Enter password when prompted (default: no password on local)

# Run these SQL commands:
CREATE DATABASE demodreamtour CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW DATABASES;
EXIT;
```

---

## Step 5: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` file (open with any text editor) and update:

```env
# Django Configuration
SECRET_KEY=your-unique-secret-key-here
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Configuration
DB_ENGINE=
DB_NAME=
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

**Generate a new SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Step 6: Run Database Migrations

```bash
# Apply all migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

---

## Step 7: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts:
```
Username: admin
Email: admin@example.com
Password: (enter secure password)
Password (again): (confirm)
```

---

## Step 8: Collect Static Files (Optional for Development)

```bash
python manage.py collectstatic --noinput
```

---

## Step 9: Run the Development Server

```bash
python manage.py runserver
```

**Output should show:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

## Access the Application

- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
  - Login with your superuser credentials

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'django'`
**Solution:** Ensure virtual environment is activated
```bash
# Check if (venv) appears in terminal
# If not, activate it:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### Issue: `Can't connect to MySQL server`
**Solution:** Check MySQL connection details
```bash
# Test MySQL connection
mysql -u root -p demodreamtour

# If connection fails:
# 1. Verify MySQL is running
# 2. Check username/password in .env
# 3. Verify DB_HOST is correct (127.0.0.1 or localhost)
```

### Issue: `Port 8000 is already in use`
**Solution:** Use a different port
```bash
python manage.py runserver 8001
# Now access at http://127.0.0.1:8001/
```

### Issue: `No such table` errors after running server
**Solution:** Run migrations again
```bash
python manage.py migrate
```

### Issue: `.env` file not being read
**Solution:** Ensure `.env` is in the project root and restart server
```bash
# Check .env location
ls -la .env  # macOS/Linux
dir .env    # Windows

# Restart server
# Ctrl+C to stop, then:
python manage.py runserver
```

---

## Development Tips

### Run Tests
```bash
python manage.py test
```

### Create App Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Shell Access (Interactive Python)
```bash
python manage.py shell
>>> from sample.models import User
>>> User.objects.all()
```

### View Database Queries (Development)
```bash
# In Django shell
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as context:
    # Run query
    pass
print(context.captured_queries)
```

---

## Deactivate Virtual Environment

When done with development:
```bash
deactivate
```

---

## Project Structure

```
Travel-And-Tourism/
├── sample/                 # Main Django app
│   ├── migrations/        # Database migrations
│   ├── static/            # CSS, JS, Images
│   ├── templates/         # HTML templates
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   └── settings.py        # Django settings
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (local)
├── .env.example          # Environment variables template
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

---

## Next Steps

1. ✅ Application is running locally
2. Create sample data in admin panel
3. Test different modules (Tours, Bus, Flight)
4. Explore the code and customize as needed
5. Deploy to production (Heroku/AWS)

---

## Support & Resources

- **Django Docs**: https://docs.djangoproject.com/
- **MySQL Docs**: https://dev.mysql.com/doc/
- **GitHub Issues**: Report issues on repository
- **GitHub Discussions**: Ask questions and get help

---

**Happy Coding! 🚀**
