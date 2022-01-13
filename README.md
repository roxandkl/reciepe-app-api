# recipe-app-api

## Software Description
Source code of backend REST API for recipe app. It can be cloned in local machine using
```
$ git clone https://github.com/roxandkl/reciepe-app-api.git
```

## Techonlogies Used
* Python
* Django
* Django-Rest-Framework
* Docker/ Docker-Compose
* Pillow
* Postgres

## Getting started
Application can be started using 
```
$ docker-compose up
```
The API is then available at http://127.0.0.1:8000.

## Endpoints
The API has following endpoints

admin/

api/user/ 

api/reciepe/tags/

api/reciepe/tags/<int>/

api/reciepe/ingredients/

api/reciepe/ingredients/<int>/

api/reciepe/reciepes/

api/reciepe/reciepes/<int>/

api/reciepe/reciepes/<int>/upload-image/

api/reciepe/reciepes/<int>/upload-image/<int>/
