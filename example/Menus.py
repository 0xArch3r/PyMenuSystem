from Menu import BaseMenu

class ThirdSubMenu:
    def __init__(self):
        self._menu = BaseMenu("Third Sub Menu")
        self._menu.append_to_menu(1,"Whatever","Tets")
        self._menu.append_to_menu(2,"Second Option","Tets")
        self._menu.append_to_menu(3,"Third Option","Tets")

    def run(self):
        x = self._menu.run_menu()
        if x == 99:
            return x

test = ThirdSubMenu()

class SecondSubMenu:
    def __init__(self):
        self._menu = BaseMenu("Second Sub Menu")
        self._menu.append_to_menu(1,"First Option",test)
        self._menu.append_to_menu(2,"Second Option","Tets")
        self._menu.append_to_menu(3,"Third Option","Tets")

    def run(self):
        x = self._menu.run_menu()
        if x == 99:
            return x

t=SecondSubMenu()

class FirstSubMenu:
    def __init__(self):
        self._menu = BaseMenu("First Sub Menu")
        self._menu.append_to_menu(1,"First Option",t)
        self._menu.append_to_menu(2,"Second Option","Tets")
        self._menu.append_to_menu(3,"Third Option","Tets")

    def run(self):
        x = self._menu.run_menu()
        if x == 99:
            return x
