import configparser

class FileOps:
    @staticmethod
    def read_config_properties(file='config.ini'):
        config = configparser.ConfigParser()

        # Read the properties file
        config.read(file)

        # Print all sections and options to debug
        #print(config.sections())  # This will print out the section names
        #print(config.options("default"))  # This will print out the options under the 'DEFAULT' section

        # Return the values as a dictionary
        return {
            "base_url": config.get("default", "base_url"),
            "username": config.get("default", "username"),
            "password": config.get("default", "password")
        }
