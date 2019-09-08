# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:39:10
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-09-05 17:42:18

from __init__ import *


def clearScr():
    os.system('cls' if os.name == 'nt' else 'clear')

settings = cfg_settings()

app_manager_prompt = "Qlik Sense Application Manager ~# "


appmanagerlogo = r'''                  
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |    ___       | || |   _____      | || |     _____    | || |  ___  ____   | |
| |  .'   '.     | || |  |_   _|     | || |    |_   _|   | || | |_  ||_  _|  | |
| | /  .-.  \    | || |    | |       | || |      | |     | || |   | |_/ /    | |
| | | |   | |    | || |    | |   _   | || |      | |     | || |   |  __'.    | |
| | \  `-'  \_   | || |   _| |__/ |  | || |     _| |_    | || |  _| |  \ \_  | |
| |  `.___.\__|  | || |  |________|  | || |    |_____|   | || | |____||____| | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'                     
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
            info()
        elif choice == "2":
            developer()
        elif choice == "3":
            retrieve_settings()
        else:
            sys.exit()

        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()


class info:
    menuLogo = r'''
 .----------------.  .-----------------. .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || | ____  _____  | || |  _________   | || |     ____     | |
| |    |_   _|   | || ||_   \|_   _| | || | |_   ___  |  | || |   .'    `.   | |
| |      | |     | || |  |   \ | |   | || |   | |_  \_|  | || |  /  .--.  \  | |
| |      | |     | || |  | |\ \| |   | || |   |  _|      | || |  | |    | |  | |
| |     _| |_    | || | _| |_\   |_  | || |  _| |_       | || |  \  `--'  /  | |
| |    |_____|   | || ||_____|\____| | || | |_____|      | || |   `.____.'   | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
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

class developer:
    menuLogo = r'''
.----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  ________    | || |  _________   | || | ____   ____  | |
| | |_   ___ `.  | || | |_   ___  |  | || ||_  _| |_  _| | |
| |   | |   `. \ | || |   | |_  \_|  | || |  \ \   / /   | |
| |   | |    | | | || |   |  _|  _   | || |   \ \ / /    | |
| |  _| |___.' / | || |  _| |___/ |  | || |    \ ' /     | |
| | |________.'  | || | |_________|  | || |     \_/      | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
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
    menuLogo = r'''
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |     ____     | || | ____  _____  | || |  _________   | || |     _____    | || |    ______    | |
| |   .' ___  |  | || |   .'    `.   | || ||_   \|_   _| | || | |_   ___  |  | || |    |_   _|   | || |  .' ___  |   | |
| |  / .'   \_|  | || |  /  .--.  \  | || |  |   \ | |   | || |   | |_  \_|  | || |      | |     | || | / .'   \_|   | |
| |  | |         | || |  | |    | |  | || |  | |\ \| |   | || |   |  _|      | || |      | |     | || | | |    ____  | |
| |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\   |_  | || |  _| |_       | || |     _| |_    | || | \ `.___]  _| | |
| |   `._____.'  | || |   `.____.'   | || ||_____|\____| | || | |_____|      | || |    |_____|   | || |  `._____.'   | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    '''

    def __init__(self):
        clearScr()
        settings = cfg_settings()

        print(self.menuLogo)
        print("\t{1}--Change the name and location of application manager file" + "......{}".format(settings.app_config_file))          
        print("\t{2}--Change target application..............................." + "......{}".format(settings.app_name))
        print("\t{3}--Change host credentials................................." + "......{}".format(settings.host))              
        print("\t{4}--Change user credentials................................." + "......{}".format(settings.user))
        print("\t{99}-Back To Main Menu \n")

        choice_update = input("\n" + app_manager_prompt)
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
