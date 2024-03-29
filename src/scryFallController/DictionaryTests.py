import json

card = """{
    "object": "card",
    "id": "67f4c93b-080c-4196-b095-6a120a221988",
    "oracle_id": "562d71b9-1646-474e-9293-55da6947a758",
    "multiverse_ids": [
        491723
    ],
    "mtgo_id": 83139,
    "arena_id": 73284,
    "tcgplayer_id": 222163,
    "cardmarket_id": 496690,
    "name": "Agadeem's Awakening // Agadeem, the Undercrypt",
    "lang": "en",
    "released_at": "2020-09-25",
    "uri": "https://api.scryfall.com/cards/67f4c93b-080c-4196-b095-6a120a221988",
    "scryfall_uri": "https://scryfall.com/card/znr/90/agadeems-awakening-agadeem-the-undercrypt?utm_source=api",
    "layout": "modal_dfc",
    "highres_image": true,
    "image_status": "highres_scan",
    "cmc": 3.0,
    "type_line": "Sorcery // Land",
    "color_identity": [
        "B"
    ],
    "keywords": [],
    "produced_mana": [
        "B"
    ],
    "card_faces": [
        {
            "object": "card_face",
            "name": "Agadeem's Awakening",
            "mana_cost": "{X}{B}{B}{B}",
            "type_line": "Sorcery",
            "oracle_text": "Return from your graveyard to the battlefield any number of target creature cards that each have a different mana value X or less.",
            "colors": [
                "B"
            ],
            "flavor_text": "\"Now is the death-hour, just before dawn. Wake, sleepers, and haunt the living!\"\n\u2014Vivias, Witch Vessel",
            "artist": "Dmitry Burmak",
            "artist_id": "9872f5c0-274a-48ce-a9ad-6f0d5654e29c",
            "illustration_id": "9c4fd66b-b125-4e63-a0ee-d49ec58fc381",
            "image_uris": {
                "small": "https://c1.scryfall.com/file/scryfall-cards/small/front/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226",
                "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226",
                "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226",
                "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/6/7/67f4c93b-080c-4196-b095-6a120a221988.png?1604195226",
                "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226",
                "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226"
            }
        },
        {
            "object": "card_face",
            "name": "Agadeem, the Undercrypt",
            "flavor_name": "",
            "mana_cost": "",
            "type_line": "Land",
            "oracle_text": "As Agadeem, the Undercrypt enters the battlefield, you may pay 3 life. If you don't, it enters the battlefield tapped.\n{T}: Add {B}.",
            "colors": [],
            "flavor_text": "\"Here below the hedron fields, souls and secrets lie entombed.\"\n\u2014Vivias, Witch Vessel",
            "artist": "Dmitry Burmak",
            "artist_id": "9872f5c0-274a-48ce-a9ad-6f0d5654e29c",
            "illustration_id": "259cbafd-c75a-45b1-9b1e-a428796aa977",
            "image_uris": {
                "small": "https://c1.scryfall.com/file/scryfall-cards/small/back/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226",
                "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/back/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226",
                "large": "https://c1.scryfall.com/file/scryfall-cards/large/back/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226",
                "png": "https://c1.scryfall.com/file/scryfall-cards/png/back/6/7/67f4c93b-080c-4196-b095-6a120a221988.png?1604195226",
                "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/back/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226",
                "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/back/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg?1604195226"
            }
        }
    ],
    "legalities": {
        "standard": "legal",
        "future": "not_legal",
        "historic": "legal",
        "gladiator": "legal",
        "pioneer": "legal",
        "explorer": "legal",
        "modern": "legal",
        "legacy": "legal",
        "pauper": "not_legal",
        "vintage": "legal",
        "penny": "not_legal",
        "commander": "legal",
        "brawl": "legal",
        "historicbrawl": "legal",
        "alchemy": "legal",
        "paupercommander": "not_legal",
        "duel": "legal",
        "oldschool": "not_legal",
        "premodern": "not_legal"
    },
    "games": [
        "arena",
        "paper",
        "mtgo"
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
    "reprint": false,
    "variation": false,
    "set_id": "f4e01fa7-b254-42dd-849f-69b58027a8c4",
    "set": "znr",
    "set_name": "Zendikar Rising",
    "set_type": "expansion",
    "set_uri": "https://api.scryfall.com/sets/f4e01fa7-b254-42dd-849f-69b58027a8c4",
    "set_search_uri": "https://api.scryfall.com/cards/search?order=set&q=e%3Aznr&unique=prints",
    "scryfall_set_uri": "https://scryfall.com/sets/znr?utm_source=api",
    "rulings_uri": "https://api.scryfall.com/cards/67f4c93b-080c-4196-b095-6a120a221988/rulings",
    "prints_search_uri": "https://api.scryfall.com/cards/search?order=released&q=oracleid%3A562d71b9-1646-474e-9293-55da6947a758&unique=prints",
    "collector_number": "90",
    "digital": false,
    "rarity": "mythic",
    "artist": "Dmitry Burmak",
    "artist_ids": [
        "9872f5c0-274a-48ce-a9ad-6f0d5654e29c"
    ],
    "border_color": "black",
    "frame": "2015",
    "security_stamp": "oval",
    "full_art": false,
    "textless": false,
    "booster": true,
    "story_spotlight": false,
    "edhrec_rank": 22264,
    "preview": {
        "source": "Star City Games",
        "source_uri": "https://articles.starcitygames.com/news/black-gets-modal-double-faced-mythic-in-agadeems-awakening/",
        "previewed_at": "2020-09-08"
    },
    "prices": {
        "usd": "13.31",
        "usd_foil": "15.15",
        "usd_etched": null,
        "eur": "15.62",
        "eur_foil": "20.00",
        "tix": "5.92"
    },
    "related_uris": {
        "gatherer": "https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=491723",
        "tcgplayer_infinite_articles": "https://infinite.tcgplayer.com/search?contentMode=article&game=magic&partner=scryfall&q=Agadeem%27s+Awakening+%2F%2F+Agadeem%2C+the+Undercrypt&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "tcgplayer_infinite_decks": "https://infinite.tcgplayer.com/search?contentMode=deck&game=magic&partner=scryfall&q=Agadeem%27s+Awakening+%2F%2F+Agadeem%2C+the+Undercrypt&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "edhrec": "https://edhrec.com/route/?cc=Agadeem%27s+Awakening"
    },
    "purchase_uris": {
        "tcgplayer": "https://www.tcgplayer.com/product/222163?page=1&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "cardmarket": "https://www.cardmarket.com/en/Magic/Products/Search?referrer=scryfall&searchString=Agadeem%27s+Awakening&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall",
        "cardhoarder": "https://www.cardhoarder.com/cards/83139?affiliate_id=scryfall&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"
    }
}"""

cardDictionary = json.loads(card, encoding='utf=8')

print(cardDictionary.keys())