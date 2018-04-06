from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

manager = Manager(app)  # Used to configure command line scripts

manager.add_command('db', MigrateCommand)  # python manage.py db <command>
# python manage.py db  # to see all commands
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade

if __name__ == '__main__':
    manager.run()
