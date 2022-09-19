import json
import re
import gzip

import factory.models.collection_models as collection_models
import factory.models.regex_patterns as patterns
import factory.datadownloader as datadownloader
import factory.datauploader as uploader

StatsModel = collection_models.CollectionStatsModel()

## Color Combination Functions ##
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

# Generates a list of cards with a color combination abbreviations.
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




## Color Identity Functions ##
# Get a card's color identity.
def GenerateCardColorIdentityAggregate(_loadedCard):
    CardColorIdentityAggregate = ""

    # Not all cards have a color identity.
    
    if _loadedCard.get("color_identity") != None:
        for color in _loadedCard["color_identity"]:
                CardColorIdentityAggregate = CardColorIdentityAggregate + (color)
    else:
        CardColorIdentityAggregate = ""

    CardColorCombinationEntry = [CardColorIdentityAggregate, _loadedCard["id"]]
    return CardColorCombinationEntry

# Generate a list of cards with color identity abbreviations.
def GenerateCardsColorIdentityAggregate(_loadedCards):

    CardColorIdentityAggregateDictionaryRaw = {}
    for card in _loadedCards["data"]:

        Entry = GenerateCardColorIdentityAggregate(_loadedCard=card)

        colorKey = str(Entry[0])
        cardId = str(Entry[1])

        if colorKey in CardColorIdentityAggregateDictionaryRaw.keys():
            CardColorIdentityAggregateDictionaryRaw[colorKey].append(cardId)
        else:
            CardColorIdentityAggregateDictionaryRaw[colorKey] = []
            CardColorIdentityAggregateDictionaryRaw[colorKey].append(cardId)

    return CardColorIdentityAggregateDictionaryRaw

# Generates a sorted list of cards by matchin color identity names.
def GenerateCardColorIdentityAggregates(_processedCardColorIdentityAggregatesDictionary):

    GeneratedCardColorIdentityAggregatesDictionary = {}


    colorPatternKeys = patterns.ColorRegexPatterns.keys()
    processedPattern = _processedCardColorIdentityAggregatesDictionary.keys()

    for pattern in colorPatternKeys:
        p = re.compile(patterns.ColorRegexPatterns[pattern], re.IGNORECASE)

        for processedCombo in processedPattern:
            if p.match(processedCombo):
                entry = _processedCardColorIdentityAggregatesDictionary.get(processedCombo)
                GeneratedCardColorIdentityAggregatesDictionary[pattern] = entry

    return GeneratedCardColorIdentityAggregatesDictionary

## Cards by Cost Functions
# Functions are used to generate the aggregates of cards by cost.

# Create Card by Cost Entry
def GenerateCardCostEntry(_loadedCard):
    if  _loadedCard.get("mana_cost"):
        CardCostEntry = [_loadedCard["id"], _loadedCard["mana_cost"]]
    else:
        CardCostEntry = [_loadedCard["id"], "NoCost"]

    return CardCostEntry

def GenerateCardCostAggregate(_loadedCards):
    CardCostAggregateDictionary = {}
    # build the keys
    for card in _loadedCards["data"]:
        entry = GenerateCardCostEntry(_loadedCard=card)
        CardCostAggregateDictionary[entry[1]] = []
    # populate the values... gross?
    for card in _loadedCards["data"]:
        entry = GenerateCardCostEntry(_loadedCard=card)
        CardCostAggregateDictionary[str(entry[1])].append(entry[0])
    return CardCostAggregateDictionary


## CMV Functions ##
# Functions listed are used to generate the aggregate data for the CMV (perviously CMC values)

# Create CMV Entry
def GenerateCardCMVEntry(_loadedCard):
        CardCMVEntry = [_loadedCard["id"], _loadedCard["cmc"]]
        return CardCMVEntry

