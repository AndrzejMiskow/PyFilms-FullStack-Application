## Project Base for Django 

This is an example project that can be used as a starting point to create Django project.
It contains all the necessary configuration and some placeholder files to get you started.

### Running the Application
There are two ways to run the application :  In the terminal where manage.py is located run "python3 manage.py runserver" to run the test server , another way is through Atom's IDE terminal plugin with the same command 

The following should show in the terminal

> System check identified no issues (0 silenced).
> 
> February 17, 2021 - 04:10:29
> 
> Django version 3.1.6, using settings 'mysite.settings'
> 
> Starting development server at http://127.0.0.1:8000/
> 
> Quit the server with CONTROL-C.
> 
> Not Found: /
> 
> [17/Feb/2021 04:10:36] "GET / HTTP/1.1" 404 2031





To test that it works , go to your browser of choice and enter in the url http://127.0.0.1:8000/admin , should show the admin web interface. As the file has been altered if you were to just type http://127.0.0.1:8000 it will show 404 error 


### Prequisties needed 


1. **Python3 (Verison 3.7.5)**
- Django 1.1 installation supports python 2.7 however if using pip to install package would lead to issues hence the use of python3 



2. **Django**
- After creating folder to store project , open a terminal and run  "python3 -m pip install Django " . This would start to download the latest stable version of Django. 

        If any issues follow the guide here for the set-up
        https://docs.djangoproject.com/en/3.1/intro/tutorial01/


3. **Atom (Optional)**
- Used Atom as allowed for split terminal window plugin , (Preference -> Install -> Search(Terminal Platform) --> install platformio-ide-terminal)


### Brief idea (overview)
Overarching idea that for a project there can be many apps so e.g admin site & webpage & database with each considered as an "app"



#### IMPORTANT FILES TO TAKE NOTE OF 
1. url.py - Maps the path of your application e.g has
2. setting.py - Application Configuration , Database Connection (By default using sqlite3),Timezone
3. views.py 


#### Files 

In the zipfile currently : 
- Mysite Folder is the overall project, in it will contain the admin panel
- Protype contains the database structure and logic


#### /PROTOTYPE
- /prototype contains the database structure for Movies & Cinemas 
- /prototype/admin.py - Allows interaction of the database from the admin web interface
- /prototype/models.py - Database layout 
- /prototype/view.py - HTTP response when someome were to enter that URL 



## Accessing the Admin Webinterface

1. In your browser URL navigate to http://127.0.0.1:8000/admin, it should show a login form
2. Enter in the credentials **admin::12345** , in the event if the credentials were not able to work,enter the following command:
            
         **"python3 manage.py createsuperuser"**

3. Interface should show and you can interact with user permissions. See, add , delete and alter data in the database(Movies). 

### More Information and Next Steps
-Django Documentation


#### Notes
If you run application remember to use python3 not python2 if not certain default files due to format will fail.
