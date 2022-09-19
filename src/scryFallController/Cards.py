import requests, json, uuid

# Example response object
"""{
    "object": "card",
    "id": "fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6",
    "oracle_id": "56719f6a-1a6c-4c0a-8d21-18f7d7350b68",
    "multiverse_ids": [
        571092
    ],
    "tcgplayer_id": 272719,
    "cardmarket_id": 658554,
    "name": "Swamp",
    "lang": "en",
    "released_at": "2022-06-10",
    "uri": "https://api.scryfall.com/cards/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6",
    "scryfall_uri": "https://scryfall.com/card/clb/459/swamp?utm_source=api",
    "layout": "normal",
    "highres_image": false,
    "image_status": "lowres",
    "image_uris": {
        "small": "https://c1.scryfall.com/file/scryfall-cards/small/front/f/c/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6.jpg?1652827096",
        "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/f/c/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6.jpg?1652827096",
        "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/f/c/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6.jpg?1652827096",
        "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/f/c/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6.png?1652827096",
        "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/f/c/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6.jpg?1652827096",     
        "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/f/c/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6.jpg?1652827096"
    },
    "mana_cost": "",
    "cmc": 0.0,
    "type_line": "Basic Land \u2014 Swamp",
    "oracle_text": "({T}: Add {B}.)",
    "colors": [],
    "color_identity": [
        "B"
    ],
    "keywords": [],
    "produced_mana": [
        "B"
    ],
    "legalities": {
        "standard": "legal",
        "future": "legal",
        "historic": "legal",
        "gladiator": "legal",
        "pioneer": "legal",
        "explorer": "legal",
        "modern": "legal",
        "legacy": "legal",
        "pauper": "legal",
        "vintage": "legal",
        "penny": "legal",
        "commander": "legal",
        "brawl": "legal",
        "historicbrawl": "legal",
        "alchemy": "legal",
        "paupercommander": "legal",
        "duel": "legal",
        "oldschool": "not_legal",
        "premodern": "legal"
    },
    "games": [
        "paper"
    ],
    "reserved": false,
    "foil": true,
    "nonfoil": true,
    "finishes": [
        "nonfoil",
        "foil"
    ],
    "oversized": false,
    "promo": false,
    "reprint": true,
    "variation": false,
    "set_id": "5e4c3fe8-fd57-4b20-ad56-c03790a16cea",
    "set": "clb",
    "set_name": "Commander Legends: Battle for Baldur's Gate",
    "set_type": "draft_innovation",
    "set_uri": "https://api.scryfall.com/sets/5e4c3fe8-fd57-4b20-ad56-c03790a16cea",
    "set_search_uri": "https://api.scryfall.com/cards/search?order=set&q=e%3Aclb&unique=prints",
    "scryfall_set_uri": "https://scryfall.com/sets/clb?utm_source=api",
    "rulings_uri": "https://api.scryfall.com/cards/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6/rulings",
    "prints_search_uri": "https://api.scryfall.com/cards/search?order=released&q=oracleid%3A56719f6a-1a6c-4c0a-8d21-18f7d7350b68&unique=prints",
    "collector_number": "459",
    "rarity": "common",
    "flavor_text": "Now that you've clearly hit the \"marsh\" part of Lizard Marsh, you begin to worry about the \"lizard\" part.",
    "card_back_id": "0aeebaf5-8c7d-4636-9e82-8c27447861f7",
    "artist": "Piotr Dura",
    "artist_ids": [
        "aff176e8-1d15-432e-ad1d-207a474decba"
    ],
    "illustration_id": "ed2040bb-08df-487d-89b5-18a017f2776a",
    "border_color": "black",
    "frame": "2015",
    "full_art": false,
    "textless": false,
    "booster": false,
    "story_spotlight": false,
    "prices": {
        "usd": "0.05",
        "usd_foil": "0.08",
        "usd_etched": null,
        "eur": "0.06",
        "eur_foil": "0.15",
        "tix": null
    },
    "related_uris": {
        "gatherer": "https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=571092",
        "tcgplayer_infinite_articles": "https://infinite.tcgplayer.com/search?contentMode=article&game=magic&partner=scryfall&q=Swamp&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "tcgplayer_infinite_decks": "https://infinite.tcgplayer.com/search?contentMode=deck&game=magic&partner=scryfall&q=Swamp&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "edhrec": "https://edhrec.com/route/?cc=Swamp"
    },
    "purchase_uris": {
        "tcgplayer": "https://www.tcgplayer.com/product/272719?page=1&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "cardmarket": "https://www.cardmarket.com/en/Magic/Products/Search?referrer=scryfall&searchString=Swamp&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall",
        "cardhoarder": "https://www.cardhoarder.com/cards?affiliate_id=scryfall&data%5Bsearch%5D=Swamp&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"
    }
}"""

