import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HW_WATER_2_0.settings')

application = get_asgi_application()