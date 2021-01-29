import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from app import app, db


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ido:Aa123456@localhost:5432/budget"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()