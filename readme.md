# Interpreter
This simple interpreter is developed using python and can interprete `*.my` files(Tried a custom extension).

We have two different version to use the interpreter. The first one just interprets from the hard coded input. To change the input, we need to change the value of `code` variable. And the other accepts files as input. We can write our code in a `*.my` file and tell the interpreter to interprate the file.

## 1. interpreter.py
To interprete using this interpreter, we need to run the command in the terminal: `python interpreter.py`.

To change the input, we need to change the value of the value of the `code` variable.

---

## 2. Interpreting *.my files
To interpret `*.my` files using this interpreter, we need python to be installed as our interpreter is designed in python. And we need to run the below command to interprate our `*.my` files
```python my_interpreter.py source.my```
Here `source.my` file contains our source code. And the above command should successfully interpret the `source.my` file and print the output in the terminal.