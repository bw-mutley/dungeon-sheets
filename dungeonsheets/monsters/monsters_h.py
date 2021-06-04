"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability



class HalfRedDragonVeteran(Monster):
    """
    **Multiattack**: The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword attack.

    **Longsword**: Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.

    **Shortsword**: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.

    **Heavy Crossbow**: Ranged Weapon Attack: +3 to hit, range 100/400 ft., one target. Hit: 6 (1d10 + 1) piercing damage.

    **Fire Breath**: The veteran exhales fire in a 15-foot cone. Each creature in that area must make a DC 15 Dexterity saving throw, taking 24 (7d6) fire damage on a failed save, or half as much damage on a successful one.
    """

    name = "Half-Red Dragon Veteran"
    description = "Medium humanoid, any alignment"
    challenge_rating = 5
    armor_class = 18
    skills = ""
    senses = "Blindsight 10 ft., Darkvision 60 ft., Passive Perception 12"
    languages = "Common, Draconic"
    strength = Ability(16)
    dexterity = Ability(13)
    constitution = Ability(14)
    intelligence = Ability(10)
    wisdom = Ability(11)
    charisma = Ability(10)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 65
    hit_dice = "10d8"


class Harpy(Monster):
    """
    **Multiattack**: The harpy makes two attacks: one with its claws and one with its club.

    **Claws**: Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage.

    **Club**: Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage.

    **Luring Song**: The harpy sings a magical melody. Every humanoid and giant within 300 ft. of the harpy that can hear the song must succeed on a DC 11 Wisdom saving throw or be charmed until the song ends. The harpy must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the harpy is incapacitated.
    While charmed by the harpy, a target is incapacitated and ignores the songs of other harpies. If the charmed target is more than 5 ft. away from the harpy, the must move on its turn toward the harpy by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the harpy, a target can repeat the saving throw. A creature can also repeat the saving throw at the end of each of its turns. If a creature's saving throw is successful, the effect ends on it.
    A target that successfully saves is immune to this harpy's song for the next 24 hours.
    """

    name = "Harpy"
    description = "Medium monstrosity, chaotic evil"
    challenge_rating = 1
    armor_class = 11
    skills = ""
    senses = "Passive Perception 10"
    languages = "Common"
    strength = Ability(12)
    dexterity = Ability(13)
    constitution = Ability(12)
    intelligence = Ability(7)
    wisdom = Ability(10)
    charisma = Ability(13)
    speed = 20
    swim_speed = 0
    fly_speed = 40
    climb_speed = 0
    hp_max = 38
    hit_dice = "7d8"


class Hawk(Monster):
    """
    **Keen Sight**: The hawk has advantage on Wisdom (Perception) checks that rely on sight.

    **Talons**: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 slashing damage.
    """

    name = "Hawk"
    description = "Tiny beast, unaligned"
    challenge_rating = 0
    armor_class = 13
    skills = "Perception +4"
    senses = "Passive Perception 14"
    languages = ""
    strength = Ability(5)
    dexterity = Ability(16)
    constitution = Ability(8)
    intelligence = Ability(2)
    wisdom = Ability(14)
    charisma = Ability(6)
    speed = 10
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 1
    hit_dice = "1d4"


class HellHound(Monster):
    """
    **Keen Hearing and Smell**: The hound has advantage on Wisdom (Perception) checks that rely on hearing or smell.

    **Pack Tactics**: The hound has advantage on an attack roll against a creature if at least one of the hound's allies is within 5 ft. of the creature and the ally isn't incapacitated.

    **Bite**: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 7 (2d6) fire damage.

    **Fire Breath**: The hound exhales fire in a 15-foot cone. Each creature in that area must make a DC 12 Dexterity saving throw, taking 21 (6d6) fire damage on a failed save, or half as much damage on a successful one.
    """

    name = "Hell Hound"
    description = "Medium fiend, lawful evil"
    challenge_rating = 3
    armor_class = 15
    skills = "Perception +5"
    senses = "Darkvision 60 ft., Passive Perception 15"
    languages = "understands Infernal but can't speak it"
    strength = Ability(17)
    dexterity = Ability(12)
    constitution = Ability(14)
    intelligence = Ability(6)
    wisdom = Ability(13)
    charisma = Ability(6)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 45
    hit_dice = "7d8"


