import oauth2
import urlparse

import constants

# https://dev.twitter.com/rest/public
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)

def get_request_token():
		# Create a consumer to identify app uniquely.
		client = oauth2.Client(consumer)  # client used to make requests

		# Use the client to perform a request for the request token.
		response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
		if response.status != 200:
			print("An error occurred while getting a request token from Twitter.")

		# Get the request token parsing the query string returned in 'content'.  Then convert to dict.
		return dict(urlparse.parse_qsl(content))


def get_oauth_verifier(request_token):
	# Ask user to authorise our app and give us the pin code.
	print("Go to the following website in your browser")
	print(get_oauth_verifier_url(request_token))

	return int(raw_input("What is the pin? "))


def get_oauth_verifier_url(request_token):
	return "{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token'])


def get_access_token(request_token, oauth_verifier):
	# Create a token object which contains the request token, and the verifier.
	token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)

	#Create a client with out consumer (our app) and the newly created (and verified) token.
	client = oauth2.Client(consumer, token)

	# Ask Twitter for an access token, and Twitter knows it should give us it because we've verified the request token.
	response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
	return dict(urlparse.parse_qsl(content))
