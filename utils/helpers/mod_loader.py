"""
Mod loader system.
Handles the loading and management of game modifications.
"""

import os
import importlib.util
import logging

class ModLoader:
    def __init__(self):
        self.loaded_mods = {}
        self.mod_order = []
        self.logger = logging.getLogger('mod_loader')

    def discover_mods(self, mods_directory='mods'):
        """
        Discover all available mods in the mods directory.
        Each mod should be in its own directory with an __init__.py file.
        """
        for mod_dir in os.listdir(mods_directory):
            mod_path = os.path.join(mods_directory, mod_dir)
            if os.path.isdir(mod_path):
                init_file = os.path.join(mod_path, '__init__.py')
                if os.path.exists(init_file):
                    self._load_mod(mod_dir, init_file)


    def _load_mod(self, mod_name, mod_file):
        """
        Load a single mod from file.
        """
        try:
            spec = importlib.util.spec_from_file_location(mod_name, mod_file)
            if spec is None:
                self.logger.error(f"Failed to load mod {mod_name}: Invalid module specification")
                return

            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

            if hasattr(mod, 'init_mod'):
                self.loaded_mods[mod_name] = mod
                self.mod_order.append(mod_name)
                self.logger.info(f"Successfully loaded mod: {mod_name}")
            else:
                self.logger.warning(f"Mod {mod_name} has no init_mod function, skipping")

        except Exception as e:
            self.logger.error(f"Error loading mod {mod_name}: {str(e)}")

    def initialize_mods(self, game_instance):
        """
        Initialize all loaded mods in order.
        """
        for mod_name in self.mod_order:
            mod = self.loaded_mods[mod_name]
            try:
                mod.init_mod(game_instance)
                self.logger.info(f"Initialized mod: {mod_name}")
            except Exception as e:
                self.logger.error(f"Error initializing mod {mod_name}: {str(e)}")
