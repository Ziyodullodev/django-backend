import yaml


def yaml_coerce(value):
    # Convert value to proper Python

    if isinstance(value, str):
        # yaml.load returns a Python object
        # (we are creating some quick YAML yaml data with a dummy key to make it valid YAML)
        # Converts string dict "{'apples': 1, 'bacon': 2}" to Pyton dict
        # Useful because we need to stringfy settings this way (like in Dockerfiles)
        return yaml.load(f'dummy: {value}', Loader=yaml.FullLoader)['dummy']
    return value
