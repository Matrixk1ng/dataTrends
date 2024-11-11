# DataTrends Project

This project consists of a **Next.js** frontend that interacts with a **Flask** backend to display data fetched from a database. The backend is powered by Flask with SQLAlchemy and serves data via a RESTful API. The frontend uses React and Next.js to display this data.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Frontend Setup (Next.js)](#frontend-setup-nextjs)
4. [Backend Setup (Flask)](#backend-setup-flask)
5. [Running the Application](#running-the-application)
6. [API Endpoints](#api-endpoints)
7. [Technologies Used](#technologies-used)
8. [Troubleshooting](#troubleshooting)

---


---

## Getting Started

### Prerequisites

Make sure you have the following installed:
- **Python 3.x** (for Flask backend)
- **Node.js** (for Next.js frontend)
- **npm** or **yarn** (for managing frontend dependencies)

### Install Dependencies

1. **Backend (Flask)**: create a Python virtual environment:

   ```bash
  
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  pip install flask flask-cors sqlalchemy pandas
2. Frontend
  Frontend (Next.js): Navigate to the frontend folder and install the necessary npm packages:

  cd frontend
  npm install
3. Backend Setup (Flask)
  Database Setup: The backend uses an SQLite database. You can initialize the database with the following command:
  python init_db.py
  
  Run the Backend: In the backend directory, run:
  python app.py
4. Technologies Used
  Frontend:
  
  Next.js
  React
  TypeScript
  Axios (or Fetch)
  Backend:
  
  Flask
  SQLAlchemy (ORM for database interaction)
  Pandas (for data processing)
  SQLite (database)
  Development Tools:
  
  VS Code (for development)
  Postman (for testing API requests)

