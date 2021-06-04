"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability


class Quasit(Monster):
    """
    **Shapechanger**: The quasit can use its action to polymorph into a beast form that resembles a bat (speed 10 ft. fly 40 ft.), a centipede (40 ft., climb 40 ft.), or a toad (40 ft., swim 40 ft.), or back into its true form . Its statistics are the same in each form, except for the speed changes noted. Any equipment it is wearing or carrying isn't transformed . It reverts to its true form if it dies.

    **Magic Resistance**: The quasit has advantage on saving throws against spells and other magical effects.

    **Variant: Familiar**: The quasit can serve another creature as a familiar, forming a telepathic bond with its willing master. While the two are bonded, the master can sense what the quasit senses as long as they are within 1 mile of each other. While the quasit is within 10 feet of its master, the master shares the quasit's Magic Resistance trait. At any time and for any reason, the quasit can end its service as a familiar, ending the telepathic bond.

    **Claw (Bite in Beast Form)**: Melee Weapon Attack: +4 to hit, reach 5 ft ., one target. Hit: 5 (1d4 + 3) piercing damage, and the target must succeed on a DC 10 Constitution saving throw or take 5 (2d4) poison damage and become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.

    **Scare**: One creature of the quasit's choice within 20 ft. of it must succeed on a DC 10 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the quasit is within line of sight, ending the effect on itself on a success.

    **Invisibility**: The quasit magically turns invisible until it attacks or uses Scare, or until its concentration ends (as if concentrating on a spell). Any equipment the quasit wears or carries is invisible with it.
    """

    name = "Quasit"
    description = "Tiny fiend, chaotic evil"
    challenge_rating = 1
    armor_class = 13
    skills = "Stealth +5"
    senses = "Darkvision 120 ft., Passive Perception 10"
    languages = "Abyssal, Common"
    strength = Ability(5)
    dexterity = Ability(17)
    constitution = Ability(10)
    intelligence = Ability(7)
    wisdom = Ability(10)
    charisma = Ability(10)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 7
    hit_dice = "3d4"


class Quipper(Monster):
    """
    **Blood Frenzy**: The quipper has advantage on melee attack rolls against any creature that doesn't have all its hit points.

    **Water Breathing**: The quipper can breathe only underwater.

    **Bite**: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage.
    """

    name = "Quipper"
    description = "Tiny beast, unaligned"
    challenge_rating = 0
    armor_class = 13
    skills = ""
    senses = "Darkvision 60 ft., Passive Perception 8"
    languages = ""
    strength = Ability(2)
    dexterity = Ability(16)
    constitution = Ability(9)
    intelligence = Ability(1)
    wisdom = Ability(7)
    charisma = Ability(2)
    speed = 0
    swim_speed = 40
    fly_speed = 0
    climb_speed = 0
    hp_max = 1
    hit_dice = "1d4"
