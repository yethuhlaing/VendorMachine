from typing import Callable, TypedDict
class MenuOption(TypedDict):
        description: str
        action: Callable
class Menu:
        title: str
        options: list[MenuOption]
        submenu: bool
        prompt: str
        def __init__(self, title: str = "Options:", options: list[MenuOption] = [], submenu: bool = False, prompt: str = "Your choice: ") -> None:
                # initialize menu options
                self.title = title
                self.options = options
                self.submenu = submenu
                self.prompt = prompt
                return None

        def start(self) -> None:
                # start menu-loop
                while True:
                        self.displayOptions()
                        choice = self.askChoice()
                        if choice == 0:
                                break
                        elif 1 <= choice <= len(self.options):
                                index = choice - 1
                                self.options[index]["action"]()
                        else:
                                print("Unknown option, try again!")
                        print()
                return None

        def displayOptions(self) -> None:
                print(self.title)
                for i, option in enumerate(self.options):
                        print(f"{i+1} {option['description']}")
                if self.submenu == True:
                        print("0 - Previous")
                else:
                        print("0 - Exit")
                return None

        def askChoice(self) -> int:
                choice = -1
                try:
                        feed = input(self.prompt)
                        choice = int(feed)
                except Exception:
                        choice = -1
                        # could be: pass
                return choice
