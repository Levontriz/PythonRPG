from mods.default_mod import Mod
from mods.testing_pack.screens import define_screens

class AttackSimulator(Mod):
    def __init__(self):
        self.name: str = "TestingPack"
    @staticmethod
    def show_attack_screen(game):
        game.screen_manager.get_screen_by_identifier("TestingPack:attackSimulator").display_screen()

def init_mod(game):
    sim: AttackSimulator = AttackSimulator()

    define_screens(game, sim)