from os import system, listdir, fsdecode

class SceneManager:
    scenes = dict()
    
    def run(id:str):
        if id not in SceneManager.scenes:
            raise OSError(f"Cannot run the scene {id} because it is not a valid ID.")
        SceneManager.scenes[id]._run()
        
    def init(path):
        # Get all .py files that "M_" in the front
        for file in listdir(path):
            filename = fsdecode(file)
            if filename.startswith("M_") and filename.endswith(".py"):
                module_name = filename[0:-3] 
                class_name = filename[2:-3]
                # Import and run the class
                module = __import__(module_name)
                getattr(module, class_name)()
            
class ChoiceScene:
    def __init__(self, id, title):
        if type(id) != type(""):
            raise OSError("The specified ID is not a string.")
        # {"TITLE": "option", "CALLBACK": functionAddress}
        self.__title = title
        self.__input_text = "Enter an option number: "
        self.__options = list()
        SceneManager.scenes[id] = self
        
    def setInputText(self, string):
        if type(string) != type(""):
            raise OSError("The specified value is not a string.")
        self.__input_text = string
        
    def setTitle(self, string):
        if type(string) != type(""):
            raise OSError("The specified value is not a string.")
        self.__title = string
        
    def addOption(self, title, callback=None):
        if callback == None:
            raise OSError(f"Callback for the '{title}' option has not been assigned")
        if type(callback) != type(self.addOption):
            raise OSError("Callback is not a function")
        if type(title) != type(""):
            raise OSError("Title is not a string.")
        
        self.__options.append({"TITLE":title,"CALLBACK":callback})
        
    def _run(self):
        system("cls")
        print("*"*20)
        print(self.__title)
        print("*"*20)
        for index, option in enumerate(self.__options):
            print(f"[{index}] {option['TITLE']}")
        print("*"*20)
        self.__options[int(input(self.__input_text))]["CALLBACK"]()

class CustomScene:
    def __init__(self, id):
        SceneManager.scenes[id] = self
        
    def _run(self):
        raise OSError("Your _run(self) function is not defined")
        
class MainMenu(CustomScene):
    def __init__(self):
        super().__init__("MainMenu")
        
    def _run(self):
        print("Running Right!")
        
class OptionText(ChoiceScene):
    def __init__(self):
        super().__init__("OptionText", "Option Title")
        self.addOption("Option 1", self.option1)
        self.addOption("Option 2", self.option2)
        
    def option1(self):
        print("Option 1 passed")
        
    def option2(self):
        print("Option 2 passed")
        
def main():
    classes = [MainMenu(), OptionText()]
    
    SceneManager.run("OptionText")
    
if __name__ == "__main__":
    main()