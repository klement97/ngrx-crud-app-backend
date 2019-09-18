# CarWash Backend

## Run

 ### - Virtualenv* (Required)
 After you have successfully created a virtualenv activate it by: source venv/bin/activate (linux)
 https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
 ### - Install requirements
 In 'activated' virtualenv run: pip install -r requirements.txt
 ### - Migrate* (Required)
 Continue in virtualenv as always and run: python manage.py migrate
 ### - Createsuperuser (Optional)
 Create a superuser to be able to add some data from Django Admin: python manage.py createsuperuser
 
 ### - Finally run application* (Required)
 command: python manage.py runserver
 It all becomes easier if you use Pycharm
 https://www.jetbrains.com/pycharm/download/#section=linux
