from urllib import response
import requests, json 
import urllib.parse

# Example Url:
# https://api.scryfall.com/cards/named?fuzzy=aust+com


class Decklist():

    def __init__(self, _fileName):

        deckListFile = open(_fileName, "r")
        
        self.decklist = str(deckListFile.read())

        lines = self.decklist.split("1 ")
                
        deckListFile.close()


class CardCall():

    def __init__(self, _card):

        self.nameQuoted = urllib.parse.quote(_card)
        
        self.scryUrl = "https://api.scryfall.com"
        self.cardNameStem = "/cards/named"
        self.queryString = f"?exact={self.nameQuoted}"
        self.url = self.scryUrl + self.cardNameStem + self.queryString
        self.cardName = _card
        
        response = requests.get(self.url)
        
        self.cardCallStatusCode = response.status_code
        self.cardCallResponse = response.text
        self.cardCallResponeDictionary = json.loads(response.text)



# fetch("https://api.moxfield.com/v2/decks/all/NIUzSLJ9qUCfFyvf0wEXcA", {
#   "headers": {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
#     "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJGcmVkc3RhY2siLCJqdGkiOiI2MTk1NmViNy1mZmZmLTRhNDQtOGZhOC1mMTc3OTZhNzdhZmUiLCJodHRwOi8vd3d3Lm1veGZpZWxkLmNvbS93cy8yMDE2LzA4L2lkZW50aXR5L2NsYWltcy9Vc2VySWQiOiIxMDMwNyIsImh0dHA6Ly93d3cubW94ZmllbGQuY29tL3dzLzIwMTYvMDgvaWRlbnRpdHkvY2xhaW1zL0VtYWlsQ29uZmlybWVkIjoiVHJ1ZSIsImV4cCI6MTY1MzQ1MzU4NiwiaXNzIjoiaHR0cHM6Ly9tb3hmaWVsZC1hcGkuYXp1cmV3ZWJzaXRlcy5uZXQvIiwiYXVkIjoidXNyIn0.m9A-PSRmG0g5fY7eXEsk04bNe4L46ojkRqGd3WTZieE",
#     "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site"
#   },
#   "referrer": "https://www.moxfield.com/",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": null,
#   "method": "GET",
#   "mode": "cors",
#   "credentials": "include"
# });


# Returns a moxfield deck object 
class MoxFieldDeck():
    
    def __init__(self, deckid):

        self.moxfielddeckid = deckid

        self.url = f"https://api.moxfield.com/v2/decks/all/{deckid}"

        self.headers = {
            "accept":"application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
            "accept-encoding":"utf-8"
        }

        self.moxfieldresponse = requests.get(url=self.url, headers=self.headers)

        self.moxfieldresponseContent = self.moxfieldresponse.content

        self.moxfieldresponseText = self.moxfieldresponse.text

class BuildDecklist():

    def __init__(self, moxifieldResponse):
            # Convert the response to a dictionary object for further usage.
        def PrepMoxfieldResponse(_moxfieldResponse):

            preppedDecklist = json.loads(_moxfieldResponse.moxfieldresponse.text)
            
            return preppedDecklist

        # Build the list of commanders to be added to the file.
        def GetCommanders(_decklist):
            
            incCommander = _decklist["main"]

            print(incCommander)

            commanders = []

            if len(incCommander) <= 2:

                for commander in incCommander:

                    commanders.append("1")
                    commanders.append(commander["name"])
                    commanders.append(commander["mana_cost"])
                    commanders.append(commander["cmc"])
                    commanders.append(commander["type_line"])
                    commanders.append(commander["oracle_text"])
                    commanders.append(commander["power"])
                    commanders.append(commander["toughness"])
            else:

                commanders.append("1")
                commanders.append(incCommander["name"])
                commanders.append(incCommander["mana_cost"])
                commanders.append(incCommander["cmc"])
                commanders.append(incCommander["type_line"])
                commanders.append(incCommander["oracle_text"])
                commanders.append(incCommander["power"])
                commanders.append(incCommander["toughness"])

            return commanders

        self.deckListHeaders = ["quantity", "name", "mana_cost", "cmc", "type_line", "oracle_text", "power", "toughness"]

        decklist = PrepMoxfieldResponse(_moxfieldResponse=moxifieldResponse)
        
        self.commanders = GetCommanders(_decklist=decklist)

        print(self.commanders)




def SaveCSVFile():
    pass



if __name__ == "__main__": 
    moxResp = MoxFieldDeck(deckid="NIUzSLJ9qUCfFyvf0wEXcA")

    decklist = BuildDecklist(moxifieldResponse=moxResp)

    print(decklist.commanders)