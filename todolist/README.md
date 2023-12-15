# To-do-list

Members:
- Alcordo, Roxanne - [roxsand](https://github.com/roxsand)
- Guinita, Daniel - [daniel-guinita](https://github.com/daniel-guinita)
- Pulvera, Wellmar - [wellmarpulvera](https://github.com/wellmarpulvera)

## Setup
1. Create a virtual environment:
```sh
python -m venv .venv
```

2. Activate the virtual environment
for windows powershell:
```sh
.venv\Scripts\activate
```

3. Install Flask, mysqldb, dotenv:
```sh
pip install Flask
```
Install mysqldb
```sh
pip install flask-mysqldb
```
Install dotenv
```sh
pip install python-dotenv
```

<!-- 4. Create a `.env` file and with the following template:
```sh
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DB=questnight
MYSQL_CURSORCLASS=DictCursor
MYSQL_AUTOCOMMIT=true

PORT = 5000
``` -->

### Running the Flask app
```sh
flask --app app.py run --debug
```