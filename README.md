# Shree Tours and Travel

A comprehensive Travel and Tourism website built with Django framework, providing an all-in-one platform for tour planning, bus booking, flight booking, and data visualization with advanced algorithms.

## 📋 Table of Contents
- Features
- Importance
- Project Modules
- Prerequisites
- Installation & Setup
- Running the Application
- Usage
- References
- License
- Author

## ✨ Features

- **Tours Module**: Browse, create, and customize tour packages
- **Bus Booking**: Search and book bus tickets with real-time seat availability
- **Flight Booking**: Book flights with multiple seating options
- **Smart Tour Planning**: AI-powered tour planning using Fractional Knapsack Algorithm
- **Route Optimization**: Shortest path calculation using Travelling Salesman Problem (TSP)
- **Data Visualization**: Interactive charts showing tourism trends and seasonality
- **User Authentication**: Secure login and profile management
- **Payment Integration**: Seamless payment processing

## 🎯 Importance

This application demonstrates a real-world enterprise travel management system with practical applications of:
- **Advanced Algorithms**: Implementation of Fractional Knapsack and TSP for optimal tour planning
- **Full-Stack Development**: Complete Django-based web application
- **Database Design**: Complex relational database for travel operations
- **Data Visualization**: Business intelligence using Chart.js
- **Security**: Environment-based configuration management for sensitive data
- **Scalability**: Cloud-ready architecture (Heroku compatible)

## 📦 Project Modules

### 1. **Tours Module**
Browse all available tour packages or create custom tour plans. Users can filter by budget and time constraints to find the perfect itinerary.

### 2. **Bus Booking Module**
- View available buses and schedules
- Search by source, destination, and date
- Real-time seat availability
- Book tickets with confirmation

### 3. **Flight Booking Module**
- Browse available flights
- Filter by route and date
- Select seat class and quantity
- Secure booking process

### 4. **Mathematical Programming Module**
- **Fractional Knapsack Algorithm**: Optimize tour packages within budget/time constraints
- **TSP Algorithm**: Calculate shortest path covering all tourist destinations

### 5. **Data Science Module**
- Pie charts showing tourist place popularity
- Seasonal travel trends visualization
- Interactive dashboard with Chart.js

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- MySQL Server (local or remote)
- pip (Python package manager)
- git

## 🚀 Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/CodingEnthusiastic/SRS-Tours-and-Travels.git
cd Travel-And-Tourism
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your configuration
```

Edit `.env` file with your database and Django settings:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=
DB_NAME=
DB_USER=root
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

### Step 5: Setup MySQL Database
```bash
# Create a new database
mysql -u root -p
CREATE DATABASE demodreamtour CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### Step 6: Run Migrations
```bash
python manage.py migrate
```

### Step 7: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

---

## ▶️ Running the Application

### Start the Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### Access Admin Panel
```
http://127.0.0.1:8000/admin/
```
Log in with your superuser credentials.

### Troubleshooting
- **ModuleNotFoundError**: Ensure virtual environment is activated
- **Database Connection Error**: Check MySQL is running and .env credentials are correct
- **Port 8000 already in use**: `python manage.py runserver 8001`

---

## 📖 Usage

1. **Create Account**: Sign up on the homepage
2. **Browse Tours**: View available tour packages
3. **Book Transport**: Book buses or flights
4. **Create Custom Tour**: Plan your own tour within budget/time constraints
5. **View Dashboard**: Check bookings and visualize travel data
6. **Admin Panel**: Manage packages, bookings, and user data

---

## 🔗 References & Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **MySQL Documentation**: https://dev.mysql.com/doc/

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright © 2026 CodingEnthusiastic. All rights reserved.

---

## 👤 Author

**CodingEnthusiastic**
- GitHub: [@CodingEnthusiastic](https://github.com/CodingEnthusiastic)
- Repository: [SRS-Tours-and-Travels](https://github.com/CodingEnthusiastic/SRS-Tours-and-Travels)
