from mods.default_mod import Mod

class AttackSimulator(Mod):
    def __init__(self):
        self.name = "AttackSimulator"
        self.looping = False
    def show_attack_screen(self, game):
        self.looping = True
        while self.looping:
            game.screen_manager.get_screen_by_identifier("AttackSimulator:simulator").display_screen()
    def close_attack_screen(self):
        self.looping = False

def init_mod(game):
    sim = AttackSimulator()
    attack_simulator = game.screen_manager.add_screen("AttackSimulator:simulator")
    attack_simulator.set_title("Attack Simulator")
    attack_simulator.add_option("Attack", lambda: print(game.combat_system.calculate_damage(game.character_system, None,
                                                                                            game.character_system.inventory[
                                                                                                "main_hand"])))
    attack_simulator.add_option("Increase Critical Chance", lambda: game.character_system.edit_stat("crit_chance",
                                                                                                    game.character_system.get_stat(
                                                                                                        "crit_chance") + 1))
    attack_simulator.add_option("Exit", lambda: sim.close_attack_screen())


    game.screen_manager.get_screen_by_identifier("base:mainMenu").add_option("Attack Simulator",
                                                                             lambda: sim.show_attack_screen(game))