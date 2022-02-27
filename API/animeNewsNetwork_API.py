import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
from PIL import Image 


while True:
    # API returns a XML data format
    serviceUrl = "https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime="
    animeID = input("Enter an anime ID(type #exit to exit) = ")
    if animeID == '#exit':
        break
    #appends the user input into the url 
    serviceUrl = serviceUrl + animeID

    handle = urllib.request.urlopen(serviceUrl)
    data = handle.read().decode()

    print("retrieving ",serviceUrl)
    print("Retrieved",len(data), "characters")

    #tree will contain the XML tree given by the API
    tree = ET.fromstring(data)
    
    #try-except to check if the API finds the anime ID and returns valid data
    try:
        print("Title: ",tree.find('anime').get('name'))
    except:
        print(tree.find('warning').text)
        continue 
    img = Image.open(urllib.request.urlopen(tree.find('anime').find('info').get('src')))
    img.show()
    print("Plot Summary:",tree.find('.//info[@type="Plot Summary"]').text)

