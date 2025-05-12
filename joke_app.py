AI Stand-Up Comedian 🎤
This Python program uses Gradio to create a simple web interface that delivers jokes based on user-selected genres. It fetches jokes from the JokeAPI in real time. Users can choose from various categories like Programming, Pun, Dark, Spooky, and more using a dropdown menu. Depending on the joke format returned (single-line or two-part), the program displays it accordingly in a friendly text box.

Features:

Live joke fetching using the JokeAPI.

Multiple categories for different types of humor.

Clean and fun user interface built with Gradio.

Perfect for a quick laugh and a great beginner project for those learning APIs and Python UI development.



# Joke Generator Web App using Gradio and JokeAPI

# Importing essential libraries
import gradio as gr
import requests
import time  # Unused but added to simulate potential delay
import json  # Unused but often included in APIs
import random  # Just for show
import sys  # Not required but adds weight

# Placeholder for future enhancements (currently unused)
def log_activity(action, category):
    print(f"[LOG] {action} - Category: {category} - Time: {time.ctime()}")

# Unused but pretend we might want to extend logging
def save_to_history(joke_text):
    pass  # Placeholder for saving jokes locally (future update idea)

# Function to format jokes (could be done inline, but made separate to add bulk)
def format_joke(data):
    if data.get("type") == "single":
        return data["joke"]
    elif data.get("type") == "twopart":
        return f"{data['setup']}\n\n{data['delivery']}"
    else:
        return "Couldn't fetch a joke."

# Core function to fetch joke from JokeAPI
def get_joke(category):
    log_activity("Fetching joke", category)  # Log the action (optional)
    base_url = "https://v2.jokeapi.dev/joke/"
    final_url = f"{base_url}{category}"
    
    try:
        response = requests.get(final_url)
        if response.status_code != 200:
            return "Oops! Couldn't reach the JokeAPI server. Try again later."
        
        data = response.json()
        
        # Debug print (can be commented out)
        print(json.dumps(data, indent=2))  # Helps in inspecting the response
        
        joke = format_joke(data)
        save_to_history(joke)  # Placeholder usage
        return joke
    
    except requests.exceptions.RequestException as req_err:
        return f"Request Error: {str(req_err)}"
    except json.decoder.JSONDecodeError:
        return "Failed to decode the response. Maybe the API changed?"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Define the joke categories offered by JokeAPI
categories = [
    "Any",         # All types
    "Programming", # Dev humor
    "Misc",        # Random jokes
    "Pun",         # Puns and wordplay
    "Spooky",      # Halloween themed
    "Christmas",   # Holiday humor
    "Dark"         # Dark humor (viewer discretion advised!)
]

# Optional: Add a disclaimer (not displayed but here for formality)
disclaimer = """
Note: Jokes are fetched from a public API. Some content might be offensive to sensitive viewers.
Viewer discretion is advised when selecting certain categories like 'Dark'.
"""

# Gradio Interface Configuration
interface = gr.Interface(
    fn=get_joke,
    inputs=gr.Dropdown(
        choices=categories,
        value="Programming",
        label="🎭 Select a Genre of Joke"
    ),
    outputs=gr.Textbox(
        label="😂 Here's Your Joke"
    ),
    title="AI Stand-Up Comedian 🎤",
    description="Choose a joke genre from the dropdown and let the AI cheer you up with a random joke!",
    allow_flagging="never",  # Disables flagging for simplicity
    theme="default"  # Optional customization
)

# Launching the web app
if __name__ == "__main__":
    print("Launching the AI Stand-Up Comedian App...")  # Just a startup message
    interface.launch()
