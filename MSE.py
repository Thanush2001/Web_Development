import pyautogui as p
import time

# Define the search query
search_query = "Eengliyash to tamil Meaning covert tools details"

# Define how many times to repeat the search
num_searches = 35

# Remove the last character from the search query
search_query = search_query[:-1]

time.sleep(3)
for _ in range(num_searches):
    # Type the modified search query and press Enter
    p.typewrite(search_query)
    p.press("enter")
    # Wait for a moment (adjust the time if needed)
    time.sleep(2)
    # Press Enter again (optional)
    p.press("enter")
    # Remove the last character again for the next iteration
    search_query = search_query[:-1]