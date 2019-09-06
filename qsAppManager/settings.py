# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:20:07
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-06 14:54:35

import os
import configparser
import io


CFG_LOC = os.getcwd()
CFG_FILE_NAME = 'settings.cfg'
SECTION_NAME = 'qsAppManager'

def create_cfg():
    # Check if there is already a configurtion file
    if not os.path.isfile(os.path.join(CFG_LOC,CFG_FILE_NAME)):
        # Create the configuration file as it doesn't exist yet
        cfgfile = open(CFG_FILE_NAME, 'w')
        # Add content to the file
        Config = configparser.ConfigParser()
        Config.add_section(SECTION_NAME)
        Config.set(SECTION_NAME, 'host', 'localhost')
        Config.set(SECTION_NAME, 'app_name', 'Consumer Sales.qvf')
        Config.set(SECTION_NAME, 'app_config_file', os.path.join(CFG_LOC,'Qlik Sense Application Manager.xlsx'))
        Config.set(SECTION_NAME, 'user', 'user_name')
        Config.set(SECTION_NAME, 'passwd', 'password')
        Config.write(cfgfile)
        cfgfile.close()

def write_cfg_settings(cfg_item):
    config = configparser.ConfigParser()
    config.read(CFG_FILE_NAME)
    cfg_key, cfg_val = list(cfg_item.items())[0]
    config.set(SECTION_NAME, cfg_key, cfg_val)
    with open(CFG_FILE_NAME, 'w') as configfile:
        config.write(configfile)

def set_manager_file():
    app_config_file = input('Enter the Absolute path and name of the application manager file:\n')
    write_cfg_settings({'app_config_file': app_config_file})

def set_target_application():
    app_name = input('Enter the target Qlik Sense Application Name (case sensitivty is enabled):\n')
    write_cfg_settings({'app_name': app_name})

def set_host_credentials():   
    host = input('To access a server enter the full url, otherwise the desktop can be accessed via localhost:\n')
    write_cfg_settings({'host': host})

def set_user_credentials(): 
    user = input('Enter the user name for the server you are trying to access:\n')
    passwd = input('Enter the password for the server you are trying to access:\n')
    write_cfg_settings({'user': user})
    write_cfg_settings({'passwd': passwd})


class cfg_settings:

    def __init__(self):
        create_cfg()
        config = configparser.ConfigParser()
        config.read(CFG_FILE_NAME)
        self.host = config.get(SECTION_NAME, 'host')
        self.app_name = config.get(SECTION_NAME, 'app_name')
        self.app_config_file = config.get(SECTION_NAME, 'app_config_file')
        self.user = config.get(SECTION_NAME, 'user')
        self.passwd = config.get(SECTION_NAME, 'passwd')