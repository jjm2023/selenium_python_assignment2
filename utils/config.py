import configparser

def read_config(key):
    config = configparser.ConfigParser()
    config.read('utils/config.properties')  # Path to your properties file

    # Access the value using the 'DEFAULT' section and the passed key
    try:
        value = config.get('DEFAULT', key)
        return value
    except KeyError:
        # If the key does not exist in the config file
        print(f"Error: Key '{key}' not found in the config file.")
        return None
