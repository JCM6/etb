import json
import factory.models.collection_models
import factory.models.regex_patterns


def GenerateTotalCardCount(_loadedCardSet):
    TotalCardCount = _loadedCardSet["total_cards"]
    return TotalCardCount

# Color Combinations can be from 1-5 characters in length.
def GenerateCardColorCombination(_loadedCard):
    
    CardColorCombination = ""

    # printing out the details to troubleshoot issues related to a missing key for card colors.
    # Not all cards have a color, modal cards don't appear to have a color listed as a key returned by the scryfall api.
    
    if _loadedCard.get("colors") != None:
        #print(_loadedCard["id"], " : ", _loadedCard["name"], " : ", _loadedCard["colors"])
        for color in _loadedCard["colors"]:
                CardColorCombination = CardColorCombination + (color)

    else:
        #print(_loadedCard["id"], " : ", _loadedCard["name"], " : ", None)
        CardColorCombination = ""

    CardColorCombinationEntry = [CardColorCombination, _loadedCard["id"]]
    
    return CardColorCombinationEntry



# Generates a sorted list of cards by their matching color combination abbreviations
# Ex: Red White = RW or Black Red Green = BRG
# Because we can't really control the formation of the colors array in the source json from scryfall we are going to try and use regex here.

def GenerateCardsByColorCombination(_loadedCards):
    ColorCombinationDictionary = {}
    IdList = []
    for card in _loadedCards["data"]:
        Entry = GenerateCardColorCombination(_loadedCard=card)
        IdList.append(Entry[1])
        #print(Entry)
        colorKey = str(Entry[0])
        cardId = str(Entry[1])
        if colorKey in ColorCombinationDictionary.keys():
            ColorCombinationDictionary[colorKey].append(cardId)
        else:
            ColorCombinationDictionary[colorKey] = []
            ColorCombinationDictionary[colorKey].append(cardId)
    return ColorCombinationDictionary

def LoadDownloadedJson(_jsonPath):
    LoadedJson = open(_jsonPath, "r").read()
    LoadedJson = json.loads(LoadedJson)
    return LoadedJson

def ProcessDownloadedJson(_loadedJson):
    CompleatedCollectionStatsModel = CollectionStatsModel
    return CompleatedCollectionStatsModel

print(json.dumps(GenerateCardsByColorCombination(_loadedCards=LoadDownloadedJson(_jsonPath="C:\\Users\\jeffrey.moody\\Documents\\GitHub\\etb\\exportJSON.json")), indent=4))
