class Mod:
    def set_variable(self, var_name, new_value):
        if hasattr(self, var_name):
            setattr(self, var_name, new_value)
            print(f"Changed {var_name} to {new_value}")
        else:
            print(f"Variable '{var_name}' doesn't exist")

    def get_variable(self, var_name):
        if hasattr(self, var_name):
            return getattr(self, var_name)
        else:
            print(f"Variable '{var_name}' doesn't exist")
            return None