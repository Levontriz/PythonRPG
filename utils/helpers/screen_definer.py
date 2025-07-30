def define_screens(game):
    main_menu = game.screen_manager.add_screen("base:mainMenu")
    main_menu.set_title("Welcome to PyPG")
    main_menu.add_option("Start", lambda: print("Starting game..."))
    main_menu.set_prompt("Select an option: ")
    main_menu.set_prompt_cursor("> ")