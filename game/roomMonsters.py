from random import sample

# Class to make monsters
class Monster:

    def enemies(self, item_nums):
        goblin = "They are just here for fun, but you keep attacking them. Seek help please."
        troll = "Fierce warriors hiding behind they mouse and keyboard."
        vampire = "Sad creatures dealing with stereotypes about how they are after your blood."
        zombie = "Super cool creatures, not after your brain if that's what you're thinking."
        monsters = ["goblin", "troll", "vampire", "zombie"]
        return sample(monsters, item_nums)