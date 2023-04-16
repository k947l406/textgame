'''
Hackathon Mini Game
'''
###This is where the unorganized ideas are placed.
import random

'''
The nonsense ideas
Today we will be programming a text-based adventure game
The player character will have hit points, attributes, and equipment.
The gameplay loop consists of resting and upgading in town and going through
randomly generated dungeons.
Dungeons consist of monsters, loot, and traps.
    Monsters will leave behind loot sometimes.
        Monster parts? Eyes, head, arms, legs, wings, tails, etc.
            Multiple tiers of monster parts?
            The higher the tier the more expensive it sells for.
Use gold to exchange for upgrades.
Gold can also be exchanged to train (increase) attributes.
Free "training rooms" can be found in dungeons as well.
There will be no such thing as a player character "level".
Equipment progression will be important.
The town consists of:
Smithy, for equipment
    Upgrading current equipment may be possible?
    New equipment could be unlocked when enough monster parts.
General Store, for consumables and misc. items usable in dungeons
    Some items may come in handy!
    Sell inventory expansions in sets of 5 slots
    New items will appear in Smithy and General Store as the player
    character unlocks new dungeons.
Inn, to fully recover hit points.
    It may be interesting to keep track of time.
    Perhaps going through each room in a dungeon takes some time.
        Staying awake beyond a certain threshold will impose penalties
        based on the character's attributes.
Training Room, to increase attributes
List of facilities = ["Smithy", "Store", "Inn", "Train"]
Dungeons:
More dungeons are unlocked as dungeons are cleared.
    Each dungeon has a random number of rooms (within reasonable bounds)
    and a boss at the end. Clearing the dungeon provides a treasure chest
    that is automatically opened and provides the player with rewards.
    Example:
    Beginning Dungeon:
        2 enemy rooms
        1 loot room
        1 trap room
        1 random room (any between enemy, loot, trap, and train)
        1 boss room (at the end)
    List again because there's a chance that addition events
    will include inserting new rooms
        Dungeon = [2,1,1,1,1]
    Entry Dungeon:
        3-5 enemy rooms
        1 loot room
        0-2 trap rooms
        1 boss room
        Dungeon = [random.randint(3,5),1,random.randint(0,2),1]
        Alternatively, use a dictonary
        DungeonRooms = {
            #room_type: room_count 
            "enemy": random.randint(3,5),
            "loot": 1,
            "trap": random.randint(0,2),
            "random": 0,
            "boss": 1
        }
    Rooms are naturally randomly ordered after determining how many there are.
    When a dungeon is cleared, check for new dungeons and add them to
    the list of available dungeons.
Character attributes to keep track of:
HP, MP, STR, DEX, CON, INT, WIS, CHA #naturally inspired from ttrpgs
CharStats = {
            #stat: number
            "MaxHP": 10,
            "HP": 10,
            "MaxMP": 10,
            "MP": 10,
            "STR": 10,
            "DEX": 10,
            "INT": 10,
            "CON": 10,
            "WIS": 10,
            "CHA": 10, 
            "MainHand": Sword, #so we'd grab something like
                #Damage = CharStats.get("MainHand") + CharStats.get("STR")
            "OffHand": Shield,
            "Head": None,
            "Armor": Leather,
            "Accessory": Heal_Ring
        }
Weapons like Sword have a min damage and a max damage,
{"min": minVal, "max": maxVal, "critRate": CRVal, "critMultiplier": CMVal}
Why a dictionary? Why not a class? No clue. Right, classes exist.
Head and Armor have [pDef, mDef] for physical and magical damage
Accessory provides a variety of bonuses, like stat increases.
Important! Ok, so scratch the dictionaries. We want a character class.
Define character class with all the stats and info like the dictionary.
Also define weapons as classes.
Define each equipment as a class. Turn them into easy objects.
Important!! What we should do is classify each equipment into a dictionary.
MainHands = {
    #ID: Item
    #If we do .get(ID), it returns the Item
    1: Sword,
    2: Bow,
    etc.
}
Also give weapons a 1-handed/2-handed trait for equipment checks so
it's not possible to equip a shield when you have a greatsword/bow or whatnot
OffHands = {
    1: Wood Shield,
    2: Magic Tome,
    etc.
}
Items = {
    1: Health Potion,
    2: Mana Potion,
    etc.
}
You get the idea.
This also means we need to initialize all these objects at the start of the
game so they all show up in the dictionaries proper.
It may be messy, but it could be possible to do something like:
Sword = items.Weapon("Sword",3,5,0.05,2)
BigSword = items.Weapon("BigSword",30,50,0.05,3)
MainHands = {
    1: Sword,
    2: BigSword
}
A flaw to this is that we're initializing a bunch of objects that won't
see the light of day, so I'm more inclined to do a dictionary approach for
equipment. The character is definitely a class because we will see all of
that consistently being used.
It is best for an equipment to be a dictionary itself because they don't
have any functions. Upgrading equipment may be trickier to program in, though. 
-----
Now, you might be thinking, why not store equipment information as a list
instead? We already know [1,2] would mean minDmg and maxDmg. Well, the thing
is, it's not as readable. While it would be more efficient, it makes adding
moretraits into the weapon difficult and getting the right numbers from the
right position of a weapon would be a multi-reference of going back and forth.
I could also do a list of attribute names like [name, minDmg, maxDmg], and
then refer their respective indicies to match the weapon data. I say it's too
much trouble. I'll do something more a little bit more readable like,
mindamage = character.get(weapon).get(minDmg) instead of something like
mindamage = character.get(weapon)[weaponTraits.indexof(minDmg)]
I'm a fool, I'll make items as classes themselves. The setup will read
closer to a list, but we'll have proper methods like use() for every item
-----
New list of items:
Items = {
    #100: MainHands
    101: Sword,
    102: BigSword,
    #200: OffHands
    201: Shield,
    #300: Head
    etc.
}
This way the loot table just has to refer to one dictionary, and we are able
to limit what type of item we want to give if need be by simply limiting the
ID's largest digit (Which would be the 100s value in this case)
Equip slots: Weapon, Offhand, Head, Body, Waist, Arms, Legs, Accessory
    Personally, I think this number of equipment might be overkill
    Suggested: Mainhand (Weapon), Offhand, Head, Armor, Accessory
    It's important to have a slot for a robe and wizard hat
SPELLS list: spells you can use. Spells cost MP.
    Spells can be learnt through spellbooks.
    Spellbooks can be found from loot and rewards.
    Some spellbooks can be bought from the store. 
Inventory Slots: list with a list [item name, item count]?

Save and load character data. Very important.
Lots of try except for inputs

SCENES
    BATTLE -- the first thing we should work on
        Supports multiple enemies! (hopefully)
        ATTACK -- make an attack with the weapon you have on hand
        CAST -- cast a spell you know
        ITEM == use an item
            using a piece of equipment will swap your equips
            using a consumable will trigger its effect and remove it
            from your inventory
            using monster pieces will boot you back to the main
            battle options menu. "That won't do anything here!"
        RUN -- escape the battle and leave the dungeon entirely
            There won't be room backtracking support the way this
            is programmed so simply.
    TOWN -- where you select areas to go to
        SMITHY -- scene where you pop up more menus to upgrade stuff
    MENU -- accessible anywhere? to check up on status and inventory
        INVENTORY
        calling inventory will simply print out your inventory as is
        it may be automagically sorted when new items come in, or not
            Include a sort (by type) option and a drop item option
            We will want a use item option as well
        STATUS prints out character stats, not much else to it
        CAST gives you a list of spells you can cast outside of combat
-----
It may be neat to add in an input interpreter that looks for keywords.
e.g.
>>>What do you do?:
>>>I cast fireball
The program ignores the I and reads in the keyword "cast" then looks for
the next keyword which would be a spell name, and that would be "fireball"
in this case.
>>>I call upon the dragons of darkness and cast a massive fireball
Same case: go through the string, look for the first keyword, then the
second keyword check
>>>I attack the goblin with my greatsword
All you have to do is read "attack"
This may cause some false interpretations when you try to input negations like
>>>"I do NOT attack the goblin"
So we would need a case to check for negatives and ask the player to please
input without any negatives unless we have the time to make something smart
enough to fix that up as well (So TL;DR this is a pipe dream for 36 hours)
-----
wew
'''
