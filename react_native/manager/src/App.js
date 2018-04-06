import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import firebase from 'firebase';
import ReduxThunk from 'redux-thunk';
import reducers from './reducers';
import Router from './Router';

class App extends Component {
  componentWillMount() {
    const config = {
      apiKey: "AIzaSyBho63NXs3Xe_WW5mPwYwd3giumLE_-irY",
      authDomain: "manager-f10de.firebaseapp.com",
      databaseURL: "https://manager-f10de.firebaseio.com",
      projectId: "manager-f10de",
      storageBucket: "manager-f10de.appspot.com",
      messagingSenderId: "531391349934"
    };
    firebase.initializeApp(config);
  }

  render() {
    const store = createStore(reducers, {}, applyMiddleware(ReduxThunk));

    return (
      <Provider store={store}>
        <Router />
      </Provider>
    );
  }
}

export default App;
