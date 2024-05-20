import os
import moment
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
load_dotenv()
# Configure your secret key and JWT settings
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
secret_key = os.environ.get('SECRET_KEY')
db_password = os.environ.get('PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://task_manager_c6us_user:wiLe8G8ZfRZLMhAofiebxl05a2XyBqwQ@dpg-cp5ds9q1hbls73fdoi50-a.oregon-postgres.render.com/task_manager_c6us'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
