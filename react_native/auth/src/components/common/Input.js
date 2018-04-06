import React from 'react';
import { View, Text, TextInput } from 'react-native';

const Input = ({ label, placeholder, value, onChangeText, secureTextEntry }) => {
	const { containerStyle, labelStyle, inputStyle } = styles;

	return (
		<View style={containerStyle}>
			<Text style={labelStyle}>{label}</Text>
			<TextInput
				style={inputStyle}
				autoCorrect={false}
				secureTextEntry={secureTextEntry}
				placeholder={placeholder}
				value={value}
				onChangeText={onChangeText}
			/>
		</View>
	);
};

const styles = {
	containerStyle: {
		height: 40,
		flex: 1,
		flexDirection: 'row',
		alignItems: 'center'
	},
	labelStyle: {
		fontSize: 18,
		paddingLeft: 20,
		flex: 1,
	},
	inputStyle: {
		color: '#000',
		paddingLeft: 5,
		paddingRight: 5,
		fontSize: 18,
		lineHeight: 23,
		flex: 2
	}
}

export { Input };
