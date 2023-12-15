mysql = None

def set_mysql(mysql_instance):
  global mysql
  mysql = mysql_instance

def get_mysql():
  global mysql
  return mysql

def get_connection():
  return get_mysql().connection

def get_cursor():
  return get_connection().cursor()

def execute(query, params=None):
  cursor = get_cursor()
  cursor.execute(query, params)
  return cursor

def fetchall(query, params=None):
  cursor = execute(query, params)
  result = cursor.fetchall()
  cursor.close()
  return result

def fetchone(query, params=None):
  cursor = execute(query, params)
  result = cursor.fetchone()
  cursor.close()
  return result