## Create CMV Aggregate
def GenerateCardCMVAggregate(_loadedCards):

    # There is likely a better way to do this, but right now this is what I think will prevent weird exceptions.
    statsmodel = StatsModel
    CardCMVAggregateDictionary = statsmodel.CardsByCMV
    for card in _loadedCards["data"]:
        entry = GenerateCardCMVEntry(_loadedCard=card)
        if int(entry[1]) >= 16:
            CardCMVAggregateDictionary["16+"].append(entry[0])
        else:
            # Need to make sure this an int due to "un"-sets
            CardCMVAggregateDictionary[str(int(entry[1]))].append(entry[0])

    return CardCMVAggregateDictionary



## CardsByType Functions
# Groups cards by types

def GenerateCardsByType(_loadedCard):
    CardsByTypeEntry = [_loadedCard["id"], _loadedCard["type_line"]]
    return CardsByTypeEntry

def GenerateCardsByTypeAggregate(_loadedCards):
    CardsByTypeAggregate = StatsModel.CardsByType
    for card in _loadedCards["data"]:
        entry = GenerateCardsByType(card)
        if CardsByTypeAggregate.get(entry[1]) != None:
            typeList = CardsByTypeAggregate.get(entry[1])
            typeList.append(entry[0])
        else:
            CardsByTypeAggregate[str(entry[1])] = [entry[0]]
    return CardsByTypeAggregate


## CardsByPowerValue Functions
# Groups cards by PowerValue

def GenerateCardsByPowerValue(_loadedCard):
    if _loadedCard.get("power") != None:
        CardsByPowerEntry = [_loadedCard["id"], _loadedCard["power"]]
    else:
        CardsByPowerEntry = [_loadedCard["id"], "None"]

    return CardsByPowerEntry

def GenerateCardsByPowerValueAggregate(_loadedCards):
    CardsByPowerValueAggregate = StatsModel.CardsByPowerValue
    for card in _loadedCards["data"]:
        entry = GenerateCardsByPowerValue(card)
        if CardsByPowerValueAggregate.get(entry[1]) != None:
            powerList = CardsByPowerValueAggregate.get(entry[1])
            powerList.append(entry[0])
        elif CardsByPowerValueAggregate.get(entry[1]) == None:
            CardsByPowerValueAggregate[str(entry[1])] = [entry[0]]
        else:
            CardsByPowerValueAggregate["16+"] = [entry[0]]
    return CardsByPowerValueAggregate


def GenerateCardsByToughnessValue(_loadedCard):
    if _loadedCard.get("toughness") != None:
        CardsByToughnessEntry = [_loadedCard["id"], _loadedCard["toughness"]]
    else:
        CardsByToughnessEntry = [_loadedCard["id"], "None"]

    return CardsByToughnessEntry

def GenerateCardsByToughnessValueAggregate(_loadedCards):
    CardsByToughnessValueAggregate = StatsModel.CardsByToughnessValue
    for card in _loadedCards["data"]:
        entry = GenerateCardsByToughnessValue(_loadedCard=card)
        if CardsByToughnessValueAggregate.get(entry[1]) != None:
            toughnessList = CardsByToughnessValueAggregate.get(entry[1])
            toughnessList.append(entry[0])
        elif CardsByToughnessValueAggregate.get(entry[1]) == None:
            CardsByToughnessValueAggregate[str(entry[1])] = [entry[0]]
        else:
            CardsByToughnessValueAggregate["16+"] = [entry[0]]
    return CardsByToughnessValueAggregate


def GenerateCardsByOracleTextLength(_loadedCard):
    if _loadedCard.get("oracle_text") != None:
        CardsByOracleTextLengthEntry = [_loadedCard["id"], len(_loadedCard["oracle_text"])]
    else:
        CardsByOracleTextLengthEntry = [_loadedCard["id"], 0]

    return CardsByOracleTextLengthEntry

