class Save:
    def __init__(self):
        import pathlib
        self.save_location = f"{pathlib.Path(__file__).resolve().parent}/save_data.pkl"

    def save_all(self, game):
        import pickle
        try:
            # Store the original mod lists
            character_mods = game.character_system.registered_character_mods
            combat_mods = game.combat_system.registered_combat_mods
            
            # Temporarily remove mod references
            game.character_system.registered_character_mods = []
            game.combat_system.registered_combat_mods = []
            
            # Create a data structure for saving
            save_data = {
                'stats': game.character_system.stats,
                'inventory': game.character_system.inventory,
                'modifications': game.character_system.modifications,
                'name': game.character_system.name
            }
            
            # Save using pickle
            with open(self.save_location, 'wb') as f:
                pickle.dump(save_data, f)
                
            # Restore the mod lists
            game.character_system.registered_character_mods = character_mods
            game.combat_system.registered_combat_mods = combat_mods
            
            print("Game saved successfully!")
            
        except Exception as e:
            print(f"Error saving game: {e}")
            # Ensure mod lists are restored even if save fails
            if 'character_mods' in locals():
                game.character_system.registered_character_mods = character_mods
            if 'combat_mods' in locals():
                game.combat_system.registered_combat_mods = combat_mods

    def load_all(self, game):
        """Load all game data."""
        import pickle
        try:
            with open(self.save_location, 'rb') as f:
                save_data = pickle.load(f)
            
            # Update character system with loaded data
            game.character_system.stats = save_data['stats']
            game.character_system.inventory = save_data['inventory']
            game.character_system.modifications = save_data['modifications']
            game.character_system.name = save_data['name']
            
            print("Game loaded successfully!")
            
        except Exception as e:
            print(f"Error loading game: {e}")
            # In case of error, initialize with default values
            game.character_system.initialize_base_stats()