# Python URL Shortener

A simple URL Shortener project built with Python.

## Features

- Generate short URLs from long URLs
- Retrieve the original URL using the short URL
- Prevent duplicate short URLs for the same original URL
- Handle URL collisions by generating a new unique code
- Fast dictionary-based lookups (O(1) average)

## Technologies

- Python 3
- Dictionaries (Hash Maps)
- Random Module
- String Module

## How It Works

1. User provides a long URL.
2. The program generates an 8-character random identifier.
3. A short URL is created using the base URL.
4. Two dictionaries store mappings:
   - Long URL → Short URL
   - Short URL → Long URL
5. Users can retrieve the original URL at any time using the short URL.

## Example Output

```
Original URL:
https://www.example.com

Short URL:
http://short.url/Ab12Cd34

Retrieved URL:
https://www.example.com
```

## Future Improvements

- Flask or FastAPI web interface
- SQLite/MySQL/PostgreSQL database integration
- Custom aliases
- URL expiration
- Click analytics
- QR code generation
- User authentication
- REST API
- Docker support

