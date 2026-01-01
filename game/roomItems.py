from random import sample

# Class for defining different types of items in each room
class Items:

    # Room item generator
    def room_items(self, item_nums):
        axe = "Weapon of choice when it comes to Barbarians, your total damage is\
             increased by 20 now"
        sword = "Only fancy folk use Swords, and fancy folks can't do that\
            much damage. So your total damage is only increased by 15."
        bow = "A Bow, your total damage is increased by 30 you camper"
        dagger = "Dagger!!!, your damage is increase by 35 due to sneak factor"
        shield = "You get 20 more defensive points."
        chest_piece = "You fancy new armor, let's you take an extra\
             15 damage before dying"
        braces = "Kind of useless without the rest of your body being covered,\
            but it's still better than nothing. 10 extra defensive points for you"
        shin_guard = "Pretty useless even with the rest of your body covered. \
            5 extra defensive points is added anyways"
        health = "You have gained a health potion, you can use it later on if \
            needed to heal for 50."
        defense = "Defensive potion, instant 20 points added to your total armor."
        offense = "Offensive potions add an extra 5 damage to your total damage."
        objects = ["health", "defense", "offense", "shinGuard", "braces", "chestPiece"\
            "shield", "bow", "sword", "axe", "dagger"]
        return sample(objects, item_nums)