# Example filtered card dictionary
"""{
    "id": "fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6",
    "name": "Swamp",
    "released_at": "2022-06-10",
    "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/f/c/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6.jpg?1652827096", 
    "type_line": "Basic Land \u2014 Swamp",
    "oracle_text": "({T}: Add {B}.)",
    "color_identity": [
        "B"
    ],
    "set": "clb",
    "set_name": "Commander Legends: Battle for Baldur's Gate",
    "flavor_text": "Now that you've clearly hit the \"marsh\" part of Lizard Marsh, you begin to worry about the \"lizard\" part.",
    "artist": "Piotr Dura",
    "full_art": false
}"""

# Example CSV headers, some have been removed
"""['directory', 'filename', 'id', 'name', 'released_at', 'art_crop', 'type_line', 'oracle_text', 'color_identity', 'set', 'set_name', 'flavor_text', 'artist', 'full_art']"""


def GetCardUniquePrintsByName(cardName):

    url = f"https://api.scryfall.com/cards/search?q=%21%22{str(cardName)}%22+include%3Aextras&unique=prints"


    headers = {
        'Content-Type': 'application/json',
        'Content-Encoding':'utf-16'
    }

    response = requests.get(url=url, headers=headers)
    
    cardsArray = json.loads(response.content.decode('utf-8'))["data"]

    return cardsArray

def GetCardUniquePrintsByType(_type):

    url = f"https://api.scryfall.com/cards/search?q=type%3A{str(_type)}+legal%3Acommander+include%3Aextras&unique=prints"

    headers = {
        'Content-Type': 'application/json',
        'Content-Encoding':'utf-16'
    }
    response = requests.get(url=url, headers=headers)
    
    cardsArray = json.loads(response.content.decode('utf-8'))["data"]
    return cardsArray

def GetCardFromArray(index, cardArray):
    
    card = cardArray[index]
    
    return card 

def BuildFinalizedCardArray(filteredCards):
    
    finalizedCardArray = []
    
    for card in filteredCards:

        filename = card["image_uris"]["art_crop"].split('/')[-1].split('?')[0]

        cardDetail = {
            'directory': "src\\scryfall_artcrops\\" + filename,
            'filename':filename,
            'id':card["id"],
            'name':card["name"],
            'released_at':card["released_at"],
            'art_crop':card["image_uris"]["art_crop"],
            'type_line':card["type_line"],
            'oracle_text':card["oracle_text"],
            'color_identity':card["color_identity"],
            'set':card["set"],
            'set_name':card["set_name"],
            'artist':card["artist"],
            'full_art':card["full_art"]
        }

        # Check to add the flavor text value as this is a relatively new addition to basic lands.
        if 'flavor_text' in card.keys():
            cardDetail['flavor_text'] = card["flavor_text"]
    
        finalizedCardArray.append(cardDetail)
    
    return finalizedCardArray

# We only want cards that have an art crop
def FilterResultsToArtCropOnly(cardArray, testing):

    filteredCardsArray = []

    for card in cardArray:
        
        if testing == True:
            print(json.dumps(card, indent=4), '\n')
            print(card["layout"])

        # Check to see if the card has an art crop uri, not all cards do
        # It is possible for a card object to have multiple keys associated due to the existence of modal faced cards.
        # This means that I need to find a way to iterate through those and store each card face as it's own instance.
        # I will be leaving art instances for those in as they are technically land type cards even though one card face may not be a land.
        # EX: Agadeem's Awakening //  Agadeem, the Undercrypt

        if '//' not in str(card['type_line']):
            if "art_crop" in str(card["image_uris"].keys()):
                    filteredCardsArray.append(card)
                
    return filteredCardsArray

# This should work for basic lands as their oracle text fields should not cause issues when parsing into a US standard CSV file.
def BuildCSVTags(finalizedCardDictionary, fileNamePrefix):

    csvText = "directory, filename, id, name, released_at, art_crop, type_line, oracle_text, color_identity, set, set_name, artist, full_art\n"
    
    # This needs to be set to utf-16 as there are character encodings used that are not covered by utf-8, namely hyphens otherwise known as u2014
    csvFile = open(f'{fileNamePrefix}_csvFile.csv', 'w', encoding='utf-16')

    csvFile.writelines(csvText)

    for card in finalizedCardDictionary:

        csvFile.writelines(f"{card['directory']}, {card['filename']}, {card['id']},  {card['name']}, {card['released_at']}, {card['art_crop']}, {card['type_line']}, {card['oracle_text']}, {card['color_identity']}, {card['set']}, {card['set_name']}, {card['artist']}, {card['full_art']}\n")

    csvFile.close()

    return

