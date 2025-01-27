# Clinic Management System

## Project Overview

This is a backend implementation of a Clinic Management System, built using Django. The system is designed to streamline and automate clinic operations, including appointment scheduling, patient record management, doctor and staff management, inventory and billing management, surgeries and consultations, and analytics.

## Project Structure

```plaintext
Clinic_MS/
├── backend/                # Django backend implementation
```

---

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 4.x
- SQLite

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend/backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Testing

### Account Creation and Login

When new patients or staff members are added to the system, accounts are automatically created for them with the following default credentials:

- Username: Email address provided during registration
- Default password: 12345678

> Note: Users can change their passwords through their dashboard after their first login for security purposes.

### Backend Testing

Run the test suite using:

```bash
python manage.py test
```

---
