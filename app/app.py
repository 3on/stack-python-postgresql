# Read the environment variables
import json
import os
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

if not os.path.exists('/home/dotcloud/environment.json'):
    env = {
        'DOTCLOUD_DB_SQL_LOGIN': '',
        'DOTCLOUD_DB_SQL_PASSWORD': '',
        'DOTCLOUD_DB_SQL_HOST': 'localhost',
        'DOTCLOUD_DB_SQL_PORT': '5432',
    }

# Flask setup
from flask import Flask
app = Flask(__name__)


# PostgreSQL connection
import psycopg2
conn = psycopg2.connect(database="test",
                        user=env['DOTCLOUD_DB_SQL_LOGIN'],
                        password=env['DOTCLOUD_DB_SQL_PASSWORD'],
                        host=env['DOTCLOUD_DB_SQL_HOST'],
                        port=int(env['DOTCLOUD_DB_SQL_PORT']))
cur = conn.cursor()

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()