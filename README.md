# one-file-django

For quick prototypes in Django.

Run the dev server:

```bash
DJANGO_DEBUG=1 DJANGO_SECRET_KEY=asdf1234 python app/django_main.py runserver
```

Run under uWSGI:

```bash
uwsgi --http :8000 -M --pythonpath=. --env DJANGO_SECRET_KEY=asdf1234 -w "app.django_main:application"
```
