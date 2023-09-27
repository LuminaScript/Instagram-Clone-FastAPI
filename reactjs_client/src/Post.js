import React, { userState, userEffect, useState, useEffect } from "react";
import "./Post.css";
import { Avatar, Button } from "@material-ui/core"

const BASE_URL = 'http://localhost:8000/'

function Post({ post, authToken, authTokenType, username }) {

  const [imageUrl, setImageUrl] = useState('')
  const [comments, setComments] = useState([])

  useEffect(() => {
    setComments(post.comments);
  } , [])

  useEffect(() => {
    if (post.image_url_type == 'absolute') {
      setImageUrl(post.image_url)
    } else {
      setImageUrl(BASE_URL + post.image_url)
    }
  }, [])

  
  return (
    <div className="post">

      <div className="post_header">
        <Avatar
          alt="Catalin"
          src=""/>
        <div className="post_headerInfo">
          <h3>{post.user.username}</h3>
          <Button className="post_delete">Delete</Button>
        </div>
      </div>
      <img
        className="post_image" // Corrected class name
        src={imageUrl}
      />

      <h4 className='post_text'>{post.caption}</h4>
      <div className='post_comments'>
        {
          comments.map((comment) => (
            <p>
              <strong>{comment.username}:</strong> {comment.text}
            </p>
          ))
        }
      </div>

    </div>
  )
}

export default Post;
