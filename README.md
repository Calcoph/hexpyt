Convert your hexpat (ImHex's pattern language) scripts to python scripts.

You can see the documentation of the language [here](https://imhex.werwolv.net/docs/): [ImHex docs.](https://imhex.werwolv.net/docs/)

This project is incomplete so it won't parse entire scripts completely. It is not forgiving with the formatting of the input file, you can see valid input files in the `examples` folder. `bad_and_good_examples.pat` and `bad_and_good_examples.py` can act as a quick troubleshooting guide.

# Features
* Turn structs into python classes
* Turn bitfields into python classes
* Translate some basic expressions (manual intervention probably needed)
* Dollar class that works like ImHex's $
* @ operator that works like ImHex's @ (see [Using translated structs](#using-translated-structs))
* Read from multiple files at the same time (By making multiple Dollar objects)

Docstrings contain the original hexpat syntax. Image is from examples/bin_file.py

![Demostration of docstring in vscode with syntax highlighting](resources/HoverFile.png)

If you want syntax highlighting in vscode (like in the image), you can use [this extension](https://github.com/Calcoph/vscode-hexpat)

# Installation
Just download `main.py` and `primitives.py`. You will need a modern version of python3 (so at least it supports f-strings)

# Usage
## Usage of the translator
### Option 1
Import it into another python file and use the `translate_file` function. It's strongly recommended that you rename the file in that case
```python
from main import translate_file

translate_file("examples/bin_file.pat", "examples/bin_file.py")
```
### Option 2
Edit `main.py` to enter the file paths.

At the end of the file, after <if \_\_name\_\_ == "\_\_main\_\_">
```
input_file_path = ""
output_file_path = ""
```
Then run it
```console
> python main.py
```

## Usage of the translated files
The first thing you will need to do if you want to read a file is follow the instructions in the first lines of the translated file. It looks something like this:
```python
# Template to read from a file. follow the instructions.
# _dollar___offset has this name so it doesn't clash with others. Feel free to rename it. 
if True: # Change this from "if True" to "if False", then put the file path below.
    byts = b''
else:
    file_path = "" # Put the file path here and change the above "if True" to "if False".
    with open(file_path, "rb") as f:
        byts = f.read()
_dollar___offset = Dollar(0x00, byts)
# End of template
```

From this point on I'll assume you have renamed `_dollar___offset` to `dollar`

Run the file to make sure it has been translated correctly
```terminal
> python translated_file.py
```
If any error ocurs, solve it manually.

### Using translated structs
The syntaxis for this is similar to ImHex:
```python
new_var = MyStruct() @ dollar

# Or
new_var = MyStruct() @ Dollar(0x98, byts) # The @ operator doesn't work on python's ints, so you have to convert it to a Dollar

# Or
pointer = u8() @ Dollar(0x98, byts)
new_struct = MyStruct() @ pointer # This works since u8 is a hexpyt type that was created with a @ operator

# This won't work
pointer = u8(0x98) # u8 was created with a value, so it doesn't have a reference to "byts"
new_struct = MyStruct() @ pointer

# It's recommended to type hint so you can see the original hexpat definition by hovering over the type hint (on most IDEs/text editors)
new_var: MyStruct = MyStruct() @ dollar
```

Be careful with the order of operations, since @ has a high priority:
```python
new_var = MyStruct() @ dollar + 1 # Will crash, since it will do (MyStruct() @ dollar) + 1
new_var = MyStruct() @ (dollar + 1) # Works as expected
```
