import configparser
import os

CONFIG_PATH = os.path.join('/home/pi/Public/neo_escan/setup', 'config.cfg')
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

version = "0.1.710"

config['DEFAULT']['version'] = version

# create tag ['DEFAULT']['last_update'] if not exists
if not config.has_option('DEFAULT', 'last_update'):
    config['DEFAULT']['last_update'] = '1710'
if not config.has_option('DEFAULT', 'next_update'):
    config['DEFAULT']['next_update'] = '1800'

with open(CONFIG_PATH, 'w') as configfile:
    config.write(configfile)
