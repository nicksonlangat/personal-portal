install:
	pip3 install -r requirements.txt
test:
	python3 manage.py test
migrations:
	python manage.py makemigrations

migrate:
	python3 manage.py migrate

superuser:
	python manage.py createsuperuser

collectstatic:
	python manage.py collectstatic

serve:
	python3 manage.py runserver

shell:
	python manage.py shell

gunicorn:
    gunicorn --bind 0.0.0.0:8000 mysite.wsgi

set_env_vars:
	source venv/bin/activate

hard_delete:
	python3 manage.py dropstalenotifications

.PHONY: set_env_vars
