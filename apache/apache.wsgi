import os 
import sys 
 
path = '/home/djangoProject' 
if path not in sys.path: 
    sys.path.insert(0, '/home/djangoProject/web_msqli') 
    sys.path.append('/home/djangoProject/web_msqli/') 
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 
 
import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()
