def define_screens(game):
    main_menu = game.screen_manager.add_screen("base:mainMenu")
    main_menu.set_title("Welcome to PyPG")
    main_menu.add_option("Start", lambda: print("Starting game..."))
    main_menu.add_option("Attack Simulator", lambda: game.attack_simulator())
    main_menu.add_option("List Items", lambda: game.item_system.list_items())
    main_menu.add_option("Get Character Crit Chance", lambda: print(game.character_system.get_stat("crit_chance")))
    main_menu.add_option("Exit", lambda: print("Exiting..."))
    main_menu.set_prompt("Select an option: ")
    main_menu.set_prompt_cursor("> ")

    attack_simulator = game.screen_manager.add_screen("base:attackSimulator")
    attack_simulator.set_title("Attack Simulator")
    attack_simulator.add_option("Attack", lambda: print(game.combat_system.calculate_damage(game.character_system, None,
                                                                                            game.character_system.inventory["main_hand"])))
    attack_simulator.add_option("Increase Critical Chance", lambda: game.character_system.edit_stat("crit_chance",
                                                                                                    game.character_system.get_stat(
                                                                                                        "crit_chance") + 1))
    attack_simulator.add_option("Exit", lambda: game.loop_false())