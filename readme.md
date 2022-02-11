# Run RudaTipper app
```
git clone https://github.com/marychev/rudatipper.git
cd rudatipper/
python3 -m venv venv
. venv/bin/activate
pip install django
python manage.py runserver
```


### Start django app
```
mkdir rudatipper
cd rudatipper/
python3 -m venv venv
. venv/bin/activate
pip install django
django-admin startproject rudatipper
python manage.py migrate
cd rudatipper/
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```