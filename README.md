![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome  

This is the Code Institute student PP5 walkthrough Boutique Ado readme for the project deployed to [https://ib-pp5-ado.herokuapp.com/](https://ib-pp5-ado.herokuapp.com/)

Note: To open any links in this README in a new browser tab, press CTRL + Click or right click and open in new tab/window.

# Boutique Ado

### By [Ian Bowell](https://www.instagram.com/skianianiam/)

## **[Live site](https://ib-pp5-ado.herokuapp.com/)**

---

## Table of Contents
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Agile Development](#agile-development)
* [Testing](#testing)
* [User Experience Design (UX)](#ux)
* [Deployment](#deployment)
* [Release History](#release-history)
* [Credits](#credits)
* [Reminders](#reminders)



## Introduction

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

Boutique Ado is a website built in Django using Python, JavaScript, CSS and HTML. 

## Features

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

Features here

## Future Enhancements

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

Future Enhancements here

## Technologies Used

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

Technologies used here

## Agile Development

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

Agile here

## Testing

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

Testing here

## UX

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

UX here

## Deployment

* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

Deployment here


## Release History
* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#the-garage) 

We continually tweak and adjust this.

Here is the version history:

**20 March 2023:** Begin MVP planning.

**04 April 2023:** Successful initial heroku deployment.

**20 April 2023:** Successful initial post deletion logic. Needs more checks and post editing/adding.

**20 May 2023:** Successful deployment of submission features.

**16 June 2023:** Final deployment of submission features, following further documentation and testing.

------


## Credits
* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

-   ### Source code

    - Code Institute Django course material, tutors, mentors and colleagues in Slack channels.
    - Bootstrap documentation https://getbootstrap.com/docs/5.3/getting-started/introduction/ 
    
-   ### Images
    - Car images https://www.pexels.com/ 
    - favicon.ico generation https://favicon.io/favicon-generator/
    - Colors from [Lilybug Design](https://www.lilybugdesign.co.nz/procreate-color-palettes)


## Reminders
* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 

To install django, `pip3 install 'django<4' gunicorn`

This also installs the gunicorn. Gunicorn (‘Green Unicorn’) is a pure-Python WSGI server for UNIX. It has no dependencies and can be installed using pip.
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/

A Web Server Gateway Interface (WSGI) server implements the web server side of the WSGI interface for running Python web applications.
https://www.fullstackpython.com/wsgi-servers.html 

You may also want to install the following packages for the database and storage in Cloudinary.
Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
and `pip3 install dj_database_url==0.5.0 psycopg2`
and `pip3 install dj3-cloudinary-storage`

Once all is installed, you can record the installed packages to requirements.txt 
with `pip3 freeze > requirements.txt`

and reload them with `pip3 install -r requirements.txt` 

### Initiating the Django project files
To create the essential manage.py file and the key step in enabling the site to launch
use `django-admin startproject "put your appname here" .` DON'T forget the DOT at the end !!

We used garageblog for our blog about cars and other vehicles. Here we use `boutique-ado`
Don't forget the DOT at the end as this tells Django admin that we want to create our project in the current top level folder.

Then use `python3 manage.py startapp vehicles` for example, to create the vehicles app within the project

And we update `settings.py` with details for the apps, hosts and secrets etc.
Remove the default SECRET_KEY secret entry in settings.py and use the env.py load method detailed below.

You will also need to load the SECRET_KEY in settings.py from env.py with `SECRET_KEY = os.environ.get('SECRET_KEY')`

Use `python3 manage.py runserver` to launch web server once the environment variables are all set up

```
python3 manage.py runserver
```

We add the app with `python3 manage.py startapp blog` for example

Then we need to migrate the changes to the database etc with `python3 manage.py migrate`

Remember to update settings.py with all the env vars for secure access to Django and the Elephant DB in the database section

```
import os
import dj_database_url
from django.contrib.messages import constants as messages
if os.path.isfile('env.py'):
    import env
```

To set up a app/database admin we need `python3 manage.py createsuperuser`

To install the app in Heroku you need:

1) Environment variables from env.py in your Heroku app settings
2) A Procfile to run the webserver i.e. `web: gunicorn boutique-ado.wsgi` 
    
    in this case to run my boutique app on the gunicorn wsgi webserver.

Remember also to `python manage.py collectstatic`

The project can now be deployed to Heroku at the website configured above.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

and to address a common pylint warning, update `.gitpod.yml` with
```
    - ms-toolsai.vscode-jupyter-cell-tags
    - ms-toolsai.vscode-jupyter-slideshow
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code!

---

Happy coding!
* [Back to table of contents](#table-of-contents) 
* [Back to top of README.md](#boutique-ado) 
