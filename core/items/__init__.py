class Items:
    def __init__(self):
        self.item_list = []
    def register_item(self, item):
        self.item_list.append(item)
    def edit_item_data(self, item_id):
        for list_item in self.item_list:
            if list_item.id == item_id:
                list_item.edit_data()
    def list_items(self):
        for list_item in self.item_list:
            print(list_item.display_name)
            print(list_item.id)
            print(list_item.description)
            print(list_item.craftable)
            print(list_item.recipe)
            if type(list_item) == Weapon:
                print(list_item.base_damage)
            print(list_item.modifications)
    def get_item_by_id(self, item_id):
        for list_item in self.item_list:
            if list_item.id == item_id:
                return list_item
        return None

#Default item class to be extended off
class Item:
    def __init__(self, display_name="Example Item", item_id="example:id", description="", craftable=False, recipe=None,
                 modifications=None):
        if modifications is None:
            modifications = {}
        self.display_name = display_name
        self.id = item_id
        self.description = description
        self.craftable = craftable
        self.recipe = recipe
        self.modifications = modifications

    def id(self):
        return self.id

    def set_variable(self, var_name, new_value):
        if hasattr(self, var_name):
            setattr(self, var_name, new_value)
            print(f"Changed {var_name} to {new_value}")
        else:
            print(f"Variable '{var_name}' doesn't exist")
        return self
