# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:39:10
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-04 21:32:52

from __init__ import *


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
       {1}--Application Information
       {2}--Developer Tools
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
        print("\t{5}--Generate Application Template")
        print("\t{99}-Back To Main Menu \n")
        choice_meta = input(app_manager_prompt)
        clearScr()
        if choice_meta == "1":
            print('export_master_Items()')  
        elif choice_meta == "2":
            print('export_fields()')
        elif choice_meta == "3":
            print('export_source_Tables()')
        elif choice_meta == "4":
            print('export_all()')
        elif choice_meta == "5":
            print('generate_app_template()')
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
        print("\t{1}--Update Selected Items")
        print("\t{2}--Update All Master Items and Variables")
        print("\t{99}-Back To Main Menu \n")
        choice_update = input(app_manager_prompt)
        clearScr()
        if choice_update == "1":
            print('update_selected_items')
        elif choice_update == "2":
            print('update_all()')
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
        print("\t{1}--Select the name and location of Application Manager file")          
        print("\t{2}--Select target application")
        print("\t{3}--Set Host Credentials")              
        print("\t{4}--Set User Credentials")
        print("\t{99}-Back To Main Menu \n\n")
        choice_update = input(app_manager_prompt)
        clearScr()
        if choice_update == "1":
            set_manager_file()
        elif choice_update == "2":
            set_target_application()
        elif choice_update == "3":
            set_host_credentials()    
        elif choice_update == "4":
            set_user_credentials()        
        elif choice_update == "99":
            main_menu()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()
x = main_menu()
