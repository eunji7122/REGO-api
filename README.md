# setting 



##### 1) File - Settings - Build, Execution, Deployment - Console - Python Console

Environment variables : DJANGO_SETTINGS_MODULE=REGO_api.settings

Python interpreter: project Default (Python 3.7 (REGO-api))

...

Starting script

```
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
import django
django.setup()
```



##### 2) Terminal

```
pip install django
pip install -r requirements.txt
pip manage.py makemigrations
pip manage.py migrate
pip manage.py runserver
```



