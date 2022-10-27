import requests, json 
import urllib.parse

# Example Url:
# https://api.scryfall.com/cards/named?fuzzy=aust+com

class CardCall(_cardName):

    self.nameQuoted = urllib.parse.quote(_cardName)
    
    self.config = {
        "scryUrl":"https://api.scryfall.com",
        "cardNameStem":"/cards/named",
        "queryString":f"?fuzzy={self.nameQuoted}",
        "cardName":_cardName
    }
    
    
    