from __future__ import unicode_literals

import sys
import os
import site

#sys.path.append('/home/sunnyrock/djangoProject/web_mysqli')
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
site.addsitedir('/home/sunnyrock/vernv/lib/python2.7/site-packages')
sys.path.append(os.path.join(PROJECT_ROOT, ".."))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
