flickr-random
========

## Introduction ##

Uses the Flickr API to save one random photo a month for a given year and username. I wrote this to use with my blog, thinking it would be fun to write a "year in review" post with pictures that were randomly selected.

## Getting Started ##

1. Clone the repo
2. In a Python virtualenv, install dependencies: pip install -r requirements.txt
3. Create a config.py in the main project folder (use sample_config.py as a template)

## Usage ##
From the main project folder, run the script: python random_photos.py

## Output ##
The script will write up to 12 photos to the folder specified in config.py (one for each month in the designated year).


