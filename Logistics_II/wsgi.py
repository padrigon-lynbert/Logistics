"""
WSGI config for Logistics_II project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Logistics_II.settings')
try:
 application = get_wsgi_application()
except Exception as e:
 import traceback
 traceback.print_exc()
 raise e