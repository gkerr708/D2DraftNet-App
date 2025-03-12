from pathlib import Path

current_patch = "7_37e"

PROJECT_DIR = Path(__file__).parent.parent

# Define the list of heroes
HEROS_unsorted = ['Anti-Mage', 'Axe', 'Bane', 'Bloodseeker', 'Crystal Maiden', 'Drow Ranger', 'Earthshaker', 'Juggernaut', 'Mirana', 'Morphling', 'Shadow Fiend', 
         'Phantom Lancer', 'Puck', 'Pudge', 'Razor', 'Sand King', 'Storm Spirit', 'Sven', 'Tiny', 'Vengeful Spirit', 'Windranger', 'Zeus', 'Kunkka', 'Lina', 
         'Lion', 'Shadow Shaman', 'Slardar', 'Tidehunter', 'Witch Doctor', 'Lich', 'Riki', 'Enigma', 'Tinker', 'Sniper', 'Necrophos', 'Warlock', 'Beastmaster', 
         'Queen of Pain', 'Venomancer', 'Faceless Void', 'Wraith King', 'Death Prophet', 'Phantom Assassin', 'Pugna', 'Templar Assassin', 'Viper', 'Luna', 
         'Dragon Knight', 'Dazzle', 'Clockwerk', 'Leshrac', "Nature's Prophet", 'Lifestealer', 'Dark Seer', 'Clinkz', 'Omniknight', 'Enchantress', 'Huskar', 
         'Night Stalker', 'Broodmother', 'Bounty Hunter', 'Weaver', 'Jakiro', 'Batrider', 'Chen', 'Spectre', 'Ancient Apparition', 'Doom', 'Ursa', 
         'Spirit Breaker', 'Gyrocopter', 'Alchemist', 'Invoker', 'Silencer', 'Outworld Destroyer', 'Lycan', 'Brewmaster', 'Shadow Demon', 'Lone Druid', 
         'Chaos Knight', 'Meepo', 'Treant Protector', 'Ogre Magi', 'Undying', 'Rubick', 'Disruptor', 'Nyx Assassin', 'Naga Siren', 'Keeper of the Light', 
         'Io', 'Visage', 'Slark', 'Medusa', 'Troll Warlord', 'Centaur Warrunner', 'Magnus', 'Timbersaw', 'Bristleback', 'Tusk', 'Skywrath Mage', 'Abaddon', 
         'Elder Titan', 'Legion Commander', 'Techies', 'Ember Spirit', 'Earth Spirit', 'Underlord', 'Terrorblade', 'Phoenix', 'Oracle', 'Winter Wyvern', 
         'Arc Warden', 'Monkey King', 'Dark Willow', 'Pangolier', 'Grimstroke', 'Hoodwink', 'Void Spirit', 'Snapfire', 'Mars', 'Ringmaster', 'Dawnbreaker', 
         'Marci', 'Primal Beast', 'Muerta', 'Kez']

# Map hero names to indices
#HERO_MAP = {hero: i + 1 for i, hero in enumerate(HEROS_unsorted)}

HEROS_sorted = sorted(HEROS_unsorted)
HEROS_uscore = [hero.replace(" ", "_").lower() for hero in HEROS_sorted]
HEROS = [hero.replace("nature's_prophet", "natures_prophet").lower() for hero in HEROS_uscore]
#DIRE_HEROS = sorted(["Dire_" + hero for hero in HEROS])
#RADIANT_HEROS = sorted(["Radiant_" + hero for hero in HEROS])
#
#NUM_HEROS= len(HERO_MAP) + 1  # Ensure consistency with training
#LAYERS = [32, 16]  # Layers for the current model (7.37e)
#EMBEDDING_DIM = 3  # Embedding dimension for the current model (7.37e)



if __name__ == "__main__":
    #print(HEROS)
    print(PROJECT_DIR.exists())
