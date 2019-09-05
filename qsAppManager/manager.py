# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:39:10
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-04 20:07:21
import os
import sys


def clearScr():
    os.system('cls' if os.name == 'nt' else 'clear')


app_manager_prompt = "Qlik App Manager ~# "


appmanagerlogo = '''                  
              .d88b.    88     88  88   dP   
             .8P  Y8.   88         88  dP
             88    88   88     88  88odP
             88    88   88     88  88"Yb
             `8b  d8R   88     88  88  Yb
              `Y88P'QR  88888  88  88   Yb
    '''


class main_menu:
    def __init__(self):
        clearScr()
        print(appmanagerlogo + '''
       }--------------{+} Powered By SDG Group {+}--------------{
       }--------------{+}     sdggroup.com     {+}--------------{
    ''' + '''
       {1}--Retrieve Application's Meta Data
       {2}--Update Application's Master Items and Variables
       {3}--Settings
       {99}-EXIT\n
     ''')
        choice = input(app_manager_prompt)
        if choice == "1":
                meta_data()
        elif choice == "2":
            update_calculations()
        elif choice == "3":
            retrieve_settings()
        else:
            sys.exit()

        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()


class meta_data:
    menuLogo = '''
        8b    88  888888  888888    db
        88b  d88  88__      88     dPYb
        88YbdP88  88""      88    dP__Yb
        88 YY 88  888888    88   dP""""Yb
    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print("\t{1}--Export Master Items")
        print("\t{2}--Export Fields")
        print("\t{3}--Export Source Tables")
        print("\t{4}--Export All")
        print("\t{5}--Generate Template")
        print("\t{6}--Generate Existing Application File")
        print("\t{99}-Back To Main Menu \n")
        choice_meta = input(app_manager_prompt)
        clearScr()
        if choice_meta == "1":
            print('Export_Master_Items()')  
        elif choice_meta == "2":
            print('Export_Fields()')
        elif choice_meta == "3":
            print('Export_Source_Tables()')
        elif choice_meta == "4":
            print('Export_All()')
        elif choice_meta == "5":
            print('Generate_Template()')
        elif choice_meta == "6":
            print('Generate_File()')
        elif choice_meta == "99":
            main_menu()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()

class update_calculations:
    menuLogo = '''
        88   88  88""Yb  8888B      db     888888  888888
        88   88  88__dP  88  Yb    dPYb      88    88__
        Y8   8P  88"""   88  dY   dP__Yb     88    88""
        `YbodP'  88      888y"   dP""""Yb    88    888888
    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print("\t{1}--Partial Update Master Items")
        print("\t{2}--Partial Update Variables")
        print("\t{3}--Partial Update All")
        print("\t{4}--Full Update Master Items")
        print("\t{5}--Full Update Variables")
        print("\t{6}--Full Update All")
        print("\t{99}-Back To Main Menu \n")
        choice_update = input(app_manager_prompt)
        clearScr()
        if choice_update == "1":
            print('Partial_Update_Master_Items()')
        elif choice_update == "2":
            print('Partial_Update_Variables()')
        elif choice_update == "3":
            print('Partial_Update_All()')
        elif choice_update == "4":
            print('Full_Update_Master_Items()')
        elif choice_update == "5":
            print('Full_Update_Variables()')
        elif choice_update == "6":
            print('Full_Update_All()')
        elif choice_update == "99":
            main_menu()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()
    
    
class retrieve_settings:
    menuLogo = '''
        88   88  88""Yb  8888B      db     888888  888888
        88   88  88__dP  88  Yb    dPYb      88    88__
        Y8   8P  88"""   88  dY   dP__Yb     88    88""
        `YbodP'  88      888y"   dP""""Yb    88    888888
    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)
        print("\t{1}--Select a Configuration File")
        print("\t{2}--Select a target application")
        print("\t{3}--Select a platform")
        print("\t{99}-Back To Main Menu \n")
        choice_update = input(app_manager_prompt)
        clearScr()
        if choice_update == "1":
            print('Config_File()')
        elif choice_update == "2":
            print('Target_App()')
        elif choice_update == "3":
            print('Platform()')        
        elif choice_update == "99":
            main_menu()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()
x = main_menu()
