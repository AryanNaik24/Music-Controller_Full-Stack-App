import React, { Component } from "react";
import { render } from "react-dom";

//way to extend class in react and exports it
export default class App extends Component {
    constructor(props){
        super(props);
    }
    render(){
        return <h1>Testing code</h1>;
    }
}

//gets div from index.html with id app
const appDiv = document.getElementById("app");

//renders app component in app div
render(<App/>,appDiv);