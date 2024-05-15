# DRF API for posts
Included:
- Authorization
- Throttling
- Schema .yml
- Pagination
- Permissions

## Installation
```
pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Go to `/api/v1/` to get posts

Ensure that you added superuser to add posts and then view them.
