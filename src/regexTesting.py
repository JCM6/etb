import re

# We have placed a few variations and two false options to make sure that the regex correctly id's variations.
shardVariations = ["UWB", "B", "WUBRG", "ubw", "UW", "G", "W", "WUB", "WUBR", "r", "WU", "u", "WB", "BU", "UB", "WUBG", "BUW", "RBU", "UBR", "GWR", "RWG"]

# basic setup for regex right now:
# Start of Group: (
# Character that we don't want ahead: (?<!n)
# Character set we want. This includes any combination of the encapsulated characters: [a]
# Total desired length {x}
# Character that we done want after: (?!n)
# Close of Group: )
# Example Abstract Result: ((?<!n)+(?<!m)[a]{x}(?<!n)+(?<!m)) 

ColorRegexPatternStrings = {
        "Serra":"((?<!U)+(?<!B)+(?<!R)+(?<!G)[W]{1}(?!U)+(?!B)+(?!R)+(?!G))",
        "Urza":"((?<!W)+(?<!B)+(?<!R)+(?<!G)[U]{1}(?!W)+(?!B)+(?!R)+(?!G))",
        "Yawgmoth":"((?<!W)+(?<!U)+(?<!R)+(?<!G)[B]{1}(?!W)+(?!U)+(?!R)+(?!G))",
        "Windgrace":"((?<!W)+(?<!U)+(?<!B)+(?<!G)[R]{1}(?!W)+(?!U)+(?!B)+(?!G))",
        "Freyalise":"((?<!W)+(?<!U)+(?<!B)+(?<!R)[G]{1}(?!W)+(?!U)+(?!G)+(?!R))",
        "Azorius":"((?<!R)+(?<!G)(?<!B)[WU]{2}(?!R)+(?!G)+(?!B))",
        "Dimir":"((?<!R)+(?<!G)(?<!W)[BU]{2}(?!R)+(?!G)+(?!W))",
        "Rakdos":"((?<!U)+(?<!G)(?<!W)[BR]{2}(?!U)+(?!G)+(?!W))",
        "Gruul":"((?<!U)+(?<!W)(?<!B)[RG]{2}(?!U)+(?!W)+(?!B))",
        "Selesnya":"((?<!R)+(?<!U)(?<!B)[WG]{2}(?!R)+(?!U)+(?!B))",
        "Orzhov":"((?<!R)+(?<!G)(?<!U)[WB]{2}(?!R)+(?!G)+(?!U))",
        "Izzet":"((?<!W)+(?<!G)(?<!B)[UR]{2}(?!W)+(?!G)+(?!B))",
        "Golgari":"((?<!R)+(?<!W)(?<!U)[GB]{2}(?!R)+(?!U)+(?!W))",
        "Boros":"((?<!U)+(?<!G)(?<!B)[WR]{2}(?!U)+(?!G)+(?!B))",
        "Simic":"((?<!R)+(?<!W)(?<!B)[UG]{2}(?!R)+(?!W)+(?!B))",
        "Bant":"((?<!R)+(?<!B)[WUG]{3}(?!R)+(?!B))",
        "Esper":"((?<!R)+(?<!G)[WUB]{3}(?!R)+(?!G))",
        "Grixis":"((?<!W)+(?<!G)[UBR]{3}(?!W)+(?!G))",
        "Jund":"((?<!W)+(?<!U)[BRG]{3}(?!W)+(?!U))",
        "Naya":"((?<!U)+(?<!B)[WRG]{3}(?!U)+(?!B))",
        "Abzan":"((?<!R)+(?<!G)[WUB]{3}(?!R)+(?!G))",
        "Jeskai":"((?<!B)+(?<!G)[WUR]{3}(?!B)+(?!G))",
        "Sultai":"((?<!R)+(?<!W)[UBG]{3}(?!R)+(?!W))",
        "Mardu":"((?<!U)+(?<!G)[WBR]{3}(?!U)+(?!G))",
        "Temur":"((?<!W)+(?<!B)[URG]{3}(?!W)+(?!B))",
        "Glint":"((?<!W)[URBG]{4}(?!W))",
        "Dune":"((?<!U)[WRBG]{4}(?!U))",
        "Ink":"((?<!B)[WRUG]{4}(?!B))",
        "Witch":"((?<!R)[WUBG]{4}(?!R))",
        "Yore":"((?<!G)[WRBR]{4}(?!G))",
        # Urd is 5 color. 
        # #I was going to do Ur due to the Ur Dragon, but figured it would be besty to 
        # make a new term. rather than repeat Izzet.
        "Urd":"[WUBRG]{5}"
}



p = re.compile(ColorRegexPatternStrings["Urza"], re.IGNORECASE)

for pattern in shardVariations:
    print("matches: ", p.match(pattern), " search results: ", p.search(pattern))
