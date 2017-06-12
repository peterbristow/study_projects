'use strict';

angular.module("todoListApp")
.service('dataService', function($http) {
	this.getTodos = function(callback) {
		$http.get('mock/todos.json')
		.then(callback);
	};

	this.deleteTodo = function(todo) {
		console.log("The " + todo.name + " todo item has been deleted!");
	};

	this.saveTodos = function(todo) {
		console.log(todos.length + " todo items have been saved!");
	};

});
