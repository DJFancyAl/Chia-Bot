import pathlib
import os
import yaml

def get_config():
    directory = pathlib.Path().resolve()
    file_name = 'config.yaml'
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Unable to find the config.yaml file. Expected location: {file_path}")
    f = open(file_path, 'r')
    config = yaml.load(stream=f, Loader=yaml.Loader)
    f.close()
    return config


def settings(config):
    settings = config.get('settings', None)
    return settings
