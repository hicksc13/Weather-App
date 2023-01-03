# Importing required modules
import requests as req
import os, bs4
  
# Storing website URL
url = 'https://xkcd.com/'
# Make Directory to store image
os.makedirs('xkcd', exist_ok=True)
# exist_ok prevent program from throwing an exception if the folder existed
  
# Append the user comic number in the url
for n in range(1,2707):
    starturl = url
    url += str(n)
    print('Downloading image from %s...' % url)
    # Request the url from the web
    res = req.get(url)
  
    # Now Store the HTML page that is found in the url
    soup = bs4.BeautifulSoup(res.text)
  
    # Find the Element that contain the image tag
    comicElem = soup.select('#comic img')
  
    # Now get that source of the image and make it as a url
    comicUrl = 'http:' + comicElem[0].get('src')
  
    # Request the url from the web
    res = req.get(comicUrl)
  
    # Save the file in the directory
    # wd means it is open for writing in binary mode
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(1):
        # Writing the binary image file
        imageFile.write(chunk)
    # Closing the binary image file
    imageFile.close()
    print('Successfully downloaded')
    url = starturl
    