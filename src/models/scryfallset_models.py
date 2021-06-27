
# What we want to pull for our purposes:
CollectionStatsModel = {   
    "TotalCardCount":[],
    "CardsByColorCombination":{
        "Azorius":[],
        "Dimir":[],
        "Rakdos":[],
        "Gruul":[],
        "Selesnya":[],
        "Orzhov":[],
        "Izzet":[],
        "Golgari":[],
        "Boros":[],
        "Simic":[],
        "Bant":[],
        "Esper":[],
        "Grixis":[],
        "Jund":[],
        "Naya":[],
        "Abzan":[],
        "Jeskai":[],
        "Sultai":[],
        "Mardu":[],
        "Temur":[],
        "Glint":[],
        "Dune":[],
        "Ink":[],
        "Witch":[],
        "Yore":[],
        # Urd is 5 color. 
        # #I was going to do Ur due to the Ur Dragon, but figured it would be besty to 
        # make a new term. rather than repeat Izzet.
        "Urd":[]
        },
    "CardsByCMV":{
        "0":[],
        "1":[],
        "2":[],
        "3":[],
        "4":[],
        "5":[],
        "6":[],
        "7":[],
        "8":[],
        "9":[],
        "10":[],
        "11":[],
        "12":[],
        "13":[],
        "14":[],
        "15":[],
        "16+":[]
    },
    "CardsBySuperType":{
        "Basic":[],
        "Legendary":[],
        "Ongoing":[],
        "Snow":[],
        "World":[]
    },
    "CardsByType":{
        "Artifacts":[], 
        "Creatures":[], 
        "Enchantments":[], 
        "Instants":[], 
        "Lands":[], 
        "Planeswalkers":[], 
        "Sorceries":[], 
        "Tribals":[], 
        "Planes":[], 
        "PhenomenaVanguards":[], 
        "Schemes":[], 
        "Conspiracies":[]
    },


}
# Split off Cards into their own list with neded values
CardDetailModel = [
    {
        "object": "card",
        "id": "4620cc3b-e401-4096-b310-fed080806344",
        "oracle_id": "b22de128-6dad-4e15-a547-1c9ca08df5ff",
        "multiverse_ids": [
            513568
        ],
        "mtgo_id": 88659,
        "arena_id": 76484,
        "tcgplayer_id": 235873,
        "cardmarket_id": 557514,
        "name": "Academic Dispute",
        "lang": "en",
        "released_at": "2021-04-23",
        "layout": "normal",
        "mana_cost": "{R}",
        "cmc": 1.0,
        "type_line": "Instant",
        "oracle_text": "Target creature blocks this turn if able. You may have it gain reach until end of turn.\nLearn. (You may reveal a Lesson card you own from outside the game and put it into your hand, or discard a card to draw a card.)",
        "colors": [
            "R"
        ],
        "color_identity": [
            "R"
        ],
        "keywords": [
            "Learn"
        ],
        "reprint": False,
        "variation": False,
        "set": "stx",
        "set_name": "Strixhaven: School of Mages",
        "set_type": "expansion",
        "collector_number": "91",
        "digital": False,
        "rarity": "uncommon",
        "flavor_text": "\"I'll show you original research, you hack!\"",
        "card_back_id": "0aeebaf5-8c7d-4636-9e82-8c27447861f7",
        "artist": "Manuel Casta\u00f1\u00f3n",
        "artist_ids": [
            "35f11eeb-36ff-4059-bb70-d1274f5bd858"
        ],
        "illustration_id": "e80a3753-bdc7-4945-bb91-a6e7dc59fa40",
        "border_color": "black",
        "frame": "2015",
        "full_art": False,
        "textless": False,
        "booster": True,
        "story_spotlight": False,
        "edhrec_rank": 13957
    }
]