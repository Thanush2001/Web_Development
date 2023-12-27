import pyautogui as p
import time
import random  # Import the random module

# Define the list of search queries
search_queries = [
    "English to tamil Meaning covert tools details",
    "Tamilnadu news",
    "Andhra trending news",
    "kerala animal",
    "java example code",
    "python example code",
    "html example code",
    "css attributes",
    "what is git",
    "explan github",
    "variable means",
    "Trending tamil news",
    "Trending chittoor news",
    "beautiful story",
    "natural content",
    "lion content",
    "birds content",
    "laptop feature",
    "movie list thalapathy",
    "ajith movie list",
    "songs", "tamil audio", "macro vba", "tamilnadu land size",
    "kutty story", "book name history",
    "maths formulas", "earth rotates",
    "bharathiyar song list", "resume templates"
    # Add more search queries as needed
]

# Shuffle the search_queries list randomly
random.shuffle(search_queries)

# Define how many times to repeat the search for each query
num_searches_per_query = 1

time.sleep(3)

for search_query in search_queries:

    for _ in range(num_searches_per_query):
        # Type the modified search query and press Enter
        p.typewrite(search_query)
        p.press("enter")

        # Wait for a moment (adjust the time if needed)
        time.sleep(5)

        # Press Enter again (optional)
        p.press("enter")

        # Wait for a moment before the next search
        time.sleep(1)