def GenerateCardsByOracleTextLengthAggregate(_loadedCards):
    CardsByOracleTextLengthAggregate = StatsModel.OracleTextLength
    for card in _loadedCards["data"]:
        entry = GenerateCardsByOracleTextLength(_loadedCard=card)
        if CardsByOracleTextLengthAggregate.get(entry[1]) != None:
            oracleTextLengthList = CardsByOracleTextLengthAggregate.get(entry[1])
            oracleTextLengthList.append(entry[0])
        elif CardsByOracleTextLengthAggregate.get(entry[1]) == None:
            CardsByOracleTextLengthAggregate[str(entry[1])] = [entry[0]]
        else:
            CardsByOracleTextLengthAggregate["Unkown"] = [entry[0]]
    return CardsByOracleTextLengthAggregate



## Card Name Id Functions ##
# Generates an array that contains the id and the name of the card.
def GenerateCardNameIdEntry(_loadedCard):
    CardNameIdEntry = [_loadedCard["id"], _loadedCard["name"]]
    return CardNameIdEntry

def GenerateCardNameIdDictionary(_loadedCards):
    GeneratedCardNameIdDictionary = {}
    for card in _loadedCards["data"]:
        Entry = GenerateCardNameIdEntry(_loadedCard=card)
        GeneratedCardNameIdDictionary[str(Entry[0])] = str(Entry[1])
    return GeneratedCardNameIdDictionary



## Functions for saving and loading files ##

# Retreive Live Scryfall Data from the Set Endpoint.
def LoadLiveJson(_setAbbreviation):
    dloader = datadownloader
    return dloader.RetrieveScryfallSetJsonDictionary(_setAbbr=_setAbbreviation)

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

        readFile = json.loads(readFile)

        CompletionMessage = "Opening compressed file completed successfully."

    except():
        CompletionMessage = "Opening the compressed file failed."
        readFile = None

    return [CompletionMessage, readFile]

# Converts an expanded json.gzip file into a dictionary.
def LoadExpandedGZIPJson(_incomingGZIPJson):
    ExpandedGZIPDictionary = json.loads(_incomingGZIPJson[1])
    return ExpandedGZIPDictionary


## Stats block
# Pulls the total card count for a set from the source JSON.
def GenerateTotalCardCount(_loadedCardSet):

    TotalCardCount = _loadedCardSet["total_cards"]

    return TotalCardCount

##
# Builds the final collection stats model for saving an later distribution.
def BuildCollectionStats(_loadedJson):
    CompleatedCollectionStatsModel = StatsModel
    CompleatedCollectionStatsModel.OracleTextLength = GenerateCardsByOracleTextLengthAggregate(_loadedCards=_loadedJson)
    CompleatedCollectionStatsModel.CardsByPowerValue = GenerateCardsByPowerValueAggregate(_loadedCards=_loadedJson)
    CompleatedCollectionStatsModel.CardsByPowerValue = GenerateCardsByToughnessValueAggregate(_loadedCards=_loadedJson)
    CompleatedCollectionStatsModel.TotalCardCount = GenerateTotalCardCount(_loadedCardSet=_loadedJson)
    CompleatedCollectionStatsModel.CardsByColorCombination = GenerateCardsByColorCombination(_processedColorCombinationDictionary=GenerateCardsByColorCombinationRaw(_loadedCards=_loadedJson))
    CompleatedCollectionStatsModel.ColorIdentityAggregate = GenerateCardColorIdentityAggregates(_processedCardColorIdentityAggregatesDictionary=GenerateCardsColorIdentityAggregate(_loadedCards=_loadedJson))
    CompleatedCollectionStatsModel.CardsByCMV = GenerateCardCMVAggregate(_loadedCards=_loadedJson)
    CompleatedCollectionStatsModel.CardsByCost = GenerateCardCostAggregate(_loadedCards=_loadedJson)
    CompleatedCollectionStatsModel.CardsByType = GenerateCardsByTypeAggregate(_loadedCards=_loadedJson)
    CompleatedCollectionStatsModel.CardNames = GenerateCardNameIdDictionary(_loadedCards=_loadedJson)

    return CompleatedCollectionStatsModel

