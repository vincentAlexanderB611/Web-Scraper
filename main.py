import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage
url = 'https://uk.finance.yahoo.com/news/trending-tickers-virgin-money-rentokil-aviva-itv-123126806.html'

# Set custom headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'
}

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the title of the webpage
        title = soup.title.text

        # Print the title
        print("Title:", title)
    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", e)
