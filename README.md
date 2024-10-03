# Billboard Top 100 Spotify Playlist Creator

This Python project allows users to create a Spotify playlist of the Billboard Top 100 songs from a specific date using web scraping and the Spotify API. Users can input a date (in `YYYY-MM-DD` format), and the program will fetch the Billboard Hot 100 chart for that day and automatically create a Spotify playlist with those songs.

## Features

- **Billboard Scraper**: Scrapes Billboard's Hot 100 chart for a given date.
- **Spotify Integration**: Uses the Spotify API to create a public playlist on the user's account.
- **Playlist Creation**: Automatically adds songs from the Billboard Hot 100 to a new Spotify playlist.

## How It Works

1. The user inputs a date (in `YYYY-MM-DD` format) for which they want to retrieve the Billboard Hot 100 chart.
2. The program scrapes the Billboard website to extract the top 100 songs for that date.
3. The program searches for each song on Spotify using the Spotify API.
4. A new playlist is created on the user's Spotify account, containing the top 100 songs.

## Prerequisites

To run this project, you’ll need the following:

- **Python 3.x**
- **Spotify Account**: You will need a Spotify Developer Account and credentials (Client ID and Client Secret).
- **Required Libraries**:
  - `requests`: To fetch data from the Billboard website.
  - `beautifulsoup4`: For web scraping the Billboard website.
  - `spotipy`: For interacting with the Spotify API.
  
You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 spotipy
