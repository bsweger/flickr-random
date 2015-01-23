flickr-random
========

## Introduction ##

Uses the Flickr API to save one random photo a month for a given year and username. I wrote this to use with my blog, thinking it would be fun to write a "year in review" post with pictures that were randomly selected.

## Getting Started ##
**Requirements:**

Python 2.x

1. Clone the repo
2. Install dependencies:
        pip install -r requirements.txt
3. Create the directory that will hold the downloaded photos, if it doesn't already exist
3. Create a config.py in the main project folder, using __sample_config.py__ as a template:
        cp sample_config.py config.py
4. Edit config.py: specify your Flickr API key and the directory where the photos will be saved

## Usage ##
From the main project folder, run the script: python random_photos.py

## Output ##
The script will write up to 12 photos to the folder specified in config.py (one for each month in the designated year).

##License
MIT License

