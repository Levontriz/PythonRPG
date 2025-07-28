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
    def __init__(self, display_name="Example Item", itemid="example:id", description="", craftable=False, recipe=None,
                 modifications=None):
        if modifications is None:
            modifications = {}
        self.display_name = display_name
        self.id = itemid
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

    def to_dict(self):
        """Convert item to dictionary for serialization."""
        data = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                continue

            # Handle nested objects with to_dict method
            if hasattr(value, 'to_dict') and callable(getattr(value, 'to_dict')):
                data[key] = value.to_dict()

            # Handle lists
            elif isinstance(value, list):
                serialized_list = []
                for item in value:
                    if hasattr(item, 'to_dict') and callable(getattr(item, 'to_dict')):
                        serialized_list.append(item.to_dict())
                    else:
                        serialized_list.append(item)
                data[key] = serialized_list

            # Handle dictionaries
            elif isinstance(value, dict):
                data[key] = self._serialize_dict(value)

            # Handle basic types
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
                result[k] = v
        return result


class Weapon(Item):
    def __init__(self, display_name="Example Item", id="example:id", description="", craftable=False, recipe=None,
                 base_damage=1, modifications={}):
        super().__init__(display_name, id, description, craftable, recipe, modifications)
        self.base_damage = base_damage

    def register_modifier(self, namespace, modifier_to_add, value):
        self.modifications[namespace][modifier_to_add] = value
        return self
