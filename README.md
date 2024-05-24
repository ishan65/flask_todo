# About TODO

#####  This application require db to perform CRUD operation. 

If running code from local system then perform change in the `web.py` as follows:

comment:
`app.config["MYSQL_HOST"] = "mysql-db"`
uncomment:
`app.config["MYSQL_HOST"] = "localhost"`

Ensure the mysql is up and running before running the application in localhost i.e not in the docker environment


### To run the script
```
python web.py
```

### Web visible
```
http://127.0.0.1:5789/
```

### To execute the tests
```
pytest tests\test_web.py
```

### To execute the syntax tests
```
flask8 ./
```

### Coverage report
```
python -m pytest --cov-report term-missing --cov=./
```

### Bring up development environment
```
docker compose up
```