class Hezrou(Monster):
    """
    **Magic Resistance**: The hezrou has advantage on saving throws against spells and other magical effects.

    **Stench**: Any creature that starts its turn within 10 feet of the hezrou must succeed on a DC 14 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creature is immune to the hezrou's stench for 24 hours.

    **Multiattack**: The hezrou makes three attacks: one with its bite and two with its claws.

    **Bite**: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 15 (2d10 + 4) piercing damage.

    **Claws**: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.

    **Variant: Summon Demon**: The demon chooses what to summon and attempts a magical summoning.
    A hezrou has a 30 percent chance of summoning 2d6 dretches or one hezrou.
    A summoned demon appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other demons. It remains for 1 minute, until it or its summoner dies, or until its summoner dismisses it as an action.
    """

    name = "Hezrou"
    description = "Large fiend, chaotic evil"
    challenge_rating = 8
    armor_class = 16
    skills = ""
    senses = "Darkvision 120 ft., Passive Perception 11"
    languages = "Abyssal, telepathy 120 ft."
    strength = Ability(19)
    dexterity = Ability(17)
    constitution = Ability(20)
    intelligence = Ability(5)
    wisdom = Ability(12)
    charisma = Ability(13)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 136
    hit_dice = "13d10"


class HillGiant(Monster):
    """
    **Multiattack**: The giant makes two greatclub attacks.

    **Greatclub**: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18 (3d8 + 5) bludgeoning damage.

    **Rock**: Ranged Weapon Attack: +8 to hit, range 60/240 ft., one target. Hit: 21 (3d10 + 5) bludgeoning damage.
    """

    name = "Hill Giant"
    description = "Huge giant, chaotic evil"
    challenge_rating = 5
    armor_class = 13
    skills = "Perception +2"
    senses = "Passive Perception 12"
    languages = "Giant"
    strength = Ability(21)
    dexterity = Ability(8)
    constitution = Ability(19)
    intelligence = Ability(5)
    wisdom = Ability(9)
    charisma = Ability(6)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 105
    hit_dice = "10d12"


class Hippogriff(Monster):
    """
    **Keen Sight**: The hippogriff has advantage on Wisdom (Perception) checks that rely on sight.

    **Multiattack**: The hippogriff makes two attacks: one with its beak and one with its claws.

    **Beak**: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage.

    **Claws**: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage.
    """

    name = "Hippogriff"
    description = "Large monstrosity, unaligned"
    challenge_rating = 1
    armor_class = 11
    skills = "Perception +5"
    senses = "Passive Perception 15"
    languages = ""
    strength = Ability(17)
    dexterity = Ability(13)
    constitution = Ability(13)
    intelligence = Ability(2)
    wisdom = Ability(12)
    charisma = Ability(8)
    speed = 40
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 19
    hit_dice = "3d10"


class Hobgoblin(Monster):
    """
    **Martial Advantage**: Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 ft. of an ally of the hobgoblin that isn't incapacitated.

    **Longsword**: Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) slashing damage, or 6 (1d10 + 1) slashing damage if used with two hands.

    **Longbow**: Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target. Hit: 5 (1d8 + 1) piercing damage.
    """

    name = "Hobgoblin"
    description = "Medium humanoid, lawful evil"
    challenge_rating = 0.5
    armor_class = 18
    skills = ""
    senses = "Darkvision 60 ft., Passive Perception 10"
    languages = "Common, Goblin"
    strength = Ability(13)
    dexterity = Ability(12)
    constitution = Ability(12)
    intelligence = Ability(10)
    wisdom = Ability(10)
    charisma = Ability(9)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 11
    hit_dice = "2d8"


class Homunculus(Monster):
    """
    **Telepathic Bond**: While the homunculus is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically.

    **Bite**: Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or be poisoned for 1 minute. If the saving throw fails by 5 or more, the target is instead poisoned for 5 (1d10) minutes and unconscious while poisoned in this way.
    """

    name = "Homunculus"
    description = "Tiny construct, neutral"
    challenge_rating = 0
    armor_class = 13
    skills = ""
    senses = "Darkvision 60 ft., Passive Perception 10"
    languages = "understands the languages of its creator but can't speak"
    strength = Ability(4)
    dexterity = Ability(15)
    constitution = Ability(11)
    intelligence = Ability(10)
    wisdom = Ability(10)
    charisma = Ability(7)
    speed = 20
    swim_speed = 0
    fly_speed = 40
    climb_speed = 0
    hp_max = 5
    hit_dice = "2d4"


