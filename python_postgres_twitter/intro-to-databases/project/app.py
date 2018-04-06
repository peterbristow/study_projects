from database import Database
from user import User


Database.initialise(
	user='peter',
	password='hp271008',
	database='learning',
	host='localhost'
)

user = User('hema@email.com', 'Hema', 'Smith', None)

user.save_to_db()

user = User.load_from_db_by_email('peter@email.com')

print(user.email)
print(user.first_name)
print(user.last_name)