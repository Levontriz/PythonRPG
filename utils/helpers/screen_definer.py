def define_screens(game):
    main_menu = game.screen_manager.add_screen("base:mainMenu")
    main_menu.set_title("Welcome to PyPG")
    main_menu.add_option("Start", lambda: print("Starting game..."))
    main_menu.add_option("List Items", lambda: game.item_system.list_items())
    main_menu.add_option("Get Character Crit Chance Stat", lambda: print(game.character_system.get_stat("crit_chance")))
    main_menu.set_prompt("Select an option: ")
    main_menu.set_prompt_cursor("> ")