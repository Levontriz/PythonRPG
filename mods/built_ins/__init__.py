from mods.default_mod import Mod
from mods.built_ins.screens import define_screens
from mods.built_ins.items import define_items

class BuiltIns(Mod):
    def __init__(self):
        print(self)
        self.items = []



def init_mod(game):
    system: BuiltIns = BuiltIns()
    define_screens(game)
    define_items(system)