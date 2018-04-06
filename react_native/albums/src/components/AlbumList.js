// Import libraries to help create a component
import React, { Component } from 'react';
import { ScrollView } from 'react-native';
import AlbumDetail from './AlbumDetail';

// Class based component - must define a render method
class AlbumList extends Component {
	// Set up state using a class level property
	state = { albums: [] };

	// Lifecycle Method
	componentWillMount() {
		fetch('https://rallycoding.herokuapp.com/api/music_albums')
		.then((response) => response.json())
		.then((responseData) => {
			this.setState({ albums: responseData });
		});
	}

	renderAlbums() {
		return this.state.albums.map(album => 
			<AlbumDetail key={album.title} album={album} />  // passing prop here
		);
	}

	render() {

		console.log(this.state);

		return (
			<ScrollView>
				{this.renderAlbums()}
			</ScrollView>
		);
	}
}

export default AlbumList;
