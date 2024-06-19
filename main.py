import os
from dotenv import load_dotenv, dotenv_values 

import praw
import openai
import tiktoken

load_dotenv() 

client_id = os.getenv("RDT_CLIENT_ID")
client_secret = os.getenv("RDT_CLIENT_SECRET")
user_agent = os.getenv("RDT_USER_AGENT")

# OpenAI API key
openai.api_key = os.getenv("OPENAI_SECRET")

# Initialize the Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Function to fetch posts from a subreddit
def fetch_posts(subreddit_name, limit=5):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.hot(limit=limit):
        if not post.stickied:
            posts.append(post.title + ' ' + post.selftext)
    return posts

def count_tokens(text, model="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Function to generate a similar post using OpenAI API
def generate_post(posts, max_tokens=10000, buffer=500):
    prompt = "You will create an original Reddit post for the subreddit 'AmITheAsshole,' adhering to the subreddit's theme where users submit stories from their personal lives and commenters vote on whether the original poster was at fault in the situation. The post should be entirely new and not based on any provided samples. Please ensure the post matches the length, structure, and tone of the subreddit, focusing on storytelling aspects—a concise narrative covering the context of the conflict, the conflict itself, and the immediate social outcome. Additionally, infuse the narrative with a small amount of absurdity and surrealism while still appearing non-fictional. Lastly, make sure all the characters are humans.\nSample posts:"
    total_tokens = count_tokens(prompt)
    
    for post in posts:
        post_tokens = count_tokens(post)
        if total_tokens + post_tokens + buffer <= max_tokens:
            prompt += post + "\n"
            total_tokens += post_tokens
        else:
            break
            
    prompt += "\n\nGenerated post:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the gpt-3.5-turbo model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4096  # Adjust this value as needed
    )
    
    return response.choices[0].message['content'].strip()

# Fetch posts and generate a similar post
subreddit_name = 'AmItheAsshole'
posts = fetch_posts(subreddit_name)
similar_post = generate_post(posts)
print(similar_post)