class HornedDevil(Monster):
    """
    **Devil's Sight**: Magical darkness doesn't impede the devil's darkvision.

    **Magic Resistance**: The devil has advantage on saving throws against spells and other magical effects.

    **Multiattack**: The devil makes three melee attacks: two with its fork and one with its tail. It can use Hurl Flame in place of any melee attack.

    **Fork**: Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 15 (2d8 + 6) piercing damage.

    **Tail**: Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 10 (1d8 + 6) piercing damage. If the target is a creature other than an undead or a construct, it must succeed on a DC 17 Constitution saving throw or lose 10 (3d6) hit points at the start of each of its turns due to an infernal wound. Each time the devil hits the wounded target with this attack, the damage dealt by the wound increases by 10 (3d6). Any creature can take an action to stanch the wound with a successful DC 12 Wisdom (Medicine) check. The wound also closes if the target receives magical healing.

    **Hurl Flame**: Ranged Spell Attack: +7 to hit, range 150 ft., one target. Hit: 14 (4d6) fire damage. If the target is a flammable object that isn't being worn or carried, it also catches fire.
    """

    name = "Horned Devil"
    description = "Large fiend, lawful evil"
    challenge_rating = 11
    armor_class = 18
    skills = ""
    senses = "Darkvision 120 ft., Passive Perception 13"
    languages = "Infernal, telepathy 120 ft."
    strength = Ability(22)
    dexterity = Ability(17)
    constitution = Ability(21)
    intelligence = Ability(12)
    wisdom = Ability(16)
    charisma = Ability(17)
    speed = 20
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 178
    hit_dice = "17d10"


class HunterShark(Monster):
    """
    **Blood Frenzy**: The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.

    **Water Breathing**: The shark can breathe only underwater.

    **Bite**: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage.
    """

    name = "Hunter Shark"
    description = "Large beast, unaligned"
    challenge_rating = 2
    armor_class = 12
    skills = "Perception +2"
    senses = "Darkvision 30 ft., Passive Perception 12"
    languages = ""
    strength = Ability(18)
    dexterity = Ability(13)
    constitution = Ability(15)
    intelligence = Ability(1)
    wisdom = Ability(10)
    charisma = Ability(4)
    speed = 0
    swim_speed = 40
    fly_speed = 0
    climb_speed = 0
    hp_max = 45
    hit_dice = "6d10"


class Hydra(Monster):
    """
    **Hold Breath**: The hydra can hold its breath for 1 hour.

    **Multiple Heads**: The hydra has five heads. While it has more than one head, the hydra has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious.
    Whenever the hydra takes 25 or more damage in a single turn, one of its heads dies. If all its heads die, the hydra dies.
    At the end of its turn, it grows two heads for each of its heads that died since its last turn, unless it has taken fire damage since its last turn. The hydra regains 10 hit points for each head regrown in this way.

    **Reactive Heads**: For each head the hydra has beyond one, it gets an extra reaction that can be used only for opportunity attacks.

    **Wakeful**: While the hydra sleeps, at least one of its heads is awake.

    **Multiattack**: The hydra makes as many bite attacks as it has heads.

    **Bite**: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) piercing damage.
    """

    name = "Hydra"
    description = "Huge monstrosity, unaligned"
    challenge_rating = 8
    armor_class = 15
    skills = "Perception +6"
    senses = "Darkvision 60 ft., Passive Perception 16"
    languages = ""
    strength = Ability(20)
    dexterity = Ability(12)
    constitution = Ability(20)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(7)
    speed = 30
    swim_speed = 30
    fly_speed = 0
    climb_speed = 0
    hp_max = 172
    hit_dice = "15d12"


class Hyena(Monster):
    """
    **Pack Tactics**: The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 ft. of the creature and the ally isn't incapacitated.

    **Bite**: Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage.
    """

    name = "Hyena"
    description = "Medium beast, unaligned"
    challenge_rating = 0
    armor_class = 11
    skills = "Perception +3"
    senses = "Passive Perception 13"
    languages = ""
    strength = Ability(11)
    dexterity = Ability(13)
    constitution = Ability(12)
    intelligence = Ability(2)
    wisdom = Ability(12)
    charisma = Ability(5)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 5
    hit_dice = "1d8"