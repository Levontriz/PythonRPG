# filepath: c:\Users\WINDOWS\Desktop\Coding\PythonRPG\main.py

"""
Main game entry point.
Initializes and runs the game systems.
"""

from utils.helpers.mod_loader import ModLoader
from utils.helpers.menufy import ScreenManager, ScreenTypes, Screen
from core.character import Character
from core.combat import CombatSystem
from core.items import Items
from core.save_system import Save
from utils.helpers.screen_definer import define_screens

loop = True

class Game:
    def __init__(self):
        self.mod_loader = ModLoader()
        self.screen_manager = ScreenManager()
        self.character_system = Character()
        self.item_system = Items()
        self.save_system = Save()
        self.combat_system = CombatSystem()
        
    def initialize(self):
        """Initialize game systems and load mods."""
        print("Initializing game systems...")
        # Define all built-in screens
        define_screens(self)
        # Discover and load all mods
        self.mod_loader.discover_mods()
        # Initialize mods with game instance
        self.mod_loader.initialize_mods(self)
        # If available load character file
        self.save_system.load_all(self)
        main_menu: Screen = game.screen_manager.get_screen_by_identifier("base:mainMenu")
        main_menu.add_option("Exit", lambda: main_menu.close())
        print("Game initialization complete!")

    def run(self):
        """Main game loop."""
        self.initialize()

        # self.save_system.save_all(self)
        self.screen_manager.get_screen_by_identifier("base:mainMenu").display_screen()

        
if __name__ == "__main__":
    game = Game()
    game.run()