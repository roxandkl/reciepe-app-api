# recipe-app-api

##Software Description
Source code of backend REST API for recipe app. It can be cloned in local machine using
'''
$ git clone https://github.com/roxandkl/reciepe-app-api.git
''' 

##Techonlogies Used
* Python
* Django
* Django-Rest-Framework
* Docker/ Docker-Compose
* Pillow
* Postgres

##Getting started
Application can be started using 
'''
$ docker-compose up
'''
The API is then available at http://127.0.0.1:8000.

##Endpoints
The API has following endpoints

admin/
api/user/
api/reciepe/ ^tags/$ [name='tag-list']
api/reciepe/ ^tags\.(?P<format>[a-z0-9]+)/?$ [name='tag-list']
api/reciepe/ ^ingredients/$ [name='ingredient-list']
api/reciepe/ ^ingredients\.(?P<format>[a-z0-9]+)/?$ [name='ingredient-list']
api/reciepe/ ^reciepes/$ [name='reciepe-list']
api/reciepe/ ^reciepes\.(?P<format>[a-z0-9]+)/?$ [name='reciepe-list']
api/reciepe/ ^reciepes/(?P<pk>[^/.]+)/$ [name='reciepe-detail']
api/reciepe/ ^reciepes/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='reciepe-detail']
api/reciepe/ ^reciepes/(?P<pk>[^/.]+)/upload-image/$ [name='reciepe-upload-image']
api/reciepe/ ^reciepes/(?P<pk>[^/.]+)/upload-image\.(?P<format>[a-z0-9]+)/?$ [name='reciepe-upload-image']
api/reciepe/ ^$ [name='api-root']
api/reciepe/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^media/(?P<path>.*)$