import re

identifier = "levon:booth123wow"

pattern = re.compile(r"^[a-zA-Z0-9]+:[a-zA-Z0-9]+$")
valid_identifier = True if pattern.match(identifier) is not None else False
if not valid_identifier:
    raise ValueError("Identifier must be in the format 'namespace:identifier'.")

