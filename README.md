# CarWash Backend

## Run

 ### - Virtualenv
 After you have successfully created a virtualenv activate it by: source venv/bin/activate (linux)
 https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
 ### - Install requirements
 In 'activated' virtualenv run: pip install -r requirements.txt
 ### - Migrate
 Continue in virtualenv as always and run: python manage.py migrate
 ### - Createsuperuser (Optional)
 Create a superuser to be able to add some data from Django Admin: python manage.py createsuperuser
 
 ### - Finally run application
 command: python manage.py runserver
