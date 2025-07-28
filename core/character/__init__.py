"""
Character system module.
Handles character creation, stats, and progression.
"""
class Character:
    def __init__(self):
        self.name = "None"
        self.stats = {}
        self.inventory = {}
        self.modifications = {}
        self.registered_character_mods = []
        self.initialize_base_stats()

    def initialize_base_stats(self):
        """Initialize basic character stats."""
        self.stats = {
            'health': 100,
            'strength': 10,
            'defense': 10,
        }
        self.inventory = {
            "main_hand": None,
            "off_hand": None,
            "armour": {
                "head": None,
                "body": None,
                "legs": None,
                "boots": None
            },
            "storage": []
        }

    def register_mod(self, mod):
        """Register a character modification from a mod."""
        self.registered_character_mods.append(mod)
        if hasattr(mod, 'on_character_init'):
            mod.on_character_init(self)

    def edit_character_mod_data(self, mod_name, var_name, new_value):
        for mod in self.registered_character_mods:
            print(mod)
            if mod.name == mod_name:
                mod.set_variable(var_name, new_value)

    def edit_modification(self, modification, value):
        self.modifications[modification] = value
    def edit_stat(self, stat, value):
        self.stats[stat] = value

    def get_stat(self, stat_name):
        """Get a stat value, allowing mods to modify it."""
        base_value = self.stats.get(stat_name, 0)
        
        # Allow mods to modify stat calculation
        for mod in self.registered_character_mods:
            if hasattr(mod, 'modify_stat'):
                base_value = mod.modify_stat(stat_name, base_value, self)
        
        return base_value


    def to_dict(self):
        data = {}
        # Only exclude specific attributes that shouldn't be serialized
        exclude_attrs = {'registered_character_mods'}

        for key, value in self.__dict__.items():
            if key.startswith("_") or key in exclude_attrs:
                continue

            # Handle objects with to_dict method
            if hasattr(value, 'to_dict') and callable(getattr(value, 'to_dict')):
                data[key] = value.to_dict()
            # Handle lists
            elif isinstance(value, list):
                serialized_list = []
                for item in value:
                    if hasattr(item, 'to_dict') and callable(getattr(item, 'to_dict')):
                        serialized_list.append(item.to_dict())
                    else:
                        # For lists, try to serialize everything, let JSON serialization handle errors
                        serialized_list.append(item)
                data[key] = serialized_list

            # Handle dictionaries (like your inventory with nested objects)
            elif isinstance(value, dict):
                data[key] = self._serialize_dict(value)

            # Handle everything else - let JSON serialization decide if it's valid
            else:
                data[key] = value

        return data

    def _serialize_dict(self, d):
        """Recursively serialize dictionary values."""
        result = {}
        for k, v in d.items():
            if hasattr(v, 'to_dict') and callable(getattr(v, 'to_dict')):
                result[k] = v.to_dict()
            elif isinstance(v, dict):
                result[k] = self._serialize_dict(v)
            elif isinstance(v, list):
                serialized_list = []
                for item in v:
                    if hasattr(item, 'to_dict') and callable(getattr(item, 'to_dict')):
                        serialized_list.append(item.to_dict())
                    else:
                        serialized_list.append(item)
                result[k] = serialized_list
            else:
                # Don't skip anything in dictionaries - include everything
                result[k] = v
        return result


