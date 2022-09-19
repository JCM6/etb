import requests, json

# Retrieve the raw json data to be parsed from scryfall


# Bulk data retrieval logic

## Retrive a list of sets from scryfall:
def RetrieveRawScryfallSetList():
    response = requests.get(url="https://api.scryfall.com/sets")
    retrievedRawSetList = response.text
    return retrievedRawSetList

def FormatRawRetrievedScyfallSetList(_retrievedRawSetList):
    retrievedDictionary = json.loads(_retrievedRawSetList)
    return retrievedDictionary

def RefineRawRetrievedScryfallSetListDictionary(_retrievedDictionary):
    refinedDictionary = {}
    for entry in _retrievedDictionary["data"]:
        refinedDictionary[entry["id"]] = [entry["code"], entry["name"]]
    return refinedDictionary

## Single Set Retrieval logic.
def RetrieveScryfallSetJson(_setAbbreviation):
    url = "https://api.scryfall.com/cards/search?q=set%3D"
    response = requests.get(url=url + _setAbbreviation)
    retrievedResponseJson = response.text
    return retrievedResponseJson
    
## Load the retrieved json into a python dictionary.
def FormatScryfallSetAsDict(_retrievedJson):
    retrievedDictionary = json.loads(_retrievedJson)
    return retrievedDictionary

## Display the constructed dictionary in the console.
def DisplayJsonInConsole(_inputDictionary):
    try:
        print(json.dumps(_inputDictionary, indent=4))
        returnStatement = {"Code":1, "Description":"Display Json in console completed successfully."}
    except:
        returnStatement = {"Code":0, "Description":"Display Json in console failed."}
    return returnStatement

## Save the returned dictionary as a json file. Single line Json occurrs when indnet is = 0.
def SaveReturnedDictionary(_inputDictionary, _indent):
    if _indent > 0:
        jsonFile = open("exportJSON.json", "w")

        try:
            _inputDictionary  = json.dumps(_inputDictionary, indent=_indent)
            for line in _inputDictionary:
                jsonFile.writelines(str(line))

            jsonFile.close()

            returnStatement = {"Code":1, "Description":"Saving Json to a file completed successfully."}
            print(returnStatement)

        except Exception as inst:
            returnStatement = {"Code":0, "Description":"Saving Json to a file failed."}
            returnStatement["Exception"] = inst
            print(returnStatement)

    else:
        jsonFile = open("exportJSON.json", "w")

        try:
            _inputDictionary  = json.dumps(_inputDictionary)
            for line in _inputDictionary:
                jsonFile.writelines(str(line))

            jsonFile.close()

            returnStatement = {"Code":1, "Description":"Saving Json to a file completed successfully."}
            print(returnStatement)

        except:
            returnStatement = {"Code":0, "Description":"Saving Json to a file failed."}
            print(returnStatement)

    return returnStatement

## Retrives set JSON and returns a python dictionary
def RetrieveScryfallSetJsonDictionary(_setAbbr):
    return FormatScryfallSetAsDict(_retrievedJson=RetrieveScryfallSetJson(_setAbbreviation=_setAbbr))

## Retrives and displays set json in an indented format in the active console.
def RetrieveAndDisplayScryfallSetJson(_setAbbr):
    DisplayJsonInConsole(_inputDictionary=FormatScryfallSetAsDict(_retrievedJson=RetrieveScryfallSetJson(_setAbbreviation=_setAbbr)))

## Retrives and saves the set json in a single line or indented format in the directory running the script.
def RetrieveAndSaveScryfallSetJson(_setAbbr, _ind):
    SaveReturnedDictionary(_inputDictionary=FormatScryfallSetAsDict(_retrievedJson=RetrieveScryfallSetJson(_setAbbreviation=_setAbbr)), _indent=_ind)


## Test Block:
print(json.dumps(RefineRawRetrievedScryfallSetListDictionary(_retrievedDictionary=FormatRawRetrievedScyfallSetList(_retrievedRawSetList=RetrieveRawScryfallSetList())), indent=4))