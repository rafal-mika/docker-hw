## Task 3 Docker - create Api and Redis via Docker-compose

This is an API application that you can read and write entries to the Redis store.
Entries are stored as key-value pairs.
To deploy services, just run `docker-compose up` in source directory (docker-compose.yml location)

-----
### API description
-----
API base path: `http://<host>:5000/api`

To get list of all keys go to `http://<host>:5000/api/keys` in your browser
or create a request from CLI:

- cUrl: `curl http://<host>:5000/api/keys`, 
- Windows PowerShell: `Invoke-WebRequest -Uri http://<host>:5000/api/keys`

To read an entry with a specified key:

- browser: `http://<host>:5000/api/keys/<key>`
- cUrl: `curl http://<host>:5000/api/keys/<key>`
- Windows PowerShell: `Invoke-WebRequest -Uri http://<host>:5000/api/keys/<key>`

To write an entry with a specified key:

- cUrl: `curl -X POST http://<host>:5000/api/keys -H "Content-Type: application/json" -d '{"key":<key>, "value":<value>}'`
- Windows PowerShell: `Invoke-WebRequest -Uri http://<host>:5000/api/keys -Method POST -ContentType "application/json" -Body '{"key":<key>, "value":<value>}'`
