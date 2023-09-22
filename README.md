# channel-dashboard
+ Clone the repository and navigate into the folder
  ```
  git clone https://github.com/prathishbv/channel-dashboard.git
  cd channel-dashboard/ 
  ```
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
+ Now in the Admin page of Django try adding a new device or modifying the existing devices, the same will be reflected in the Tkinter application. There you can filter the devices based on their status also.



## Output:
### Initial dashboard
![Screenshot from 2023-09-22 17-09-11](https://github.com/prathishbv/channel-dashboard/assets/81792348/b7988b06-7ba7-4916-b766-19d8650b17e4)

### Dashboard after adding some devices
![Screenshot from 2023-09-22 17-11-02](https://github.com/prathishbv/channel-dashboard/assets/81792348/14779d54-db4a-4cfc-a87c-fd3d33863824)

### Dashboard after filtering
![Screenshot from 2023-09-22 17-11-15](https://github.com/prathishbv/channel-dashboard/assets/81792348/819dcfb1-8337-4349-af71-ff53e9e9b46a)

### Models created 
![Screenshot from 2023-09-22 17-09-35](https://github.com/prathishbv/channel-dashboard/assets/81792348/e9458b8d-5700-4008-a5c4-582188f11d00)
