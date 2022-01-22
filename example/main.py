from Menu import BaseMenu

from Menus import FirstSubMenu, SecondSubMenu

s_menu = FirstSubMenu()
s2_menu = SecondSubMenu()

class TanOS:
    def __init__(self):
        self._loaded = False
        self._menu = BaseMenu("Main Menu")
        self._menu.append_to_menu(1, "Menu Item 1", s_menu)
        self._menu.append_to_menu(2, "Menu Item 2", s2_menu)
        self._menu.append_to_menu(3, "Menu Item 3", "test")
        self._menu.append_to_menu("blank1")
        self._menu.append_to_menu("A", "Menu Item A", "test")
        self._menu.append_to_menu("B", "Menu Item B", "test")
        self._menu.append_to_menu("blank4")
        self._menu.append_to_menu("H", "Help", "test")
        self._menu.append_to_menu("Z", "Logout", "test")


    def run_app(self):
        while True:
            self._menu.run_menu()
        

if __name__ == "__main__":
    app = TanOS()
    app.run_app()
