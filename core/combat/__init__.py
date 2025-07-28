"""
Combat system module.
Handles all combat-related mechanics and calculations.
"""

class CombatSystem:
    def __init__(self):
        self.registered_combat_mods = []

    def register_mod(self, mod):
        """Register a combat modification from a mod."""
        self.registered_combat_mods.append(mod)

    def edit_combat_mod_data(self, mod_name, var_name, new_value):
        for mod in self.registered_combat_mods:
            print(mod)
            if mod.name == mod_name:
                mod.set_variable(var_name, new_value)
    def get_combat_mod_data(self, mod_name, var_name):
        for mod in self.registered_combat_mods:
            if mod.name == mod_name:
                return mod.get_variable(var_name)
        return None

    def calculate_damage(self, attacker, defender, item_used):
        """Base damage calculation that can be modified by mods."""
        base_damage = attacker.get_stat("strength")
        
        # Allow mods to modify damage calculation
        for mod in self.registered_combat_mods:
            if hasattr(mod, 'modify_damage'):
                base_damage = mod.modify_damage(base_damage, attacker, defender, item_used)
        
        return max(0, base_damage)
