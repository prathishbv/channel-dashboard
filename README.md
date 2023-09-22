# channel-dashboard

+ Create a virtual environment
```
python -m venv venv
```
+ Activate your virtual environment
```
source venv/bin/activate
```
+ Install the requirements
```
pip install -r requirements.txt
```
+ Navigate to the folder consisting of manage.py and create a superuser in Django
```
cd dashboard/
python manage.py createsuperuser
```
+ Migrate the models
```
python manage.py makemigrations
python manage.py migrate
```
+ Run the Django server
```
python manage.py runserver
```
+ Open another terminal and navigate to the frontend folder.
```
cd frontend/
```
+ Run the tkinter code
```
python dashboard.py 
```
+ Frontend code prompts for a username and password in the terminal, give the credentials as same as the credentials provided while creating the superuser in Django
```
Enter the username: sample_username
Enter the password: sample_password
```
+ Now in the Admin page of Django try adding a new device or modifying the existing devices, the same will be reflected in the Tkinter application. There you can filter the devices based on the status also
