import logo from "./logo.svg";
import "./App.css";
import React, { useState, useEffect } from "react";
import Post from "./Post";

const BASE_URL = "http://localhost:8000/";

function App() {
  const [posts, setPosts] = useState([]); // Define a state variable for posts

  useEffect(() => {
    fetch(BASE_URL + "post/all")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => {
        setPosts(data); // Update the posts state with the fetched data
      })
      .catch((error) => {
        console.log(error);
        alert(error);
      });
  }, []);

  return "Hello World !";
}

export default App;
