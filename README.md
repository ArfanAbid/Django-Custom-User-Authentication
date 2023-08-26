# Django-Custom-User-Authentication

This repository contains an example implementation of custom user authentication with email-based login using Django. It demonstrates how to create a custom user model, implement authentication views, and handle user registration and login.

## Features

- Custom user model with email-based authentication
- Registration view for user sign-up
- Login view for user authentication
- Logout view to end user sessions
- Access control to certain views using the `@login_required` decorator
- Integration with Django's `messages` framework for user feedback

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/ArfanAbid/Django-Custom-User-Authentication.git

2. Navigate to project directory:
    `cd core`
   
3. Create and activate Virtual Environment:
   `python -m venv venv` then
   `.\venv\Scripts\activate`

4. Run Data base migrations:
   `python manage.py migrate`

5. Create a superuser (admin account) to access the Django admin panel:
   `python manage.py createsuperuser`

6. Run the development server:
   `python manage.py runserver`

 7. Access the development server at  `http://127.0.0.1:8000/`



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
         



