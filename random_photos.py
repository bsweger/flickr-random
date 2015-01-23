from random import randrange
import urllib2
import json
import calendar
from datetime import datetime
import flickrapi
import config

def get_random_photo(flickrid, year, month, sort=''):
    #get the photos
    first = datetime(year, month, 1)
    first = calendar.timegm(first.utctimetuple())
    last = datetime(year, month, calendar.monthrange(year, month)[1])
    last = calendar.timegm(last.utctimetuple())
    month_name = calendar.month_name[month]
    
    search = flickr.photos_search(
        user_id = flickrid,
        min_taken_date = first,
        max_taken_date = last,
        sort = sort,
        format='json',
        nojsoncallback=1,
        per_page = 500
        )
    parsed = json.loads(search)

    if parsed['stat'] == 'ok':
        photos = parsed['photos']
    else:
        print 'Bad Flickr call. Status is %s' % parsed['stat']
        return

    photos_total = int(photos['total'])
    if photos_total < 1:
        print 'No photos found for %s %s.' % (month_name, year)
        return
    #to keep things simple, we're not paging,
    #so limit random photo selection to those on the
    #first page of results
    elif photos_total > 501:
        photos_total = 501

    #select a random photo from the returned list & save it
    photo_rand = randrange(0, int(photos['total']))
    pic = photos['photo'][photo_rand]
    
    #get url for the photo's original size
    sizes = flickr.photos_getSizes(
        photo_id=pic['id'],
        format='json',
        nojsoncallback=1)
    parsed_sizes = json.loads(sizes)
    if parsed_sizes['stat'] == 'ok':
        s = parsed_sizes['sizes']['size']
        url = ''
        for idx, value in enumerate(s):
            if 'Original' in value['label']:
                url = value['source']
        if not len(url):
            print 'Unable to find URL for %s %s. Photo id = %s.' % (month, year, pic['id'])
    else:
        print 'Bad flickr call for photo sizes. Status is %s' % parsed_sizes['stat']

    #retrieve and save photo
    f = urllib2.urlopen(url)
    if f.code == 200:
        file = '%s/%s%s.jpg' % (config.photo_folder, month_name.lower(), year)
        with open(file, 'wb') as image:
            image.write(f.read())
        print 'Saved %s' % file
    else:
        print 'Error retrieving photo from %s' % url
        return

api_key = config.flickr_api_key
flickr = flickrapi.FlickrAPI(api_key)
id = flickr.people_findbyusername(username=config.username)
flickrid = id[0].attrib['id']

year = config.year
for x in range(1,13):
    get_random_photo(
        flickrid,
        year=year,
        month = x,
        sort='interestingness-desc')
