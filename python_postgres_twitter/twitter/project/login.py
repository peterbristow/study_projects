from database import Database
from twitter_utils import get_request_token, get_oauth_verifier, get_access_token
from user import User

Database.initialise(
	user='peter',
	password='hp271008',
	database='learning',
	host='localhost'
)

user_screen_name = raw_input("Enter your Twitter screen name: ")
user = User.load_from_db_by_screen_name(user_screen_name)

if not user:
	request_token = get_request_token()
	oauth_verifier = get_oauth_verifier(request_token)
	access_token = get_access_token(request_token, oauth_verifier)

	user = User(user_screen_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
	user.save_to_db()


tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])
