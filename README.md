# Coding_Challenge_Siemens
Development of a prototype of a topic modelling intelligence service

In the prototype of this topic-modelling intelligence service, a central python controller exposes an API that enables a user to add a new  topic, get articles of a topic, update a topic with new articles, and also fetch the status of the intelligence service.  

Database structure is created with the articles under topics. These articles can be assigned to a predefined topic.
Data can be inserted using insert queries to manually create an example dummy database. 

Add a new topic: /api/add/<topic>. 
Add some dummy articles to the topic in the database.  Returns a success or failure response.  
  
Getting all articles of a topic  is done using API: /api/fetch/<topic> 
Returns all articles assigned the topic passed with the request.  
  
Status of the system  - API: /api/topics
Returns all available topics and a count of all articles under each topic. 

The controller is written in Python / Django.  The controller runs on Linux hosts


Requirements

python -m pip install django django-rest_framework

Run the server:
---------------
python3 manage.py runserver


1.  To list All Topic:
------------curl http://localhost:8000/api/topics

2. Add a topic:
---------------
curl http://localhost:8000/api/add/topic1


3. Fetch all articles under a topic:
---------------------------curl http://localhost:8000/api/fetch/topic1

4. Add an article under a topic:
-------------------------------
curl http://localhost:8000/api/update/topic1 -d 'article=test article1 for topic1'
