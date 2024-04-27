# Performance Analyzer

Performance Analyzer is a web application that uses Django for the backend and React.js for the frontend. This project facilitates the analysis and visualization of performance data, allowing users to monitor various performance metrics.

## Setup Guide for Windows PowerShell

Follow these steps to set up the project on your Windows machine using PowerShell.

### Prerequisites

- Python (preferably Python 3)
- Node.js and npm (for React.js)

### Creating a Python Virtual Environment

1. **Navigate to the virtual environment:**
   ```bash
   # Navigate to your project directory
   cd C:\path\to\your\project

   # Navigate to the virtual environment named 'venv'
   cd venv
   ```

2. **Activate the virtual environment:**
   ```bash
   # Activate the virtual environment
   Scripts\activate.ps1
   
   # Or
   Scripts\activate.bat
   ```

### Installing Django

1. **Install Django within the virtual environment:**
   ```bash
   # Make sure the virtual environment is activated
   pip install django
   ```

### Installing Yarn (for React.js)

1. **Install Chocolatey (if not already installed):**
   - Follow the installation guide from [Chocolatey's official website](https://chocolatey.org/install).

2. **Install Node.js and Yarn using Chocolatey:**
   ```bash
   # Install Node.js and Yarn via Chocolatey
   choco install nodejs
   choco install yarn
   ```

3. **Navigate to the frontend directory within your project:**
   ```bash
   # Change to the frontend directory
   cd C:\path\to\your\project\frontend
   ```

4. **Install project dependencies using Yarn:**
   ```bash
   # Install dependencies using Yarn
   yarn install
   ```

### Running the Application

1. **Run Django Server:**
   ```bash
   # Make sure the virtual environment is activated
   # Navigate to the backend directory within your project
   cd C:\path\to\your\project\backend

   # Run Django development server
   python manage.py runserver
   ```

2. **Run React Development Server:**
   ```bash
   # Navigate to the frontend directory within your project
   cd C:\path\to\your\project\frontend

   # Start the React development server
   yarn start
   ```

Once both the Django server and React development server are running, you should be able to access the application at `http://localhost:3000` in your web browser.

Feel free to modify and extend this project for your specific performance analysis needs!

---

This README provides a basic guide to setting up and running the "Performance Analyzer" project on Windows using PowerShell. For more detailed instructions or troubleshooting, refer to Django's and React's official documentation.
