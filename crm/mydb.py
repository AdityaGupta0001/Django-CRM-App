import mysql.connector
from dotenv.main import load_dotenv
import os

load_dotenv()

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = os.environ['MYSQL_ROOT_PASSWORD']
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crystallize_crm")

print('All done!')