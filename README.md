# [Education Management System](https://educationmanagementsystem.herokuapp.com/)

*EDUCATION MANAGEMENT SYSTEM (EMS)*  is a flagship product of Easy Solution which covers all aspects of Universities, Colleges or Schools. EUMS covers every minute aspects of a universities work flow and integrates all processes with user friendly interface.

### Motivation

This project was done as the part of *MAKAUT* Hackathon topics. And as student we form a team and took this projects under mentorship of _Syan Nath Sir_. Our purpose is to make task like taking attandence in the univertity easy and manageable.

### Tech/framework used

1. Django (_Backend_)
2. Bootstrap UiKit Template (_FrontEnd_)
3. Jquery (_For Ajax_)
4. Chart.js (_For Graph_)

### Features

+ Their are three category of user Admin, Staff & Student. Each have their own view set.

+ Minimal Graphs are provided for better ui.

+ Feedback and Leave form are present.


### Installation

1. Download it from git and open the folder
2. Get inside the folder `UniversityManagementSystem`
3. Run command `pip install -r requirements.txt`
4. Incase of error run command python `manage.py makemigrations managementApp` and `python manage.py migrate`
5. Type `python manage.py runserver`
6. Create a admin user `python manage.py createsuperuser` provide details and login into the page.

#### How to use?

If you are running locally go throught Installation and then vist 127.0.0.1:8000 in your browser. Then login and add student & staff task.


#### Future Updates

1. By useing rest api and fontend libary like react, vue, etc. Application become more compact and faster to use.
2. By push application to online server and configured it to smtp email password reset can be provided.
