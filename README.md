# Note-Website
## Overview
This GitHub repo showcases a beginner-friendly web-app I built using Flask and SQLite. 

The goal of this project was to gain hands-on experience and a better understanding of how web frameworks and relational databases work in Python. 
It's a small full-stack application that uses HTML and CSS for front-end visuals and styling, with Flask’s Jinja2 templating engine to connect the 
front end to the Python-powered backend.


## Project Structure
The project is organized into several key python files and folders:
  + _app_ folder = 
    + templates folder = Collection of all the front-end templates
      + base.html = The 'main' template that all others inherit from to have the same main styling choices
      + landpage.html = Template of what the user first sees when they go on the web-app
      + dashboard.html = Template Where the user can create and delete user-saved notes
      + login3.html = Template where the user logs in
      + signup.html = Template  where the user signs up 
    + models.py =  where database models are created for the user and his/her notes
    + routes.py = where all the url routes and their endpoint functions are written, including the views and authenticated routes
    + init.py   = where the function called by main is created, making a instance of flask app and a empty SQLite-database with blueprints initialized from elsewhere in the app folder
  + main.py = where the app gets created and run locally by
  + requirements.txt =  all the libraries from any packages installed 

## Setup
### To run this web app yourself, you will need to install the following(via pip):
  + flask
  + flask_sqlalchemy

#### To install the required Python packages, you can use the following commands:
    pip install flask
    pip install flask_sqlalchemy

    
#### Below is all the libraries from any packages installed and their versions when the project was created:
    blinker==1.9.0
    click==8.2.1
    colorama==0.4.6
    Flask==3.1.1
    Flask-SQLAlchemy==3.1.1
    greenlet==3.2.3
    itsdangerous==2.2.0
    Jinja2==3.1.6
    MarkupSafe==3.0.2
    SQLAlchemy==2.0.41
    typing_extensions==4.14.0
    Werkzeug==3.1.3

#### After everything has been installed and cloned, you can run the app using:
    python main.py
Then open your browser and go to: http://127.0.0.1:5000/


## Features
- User sign-up and login functionality
- Dynamic landing page
- Basic user dashboard for creating or deleting saved notes
- HTML templating with Jinja2
- Data persistence with SQLite and SQLAlchemy



