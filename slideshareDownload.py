''' This program downloads all the slides from given slideshare link
    in the folder specified.'''

from PIL import Image
from requests import get
from cStringIO import StringIO
from bs4 import BeautifulSoup as bs
import os


# The url of slideshare presentation.
slide_url="http://www.slideshare.net/ubernostrum/django-in-depth"
# Get the name of slide presentation
name=" ".join(slide_url.split('/')[-1].split('-')).capitalize()
# Path where the slides are to be saved
path="F:\\%s\\" % name

if not os.path.exists(path):
    os.makedirs(path)

def save(url):
    r=get(url)
    im=Image.open(StringIO(r.content))
    im.save(path+str(current)+".jpg")
    #i.show()   # Shows the image after download


r=get(slide_url)
soup=bs(r.text, "html.parser")

def check(tag):
    return tag.parent.name=='section' and tag['class']==['slide_image']

slides=soup.find_all(check)
start=1  # Which slide to start
print "Total number of slides - %d" % len(slides)
for current in range(start, len(slides)+1):
    slide=slides[current-1]  # reason zero-indexing
    print "Downloading slide number - %d" % current

    # Chose quality of images
    url=slide['data-full']
    #url=slide['data-normal']
    #url=slide['data-small']
    try:
        save(url)
    except:
        try:
            save(url)
        except Exception as e:
            print "Some problem with slide number - %d" % current
            print "Error msg - ", str(e)
print "Finished Downloading. Keep Smiling .:-)"
