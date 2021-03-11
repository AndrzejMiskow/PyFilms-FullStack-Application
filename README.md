### Running the Project
In the terminal where manage.py is located run "python3 manage.py runserver" to run the server

The following should show in the terminal

> System check identified no issues (0 silenced).
> 
> [date and time]
> 
> Django version 3.1.6, using settings 'mysite.settings'
> 
> Starting development server at http://127.0.0.1:8000/
> 
> Quit the server with CONTROL-C.





To test that it works , go to your browser and enter in the url http://127.0.0.1:8000/admin , should show the admin web interface. Currently there there is no homepage so /admin or /helloworld are the only pages.


### Prequisties needed 


1. **Python3 (Verison 3.7.5)**
- Django 1.1 installation supports python 2.7 however if using pip to install package would lead to issues hence the use of python3 

2. **virtualenv (Optional)**
- Using a virtual environment may prove useful if you don't want to or can't install Django universally on your local machine. It creates a Python environment solely for use in this project.
- To install use `sudo pip install virtualenv`, then `virtualenv newenv` (or a name of your choice), then execute `source newenv/bin/activate`
- You can then install Django as per the instructions below
- To exit the enviornment just enter `deactivate`

3. **Django**
- After creating folder to store project , open a terminal and run  "python3 -m pip install Django " . This would start to download the latest stable version of Django. 

        If any issues follow the guide here for the set-up
        https://docs.djangoproject.com/en/3.1/intro/tutorial01/


4. **Pillow**
- Used for image processing, `pip install pillow`

5. **QRCode**
- Generates QR codes, `pip install qrcode`

6. **xhtml2pdf**
- Used for making pdf tickets `pip install xhtml2pdf`

7. **django extensions**
- Adds features to django like scripts `pip install django-extensions`

### Structure Overview
PyFilmsInc_root is the main directory we'll be working from. Within this individual apps can be created for different purposes. Apps can be easily
added, removed, or modified without effecting one another.

There's more info and resources for Django and apps in the git wiki.



#### IMPORTANT FILES TO TAKE NOTE OF 
1. url.py - Maps the path of your application e.g has
2. setting.py - Application Configuration , Database Connection (By default using sqlite3),Timezone
3. views.py 


## Accessing the Admin Webinterface

1. In your browser URL navigate to http://127.0.0.1:8000/admin, it should show a login form
2. Enter in the credentials **admin::12345** , in the event if the credentials were not able to work,enter the following command:
            
         **"python3 manage.py createsuperuser"**

3. Interface should show and you can interact with user permissions. See, add , delete and alter data in the database
