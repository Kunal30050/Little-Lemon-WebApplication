Little Lemon Web Application - Backend Capstone Project

API Endpoints:
/api/registration/
/api/token/
/api/menu/
/api/menu/<id>/
/api/bookings/
/api/bookings/<id>/

Setup Instructions:
1. Install dependencies:
   pip install django djangorestframework mysqlclient

2. Update DATABASES in littlelemon/settings.py with your MySQL credentials:
   NAME: littlelemon
   USER: root
   PASSWORD: your_password

3. Create the MySQL database:
   CREATE DATABASE littlelemon;

4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Create superuser:
   python manage.py createsuperuser

6. Run the server:
   python manage.py runserver

7. Run tests:
   python manage.py test restaurant

Testing with Insomnia:
- POST /api/registration/ with {"username","email","password"} to register
- POST /api/token/ with {"username","password"} to get token
- Add header: Authorization: Token <your_token>
- Test all menu and booking endpoints
