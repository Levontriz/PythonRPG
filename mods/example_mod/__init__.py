"""
Example mod that adds a critical hit system to the game.
This demonstrates how to create a mod that interfaces with multiple core systems.
"""
from core.items import Item, Weapon
from mods.default_mod import Mod

class CriticalHitSystem(Mod):
    def __init__(self):
        self.name = "CriticalHitSystem"
        self.default_crit_chance = 0  # 15% chance for critical hit
        self.default_crit_multiplier = 2.0  # Double damage on crit
        self.new_item = Item("Test Item", "CriticalHitSystem:TestItem", "Test item for critical hit system!", False, None)
        self.new_weapon = Weapon("Crit Sword", "CriticalHitSystem:CritSword", "This sword has increased crit chance!", False, None, 10, {"crit_chance_increase": 1, "crit_multiplier_increase": 0})
    def name(self):
        return self.name

    @staticmethod
    def modify_damage(base_damage, attacker, defender, item_used):
        """Modify damage calculation to include critical hits."""
        from math import ceil
        import random
        crit_count = 0
        crit_chance = attacker.stats["crit_chance"] + item_used.modifications["crit_chance_increase"]
        crit_multiplier = attacker.stats["crit_multiplier"] + item_used.modifications["crit_multiplier_increase"]
        for i in range(ceil(crit_chance)):
            if random.random() < (crit_chance - i):
                crit_count += 1
                base_damage *= crit_multiplier
        if crit_count > 0:
            print(f"Critical hits: {crit_count}")
        return base_damage
    def on_character_init(self, character_system):
        character_system.edit_stat("crit_chance", self.default_crit_chance)
        character_system.edit_stat("crit_multiplier", self.default_crit_multiplier)
        character_system.inventory["main_hand"] = self.new_weapon


def init_mod(game):
    """Initialize the mod by registering with relevant systems."""
    crit_system = CriticalHitSystem()
    # Register with combat system
    game.item_system.register_item(crit_system.new_item)
    game.item_system.register_item(crit_system.new_weapon)
    game.character_system.register_mod(crit_system)
    game.combat_system.register_mod(crit_system)
    """This is also where you define your screens"""
    test_screen = game.screen_manager.add_screen("critSystem:test")
    test_screen.set_title("Test Screen")
    test_screen.add_option("Print", lambda: print("Test Screen"))
    test_screen.set_prompt("Sup")
    game.screen_manager.get_screen_by_identifier("base:mainMenu").add_option("Test Screen", lambda: game.screen_manager.get_screen_by_identifier("critSystem:test").display_screen())
    print("Critical Hit System mod initialized!")
