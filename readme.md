# Client Management Application

This is a Django-based application for managing clients.

## Features

- Login functionality
- Client creation form
- Client listing with pagination
- Search functionality

## Installation

` Please Create Virtual Environment and install all the dependencies inside virtualenv`

1. Clone the repository: `git clone https://github.com/your-username/client-management.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the database settings in `client_management/settings.py`
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Usage

- Access the login page: `/login`
- Create a new client: `/create-client`
- View the client listing: `/client-listing`

## Dependencies

- Django: A high-level Python web framework - [Django Documentation](https://docs.djangoproject.com/)
- django-pagination: Simple Django pagination - [django-pagination on PyPI](https://pypi.org/project/django-pagination/)

## Notes

- Pagination is implemented using the `django.core.paginator` module.
- Search functionality filters clients based on the name field using `icontains` lookup.
- Bootstrap is used for styling the templates.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