def TestBuildCollectionFromGZIPJson(_path):
    stats  = (BuildCollectionStats(_loadedJson=ExpandGZIPJson(_incomingGzipPath=_path)[1]))
    print("TotalCardCount: ", stats.TotalCardCount)
    print("CardsByColorCombination: ", stats.CardsByColorCombination)
    print("ColorIdentityAggregate: ", stats.ColorIdentityAggregate)
    print("CardsByCMV: ", stats.CardsByCMV)
    print("CardsByCost: ", stats.CardsByCost)
    # print("CardsBySuperType: ", stats.CardsBySuperType)
    print("CardsByType: ", stats.CardsByType)
    print("CardsByPowerValue: ", stats.CardsByPowerValue)
    print("CardsByToughnessValue: ", stats.CardsByToughnessValue)
    print("CardsByRarity: ", stats.CardsByRarity)
    print("FlavorTextPresence: ", stats.FlavorTextPresence)
    print("FlavorTextLength: ", stats.FlavorTextLength)
    print("OracleTextLength: ", stats.OracleTextLength)
    print("KeywordActionAggregate: ", stats.KeywordActionAggregate)
    print("KeywordAbilityAggregate: ", stats.KeywordAbilityAggregate)
    print("CardNames: ", stats.CardNames)

# Builds a collection from live json and then displays it to the console from a passed set abbreviation.
def TestBuildCollectionFromLiveJson(_setAbbreviationInput):
    stats  = (BuildCollectionStats(_loadedJson=LoadLiveJson(_setAbbreviation=_setAbbreviationInput)))
    print("TotalCardCount: ", stats.TotalCardCount)
    print("CardsByColorCombination: ", stats.CardsByColorCombination)
    print("ColorIdentityAggregate: ", stats.ColorIdentityAggregate)
    print("CardsByCMV: ", stats.CardsByCMV)
    print("CardsByCost: ", stats.CardsByCost)
    # print("CardsBySuperType: ", stats.CardsBySuperType)
    print("CardsByType: ", stats.CardsByType)
    print("CardsByPowerValue: ", stats.CardsByPowerValue)
    print("CardsByToughnessValue: ", stats.CardsByToughnessValue)
    print("CardsByRarity: ", stats.CardsByRarity)
    print("FlavorTextPresence: ", stats.FlavorTextPresence)
    print("FlavorTextLength: ", stats.FlavorTextLength)
    print("OracleTextLength: ", stats.OracleTextLength)
    print("KeywordActionAggregate: ", stats.KeywordActionAggregate)
    print("KeywordAbilityAggregate: ", stats.KeywordAbilityAggregate)
    print("CardNames: ", stats.CardNames)

# Builds a collection model from live data, then saves it as json to the local directory from a passed set abbreviation.
def TestBuildAndSaveCollectionFromLiveJson(_setAbbreviationInput):
    stats  = (BuildCollectionStats(_loadedJson=LoadLiveJson(_setAbbreviation=_setAbbreviationInput)))
    statsJson = json.dumps(stats.__dict__)
    fileName = str(_setAbbreviationInput) + "statsmodel.json"
    statsFile = open(fileName, "w")
    statsFile.writelines(statsJson)
    statsFile.close()

# Builds a collection model from live data, then uploads it to mongodb from a passed set abbreviation.
def TestBuildAndUploadCollectionFromLiveJson(_setAbbreviationInput):
    stats  = (BuildCollectionStats(_loadedJson=LoadLiveJson(_setAbbreviation=_setAbbreviationInput)))
    statsDictionary = stats.__dict__
    uploader.InsertOneSetRecord(_recordJson=statsDictionary)

#TestBuildCollectionFromGZIPJson(_path="C:\\Users\\jeffrey.moody\\Documents\\GitHub\\etb\\compressed.json.gzip")
#TestBuildAndSaveCollectionFromLiveJson(_setAbbreviationInput="AFR")

TestBuildAndUploadCollectionFromLiveJson(_setAbbreviationInput="AFR")
