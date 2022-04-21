```
python3 -m venv buildt-env //in src dir
source buildt-env/bin/activate
pip install -r requirements.txt
python manage.py runserver
python manage.py collectstatic // puts all apps static/ folder assets into root /static dir

### todo

- add `whitenoise` package to serve static content. perhaps digital ocean can serve files from nginx, need to double check. 

- add dash layout to authed portal section of site.  

```