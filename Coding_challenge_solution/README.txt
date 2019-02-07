


python -m pip install django django-rest_framework

Run the server:
---------------
python3 manage.py runserver




1. List All Topic:
------------curl http://localhost:8000/api/topics


2. Add a topic:
---------------
curl http://localhost:8000/api/add/topic1


3. Fetch all articles under a topic:
---------------------------curl http://localhost:8000/api/fetch/topic1



4. Add an article under a topic:
-------------------------------
curl http://localhost:8000/api/update/topic1 -d 'article=test article1 for topic1'