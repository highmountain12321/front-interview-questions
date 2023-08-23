import requests
from bs4 import BeautifulSoup

url = "https://github.com/Saran-pariyar/100_Days_Of_Frontend_Interview_Questions"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <h3> elements within <li> elements within <ol> element
question_elements = soup.select('ol li h3')

# Extract the text content of each <h3> element
questions = [element.get_text(strip=True) for element in question_elements]

# Write questions to a file
with open('questions.txt', 'w', encoding='utf-8') as file:
    for i, question in enumerate(questions, start=1):
        file.write(f"Question {i}: {question}\n")