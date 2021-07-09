import json
import re
import gzip

import factory.models.collection_models as collection_models
import factory.models.regex_patterns as patterns

# Pulled from the source JSON
def GenerateTotalCardCount(_loadedCardSet):

    TotalCardCount = _loadedCardSet["total_cards"]

    return TotalCardCount

# Color Combinations can be from 1-5 characters in length.
def GenerateCardColorCombination(_loadedCard):
    
    CardColorCombination = ""

    # printing out the details to troubleshoot issues related to a missing key for card colors.
    # Not all cards have a color, modal cards don't appear to have a color listed as a key returned by the scryfall api.
    
    if _loadedCard.get("colors") != None:
        for color in _loadedCard["colors"]:
                CardColorCombination = CardColorCombination + (color)

    else:
        CardColorCombination = ""

    CardColorCombinationEntry = [CardColorCombination, _loadedCard["id"]]
    
    return CardColorCombinationEntry

# Generates a list of cards with a color combination abbreviations
def GenerateCardsByColorCombinationRaw(_loadedCards):

    ColorCombinationDictionaryRaw = {}

    for card in _loadedCards["data"]:

        Entry = GenerateCardColorCombination(_loadedCard=card)


        colorKey = str(Entry[0])
        cardId = str(Entry[1])

        if colorKey in ColorCombinationDictionaryRaw.keys():
            ColorCombinationDictionaryRaw[colorKey].append(cardId)
        else:
            ColorCombinationDictionaryRaw[colorKey] = []
            ColorCombinationDictionaryRaw[colorKey].append(cardId)

    return ColorCombinationDictionaryRaw

# Generates a sorted list of cards by their matching color combination names to matching combinations
# Ex: Red White = RW or Black Red Green = BRG
# Because we can't really control the formation of the colors array 
# in the source json from scryfall we are going to try and use regex here.
def GenerateCardsByColorCombination(_processedColorCombinationDictionary):

    GenerateCardsByColorCombinationDictionary = {}


    colorPatternKeys = patterns.ColorRegexPatterns.keys()
    processedPattern = _processedColorCombinationDictionary.keys()

    for pattern in colorPatternKeys:
        p = re.compile(patterns.ColorRegexPatterns[pattern], re.IGNORECASE)

        for processedCombo in processedPattern:
            if p.match(processedCombo):
                entry = _processedColorCombinationDictionary.get(processedCombo)
                GenerateCardsByColorCombinationDictionary[pattern] = entry

    return GenerateCardsByColorCombinationDictionary

# Loads the source json set file that has been downloaded from scryfall.
def LoadDownloadedJson(_jsonPath):

    LoadedJson = open(_jsonPath, "r").read()
    LoadedJson = json.loads(LoadedJson)

    return LoadedJson

# Saves a compressed version of an incoming json file.
# Planned use is to save processed models and source json into a compressed format.
def GZIPDownloadedJson(_incomingJsonPath):
    try:
        incomingJson = open(_incomingJsonPath, "rb")
        compressedFile = gzip.open("compressed.json.gzip", "wb") 

        compressedFile.writelines(incomingJson)
        
        compressedFile.close()
        incomingJson.close()

        CompletionMessage = "Saving compressed file completed successfully."
    except():
        CompletionMessage = "Saving a compressed file failed"
    return CompletionMessage

# Opens a json.gzip file for parsing data.
def ExpandGZIPJson(_incomingGzipPath):
    try:
        compressedFile = gzip.open(_incomingGzipPath, "r") 

        readFile = compressedFile.read()
        
        compressedFile.close()

        CompletionMessage = "Opening compressed file completed successfully."

    except():
        CompletionMessage = "Opening the compressed file failed."
        readFile = None

    return [CompletionMessage, readFile]

# Converts an expanded json.gzip file into a dictionary.
def LoadExpandedGZIPJson(_incomingJson):
    ExpandedGZIPDictionary = json.loads(_incomingJson[1])
    return ExpandedGZIPDictionary

# Builds the final collection stats model for saving an later distribution.
def BuildCollectionStats(_loadedJson):
    CompleatedCollectionStatsModel = collection_models.CollectionStatsModel
    return CompleatedCollectionStatsModel

# print(
#     json.dumps(
#         GenerateCardsByColorCombination(
#             _processedColorCombinationDictionary=GenerateCardsByColorCombinationRaw(
#                 _loadedCards=LoadDownloadedJson(_jsonPath="C:\\Users\\jeffrey.moody\\Documents\\GitHub\\etb\\exportJSON.json")
#             )
#         ), indent=4
#     )
# )

# GZIPDownloadedJson(_incomingJsonPath="C:\\Users\\jeffrey.moody\\Documents\\GitHub\\etb\\exportJSON.json")
# print(json.dumps(json.loads(ExpandGZIPJson(_incomingGzipPath="C:\\Users\\jeffrey.moody\\Documents\\GitHub\\etb\\compressed.json.gzip")[1]), indent=4))