import string
import random

# Initialization:
url_short = {}
short_to_long_url = {}
base_url = "http://short.url/"
short_length = 8

# Function which will generate a random string:
generating_random_string = lambda length: ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function which will generate a short URL:
def creating_shorturl(original_url):
    if original_url in url_short:
        return url_short[original_url]

    # Generating a new short URL
    short_url = base_url + generating_random_string(short_length)
    while short_url in short_to_long_url:
        short_url = base_url + generating_random_string(short_length)

    url_short[original_url] = short_url
    short_to_long_url[short_url] = original_url
    return short_url

# Function which will retrieve the original URL from a short URL:
def retrieved_original_url(short_url):
    return short_to_long_url.get(short_url, None)

# Example
original_url = "https://www.example.com"
short_url = creating_shorturl(original_url)

print(f"Short URL for {original_url} will be {short_url}")

# Retrieving the original URL:
retrieving_url = retrieved_original_url(short_url)
print(f"Original URL for {short_url} will be {retrieving_url}")