# Building a differently delimited file for the nonbasics since they are a bit more complicated and comma separated values may be too simplistic.
# I think the best route is to use this method for now and consolidate on the usage of one function call.
# This one is set to a custom delimiter: |
def BuildCustSV(finalizedCardDictionary, fileNamePrefix):

    # Some nonbasic lands have linebreak characters that we need to remove to ensure that the correct values are added to the corresponding tag values.
    returnChar = "\n"

    csvText = "directory|filename|id|name|released_at|art_crop|type_line|oracle_text|color_identityset|set_name|artist|full_art\n"
    
    # This needs to be set to utf-16 as there are character encodings used that are not covered by utf-8, namely hyphens otherwise known as u2014
    csvFile = open(f'{fileNamePrefix}_csvFile.csv', 'w', encoding='utf-16')

    csvFile.writelines(csvText)

    for card in finalizedCardDictionary:

        csvFile.writelines(f"{card['directory']}|{card['filename']}|{card['id']}|{card['name']}|{card['released_at']}|{card['art_crop']}|{card['type_line']}|{card['oracle_text'].replace(returnChar, ' ')}|{card['color_identity']}|{card['set']}|{card['set_name']}|{card['artist']}|{card['full_art']}\n")

    csvFile.close()

    return

def DisplayResults(cards, fCards, finalizedCardDictionary):

    print("TotalCountReturned: ", len(cards),'\n')

    print("ExampleCardReturned: ", cards[0],'\n')

    print("TotalCountReturned: ", len(fCards),'\n')

    print("FilteredCardsExample: ", fCards[0],'\n')

    print("Final Results: ", finalizedCardDictionary[0],'\n')

    print("TotalCountReturned: ", len(finalizedCardDictionary),'\n')

    return

def SaveImageFiles(finalizedCardArray, testing):
    
    for card in finalizedCardArray:
        
        # this grabs the last item in the array 
        # in theory it should look like this: ['https://c1.scryfall.com/file/scryfall-cards/art_crop/front/4/9/', ['4945031e-1158-474c-9e50-1ec817acc767.jpg', '?1562908368']]

        url = card['art_crop']

        filename = url.split('/')[-1].split('?')[0]

        directory = 'src\\scryfall_artcrops\\'

        if testing == True:
            print(filename)

        response = requests.get(url)
        
        f = open(directory + filename, 'wb')

        f.write(response.content)
    
    return

if __name__ == "__main__":
    testdiction = {
        "id": "fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6",
        "name": "Swamp",
        "released_at": "2022-06-10",
        "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/f/c/fc4111be-6dae-4ca5-bd58-c1ce7cfa9cf6.jpg?1652827096", 
        "type_line": "Basic Land \u2014 Swamp",
        "oracle_text": "({T}: Add {B}.)",
        "color_identity": [
            "B"
        ],
        "set": "clb",
        "set_name": "Commander Legends: Battle for Baldur's Gate",
        "flavor_text": "Now that you've clearly hit the \"marsh\" part of Lizard Marsh, you begin to worry about the \"lizard\" part.",
        "artist": "Piotr Dura",
        "full_art": False
    }
    
    searchTerms = ['Plains', 'Island', 'Swamp', 'Mountain', 'Forest', 'land']
    downloadImages = False

    if 1 == 1:
            
        test = "Mountain"

        cards = GetCardUniquePrintsByName(cardName=test)

        filteredCards = FilterResultsToArtCropOnly(cardArray=cards, testing=False)
            
        finalizedCardArray = BuildFinalizedCardArray(filteredCards=filteredCards)

        DisplayResults(cards=cards, fCards=filteredCards, finalizedCardDictionary=finalizedCardArray)

        if downloadImages == True:
            
            SaveImageFiles(finalizedCardArray=finalizedCardArray, testing=True)

        BuildCustSV(finalizedCardDictionary=finalizedCardArray, fileNamePrefix=test)

    else:
        searchTerm = 'land'

        res = GetCardUniquePrintsByType(_type=searchTerm)

        filteredCards = FilterResultsToArtCropOnly(cardArray=res, testing=False)
            
        finalizedCardArray = BuildFinalizedCardArray(filteredCards=filteredCards)

        DisplayResults(cards=res, fCards=filteredCards, finalizedCardDictionary=finalizedCardArray)
        
        if downloadImages == True:
            
            SaveImageFiles(finalizedCardArray=finalizedCardArray, testing=True)

        BuildCustSV(finalizedCardDictionary=finalizedCardArray, fileNamePrefix=searchTerm)

# Putting this detail here as I am going to write a function to unify this process for all desired assets.
# Hopefully this will make this process easier to run, but I may not need to since this liekly won't be revisted once it is completed.
# Flow Outline:
"""
1. Call Scryfall
2. Build a Python Dictionary with the needed values for tags.
3. Save the corresponding art crops.
4. Build the csv.
5. Remove duplicate Image ids. (I expect this as we will likely see duplicates of the basic lands.)
"""