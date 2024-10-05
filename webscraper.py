import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL you want to scrape
url = 'https://example.com'  # Replace with the target website

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the data you want to scrape
    # This example assumes we're looking for articles with a title and a link
    articles = soup.find_all('article')  # Adjust the selector based on the website structure

    # Create lists to hold the extracted data
    titles = []
    links = []

    for article in articles:
        title = article.find('h2').text.strip()  # Adjust based on actual HTML structure
        link = article.find('a')['href']  # Adjust based on actual HTML structure

        titles.append(title)
        links.append(link)

    # Create a DataFrame to organize the data
    df = pd.DataFrame({
        'Title': titles,
        'Link': links
    })

    # Save the DataFrame to a CSV file
    df.to_csv('scraped_data.csv', index=False)

    print("Data scraped and saved to scraped_data.csv")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")