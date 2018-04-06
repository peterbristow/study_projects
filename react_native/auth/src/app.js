import React, { Component } from 'react';
import { View } from 'react-native';
import firebase from 'firebase';
import { Header, CardSection, Button, Spinner } from './components/common';
import LoginForm from './components/LoginForm';

class App extends Component {
	state = { loggedIn: null };

	componentWillMount() {
		firebase.initializeApp({
			apiKey: 'AIzaSyAzKCqfkQxPO5OJLLtnQcLJHbFcsmsGsZI',
			authDomain: 'auth-528b3.firebaseapp.com',
			databaseURL: 'https://auth-528b3.firebaseio.com',
			projectId: 'auth-528b3',
			storageBucket: 'auth-528b3.appspot.com',
			messagingSenderId: '267720530323'
		});

		firebase.auth().onAuthStateChanged((user) => {
	      if (user) {
	        this.setState({ loggedIn: true });
	      } else {
	        this.setState({ loggedIn: false });
	      }
	    });
	}

	renderContent() {
		switch (this.state.loggedIn) {
			case true:
				return (
					<CardSection>
						<Button onPress={() => firebase.auth().signOut()}>
							Log Out
						</Button>
					</CardSection>
				);
			case false:
				return <LoginForm />;
			default:
				return (
					<CardSection>
						<Spinner size="large" />
					</CardSection>
				);
		}
	}

	render () {
		return (
			<View>
				<Header headerText="Authentication" />
				{this.renderContent()}
			</View>
		);
	}
}

export default App;
