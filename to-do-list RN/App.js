import React, { Component } from "react";
import { Text, View, ScrollView, StyleSheet, Image } from "react-native";
import { CheckBox, Button, Input } from "react-native-elements";
import { Constants } from "expo";

var taskName = "";
var mainId = 5;

var todoData = [
    {
        id: 1,
        text: "Take out the trash.",
        completed: true,
    },
    {
        id: 2,
        text: "Grocery shopping.",
        completed: false,
    },
    {
        id: 3,
        text: "Clean gecko tank.",
        completed: false,
    },
    {
        id: 4,
        text: "Mow lawn.",
        completed: true,
    },
    {
        id: 5,
        text: "Catch up on The Clone Wars.",
        completed: false,
    },
];

function ToDoItem(props) {
    const completedStyle = {
        fontStyle: "italic",
        color: "#cdcdcd",
        textDecoration: "line-through",
    };

    return (
        <View className="todo-item" style={{ flex: 1, flexDirection: "row" }}>
            <CheckBox
                checked={props.task.completed}
                onPress={() => props.handleChange(props.task.id)}
            />

            <Text style={props.task.completed ? completedStyle : null}>
                {props.task.text}
            </Text>

            <Button
                onPress={() => props.handleDelete(props.task.id)}
                title="Delete"
            />
        </View>
    );
}

export default class App extends Component {
    constructor() {
        super();
        this.state = {
            todos: todoData,
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
        this.handleUpdate = this.handleUpdate.bind(this);
        this.handleAdd = this.handleAdd.bind(this);
    }

    handleChange(id) {
        console.log(id);
        this.setState((prevState) => {
            const updatedTodos = prevState.todos.map((todo) => {
                if (todo.id === id) {
                    todo.completed = !todo.completed;
                }
                return todo;
            });

            console.log(updatedTodos);

            return {
                todos: updatedTodos,
            };
        });
    }

    handleDelete(id) {
        this.setState((prevState) => {
            const updatedTodos = prevState.todos.filter((todo) => {
                if (todo.id != id) {
                    return todo;
                }
            });

            console.log(updatedTodos);
            console.log("id " + mainId);
            return {
                todos: updatedTodos,
            };
        });
    }

    handleUpdate(data) {
        taskName = data;
    }

    handleAdd() {
        mainId++;
        const newTask = {
            id: mainId,
            text: taskName,
            completed: false,
        };

        let updatedTodos = this.state.todos;
        updatedTodos.push(newTask);
        console.log(updatedTodos);
        console.log("id " + mainId);

        this.setState({ todos: updatedTodos });
    }

    render() {
        const todoComponents = this.state.todos.map((task) => {
            return (
                <ToDoItem
                    key={task.id}
                    task={task}
                    handleChange={this.handleChange}
                    handleDelete={this.handleDelete}
                />
            );
        });

        return (
            <View className="todo-list">
                {todoComponents}
                <Input
                    placeholder="enter a task"
                    onChangeText={this.handleUpdate}
                />
                <Button onPress={this.handleAdd} title="submit" />
            </View>
        );
    }
}
