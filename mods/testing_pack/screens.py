from utils.helpers.menufy import *


def define_screens(game, sim):
    attack_simulator: Screen = game.screen_manager.add_screen("TestingPack:attackSimulator")
    attack_simulator.set_title("Attack Simulator")
    attack_simulator.add_option("Attack", lambda: print(game.combat_system.calculate_damage(game.character_system, None,
                                                                                            game.character_system.inventory[
                                                                                                "main_hand"])))
    attack_simulator.add_option("Increase Critical Chance", lambda: game.character_system.edit_stat("crit_chance",
                                                                                                    game.character_system.get_stat(
                                                                                                        "crit_chance") + 1))
    attack_simulator.add_option("Exit", lambda: attack_simulator.close())

    utilities_menu: Screen = game.screen_manager.add_screen("TestingPack:utilitiesMenu")
    utilities_menu.set_title("Utilities Menu")
    utilities_menu.add_option("Attack Simulator", lambda: attack_simulator.display_screen())
    utilities_menu.add_option("Get Character Crit Chance Stat", lambda: print(game.character_system.get_stat("crit_chance")))
    utilities_menu.add_option("List Items", lambda: game.item_system.list_items())
    utilities_menu.add_option("Exit", lambda: utilities_menu.close())

    # Add access to main menu
    game.screen_manager.get_screen_by_identifier("base:mainMenu").add_option("Utilities (testing_pack)",
                                                                             lambda: utilities_menu.display_screen())