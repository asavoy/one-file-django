import os
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpRequest, HttpResponse
from django.urls import path


settings.configure(
    DEBUG=(os.environ.get("DJANGO_DEBUG", "") == "1"),
    ALLOWED_HOSTS=["*"],
    ROOT_URLCONF=__name__,
    SECRET_KEY=os.environ["DJANGO_SECRET_KEY"],
)


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello world!", status=200)


urlpatterns = [
    path("", index),
]


application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

