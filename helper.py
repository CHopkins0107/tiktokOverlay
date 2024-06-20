"""Sanitize the first line of the generated post to be saved as text file"""
import re

def make_name(post):
    return post.splitlines()[0]

def clean_name(filename):
    invalid_chars = r'[<>:"/\\|?*]'
    
    sanitized = re.sub(invalid_chars, '', filename) + ".txt"
    return sanitized