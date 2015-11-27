# hungryally Installation Steps

- Install Virtual Env and Virtual Env wrapper

- Make a new virtual env with python version as 3.5

- activate the virtual environment that you have made

- sudo pip install -r requirements.txt

- install postgres database

- copy line number 85 till 90 from settings.py file (all the database part)

- Make a local_settings.py file

- paste the copied part into your local_settings.py file, and change all these database parameters: NAME,USER,PASSWORD,PORT,HOST

- run the migrate command, to add/update database schema tables: python manage.py migrate recipesearch --settings=recipeally.local_settings

- type the following command using command line - python manage.py runserver 0:8000 --settings=recipeally.local_settings

- open browser and type localhost:8000, you should see the default django page

- To add the the configured css to the page you're making add 
<head>
{% load staticfiles %}
<link rel='stylesheet' href='{% static "style.css" %}' type='text/css' />
</head>

to the top of the page

Copy HTML from http://inspirythemesdemo.com/alt-foodrecipes/

#Steps followed for deploying the web app

 - http://docs.aws.amazon.com/gettingstarted/latest/wah-linux/getting-started-prereq.html
 
