import os
import sys
import time

from variables import init
from dinky_dungeon import *

clear = lambda: os.system('cls')  
clear()

printBanner()
get_monster()
create_hero()
check_for_event()
#nav_menu()



