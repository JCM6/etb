import requests, json, shutil
import feedparser

if __name__ == "__main__":
    url = "https://backend.deviantart.com/rss.xml?type=deviation&q=by%3Afredstackle+sort%3Atime+meta%3Aall"
    response = requests.get(url)
    textResponse = response.text
    parsedFeed = feedparser.parse(textResponse)
    print(json.dumps(parsedFeed["entries"][2]["media_content"][0]["url"], indent=4))
    print(parsedFeed.keys())

    imageUrl = parsedFeed["entries"][2]["media_content"][0]["url"]

    image = requests.get(url=imageUrl, stream=True)
    
    imageFile = open("deviantArt_demo.jpg", "wb")

    imageFile.write(image.content)
    
    imageFile.close()
    