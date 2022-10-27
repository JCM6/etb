
import itertools
simpleLib = {
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
        }
simpleLib = {
            "Artifact":[], 
            "Creature":[], 
            "Enchantment":[], 
            "Instant":[], 
            "Land":[], 
            "Planeswalker":[], 
            "Sorcery":[], 
            "Tribal":[], 
            "Plane":[], 
            "Phenomena":[],
            "Vanguard":[], 
            "Scheme":[], 
            "Conspiracy":[]
        }

l = set(simpleLib.keys())
TwoColorCombos = list(itertools.combinations(l, 2))
print(TwoColorCombos)
print(type(TwoColorCombos[0]))
libUpdate = {}
for i in TwoColorCombos:
    libUpdate[str()] = []