# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:20:07
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-06 14:54:35

import os
import configparser

class cfg_settings:

    def __init__(self):

        Config = configparser.ConfigParser()

        self.CFG_LOC = os.getcwd()
        self.CFG_FILE_NAME = 'settings.cfg'
        self.SECTION_NAME = 'qsAppManager'
        self.CFG_PATH = os.path.join(self.CFG_LOC,self.CFG_FILE_NAME)

        if not os.path.isfile(self.CFG_FILE_NAME):
            # Create the configuration file as it doesn't exist yet
            cfgfile = open(self.CFG_FILE_NAME, 'w')
            # Add content to the file
            Config.add_section(self.SECTION_NAME)
            Config.set(self.SECTION_NAME, 'host', 'qlik sense desktop location')
            Config.set(self.SECTION_NAME, 'app_name', 'Consumer Sales.qvf')
            Config.set(self.SECTION_NAME, 'app_config_file', os.path.join(self.CFG_LOC,'Qlik Sense Application Manager.xlsx'))
            Config.set(self.SECTION_NAME, 'user', 'user_name')
            Config.set(self.SECTION_NAME, 'passwd', 'password')
            Config.write(cfgfile)
            cfgfile.close()
            
        Config.read(self.CFG_FILE_NAME)
        self.host = Config.get(self.SECTION_NAME, 'host')
        self.app_name = Config.get(self.SECTION_NAME, 'app_name')
        self.app_config_file = Config.get(self.SECTION_NAME, 'app_config_file')
        self.user = Config.get(self.SECTION_NAME, 'user')
        self.passwd = Config.get(self.SECTION_NAME, 'passwd')

    def write_cfg_settings(self, cfg_item):
        Config = configparser.ConfigParser()
        Config.read(self.CFG_FILE_NAME)
        cfg_key, cfg_val = list(cfg_item.items())[0]
        Config.set(self.SECTION_NAME, cfg_key, cfg_val)
        with open(self.CFG_FILE_NAME, 'w') as configfile:
            Config.write(configfile)

def set_manager_file():
    x = cfg_settings()
    app_config_file = input('Enter the Absolute path and name of the application manager file:\n')
    x.write_cfg_settings({'app_config_file': app_config_file})

def set_target_application():
    x = cfg_settings()
    app_name = input('Enter the target Qlik Sense Application Name (case sensitivty is enabled):\n')
    x.write_cfg_settings({'app_name': app_name})

def set_host_credentials():   
    x = cfg_settings()
    host = input('To access a server enter the full url, otherwise the desktop can be accessed via localhost:\n')
    x.write_cfg_settings({'host': host})

def set_user_credentials(): 
    x = cfg_settings()
    user = input('Enter the user name for the server you are trying to access:\n')
    passwd = input('Enter the password for the server you are trying to access:\n')
    x.write_cfg_settings({'user': user})
    x.write_cfg_settings({'passwd': passwd})
