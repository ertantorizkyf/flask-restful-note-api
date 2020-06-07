# flask-restful-note-api
This is a sample restful api using the Flask-RESTful library in python.

This API is used to create, read, update, and delete note.

### Using the app

1. Rename config_sample.py to config.py and adjust the configuration
2. Migrate the database
```
example:
flask db init
flask db migrate
flask db upgrade
```
Select the flask environment to run
```
example:
set flask_config=development
set flask_env=development
set flask_app=run.py
``
