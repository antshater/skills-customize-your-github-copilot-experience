from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    tags: List[str] = []

posts: List[BlogPost] = []

@app.get("/posts")
def get_posts():
    # Return all blog posts
    return posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    # Find a post by ID and return it
    for post in posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts")
def create_post(post: BlogPost):
    # Add a new post to the list and return it
    posts.append(post)
    return post

@app.get("/search")
def search_posts(query: str = Query(..., min_length=3), limit: int = 5):
    # Return posts that match the search query in the title or content
    results = [post for post in posts if query.lower() in post.title.lower() or query.lower() in post.content.lower()]
    return results[:limit]
