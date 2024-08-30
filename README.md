# Scenes - Dylan Hartman
This is a library that allows you to create custom 'Scenes' into your terminal

## Tutorial
There are 3 classes you can use from this file. Two of them are helper classes and the last one is to run the scenes.

* ChoiceScene - A scene that adds choices for the user to pick
* CustomScene - Allows the programmer to make custom scenes
* SceneManager - The brains of the operation

### ChoiceScene class
This class allows the programmer to add choices for the user to pick between, with some text added to the top

The functions associated with this class
* addOption(option_text: str, callback:function_address)
*   option_text: str - The text displayed to the user to specifiy what this option is.
*   callback: function_address - This is the function that will be called when this option is activated.
---
* setTitle(text: str):
*   text: str - Changes the title of this scene
---
* setInputText(text: str):
*   text: str - Changes the input_text of this scene
---
*   

Here is a simple template you can follow.
```python
# M_MainMenu.py
class MainMenu(ChoiceScene):
  def __init__(self):
    super().__init__("MainMenu", "This is a pretty cool title")
    self.addOption("Option 1", self.option1)
    self.addOption("Option 2", self.option2)

  def option1(self):
    print("Option one passed")

  def option2(self):
    print("Option two passed")
```

Note:
1. The class name HAS to follow the file name, or the program wont recognize it. (Without the 'M_' and '.py')
2. The file name should start with a 'M_' and end with a '.py', or the program wont recognise it.
3. We must add 'super().__init__(...)' line under the __init__() function to get all of the parent class features.
