import os
import requests

# Set your API key and the URL for the Matecat API
api_key = 'ODY3NjOGQwYjfd2b089e'
api_url = 'https://www.matecat.com/api/v2.1/'

# Get the current working directory
dir_path = os.getcwd()

# Loop through each file in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        # Read the contents of the HTML file
        file_path = os.path.join(dir_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()

        # Set the request payload for the Matecat API
        payload = {
            'q': file_contents,
            'source': 'en',
            'target': 'hi',
            'key': api_key,
            'format': 'html'
        }

        # Send the request to the Matecat API
        response = requests.post(api_url, data=payload)

        # Check for errors in the response
        if response.status_code != 200:
            print(f'Error: {response.status_code}')
            print(response.content)
            continue

        # Parse the response to get the translated HTML file
        response_data = response.json()
        if 'data' not in response_data or 'result' not in response_data['data']:
            print(f'Error: invalid response format')
            print(response.content)
            continue

        translated_html = response_data['data']['result']

        # Save the translated HTML file to a new file
        translated_filename = os.path.splitext(filename)[0] + '_hi.html'
        translated_file_path = os.path.join(dir_path, translated_filename)
        with open(translated_file_path, 'w', encoding='utf-8') as f:
            f.write(translated_html)
