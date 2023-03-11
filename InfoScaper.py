import requests
import re
from bs4 import BeautifulSoup

# Get the target URL from the user
url = input("Enter the URL to extract contact information from: ")

# Fetch the HTML content of the page
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract relevant elements such as anchor tags, paragraphs, and lists
text_elements = soup.find_all(['a', 'p', 'li'])

# Apply regular expressions to the extracted text to identify patterns of contact information
phone_numbers = set()
emails = set()
social_media_handles = set()

for text_element in text_elements:
    # Extract phone numbers with country dial codes
    phone_number_matches = re.findall(r'\+(?:\d[- ]*){9,}\d', str(text_element))
    for phone_number_match in phone_number_matches:
        phone_numbers.add(phone_number_match)

    # Extract email addresses based on .gmail.com
    email_matches = re.findall(r'\b[A-Za-z0-9._%+-]+@gmail\.com\b', str(text_element))
    for email_match in email_matches:
        emails.add(email_match)

    # Extract social media handles with any social links
    social_media_matches = re.findall(r'(?i)\b((?:https?:\/\/|www\.)(?:instagram|facebook|twitter)\.com\/\S+)\b', str(text_element))
    for social_media_match in social_media_matches:
        social_media_handles.add(social_media_match)

# Print the extracted contact information
print("Phone Numbers: ", phone_numbers)
print("Emails: ", emails)
print("Social Media Handles: ", social_media_handles)
