# AirBnB_clone

![image](https://user-images.githubusercontent.com/56034849/156102955-559f8659-bee1-44a6-9355-e4919fe8c097.png)

## Table of Contents

* [Description](#description)
* [Purpose](#purpose)
* [Installation](#installation)
* [Usage](#usage)
* [Usage Examples](#usage-examples)
* [Bugs](#bugs)
* [Authors](#authors)

## Description

The Airbnb clone project for which we are creating a copy of the Airbnb. This repository contains the code for one of the preliminary steps of this whole project: the console. 

## Purpose

The purpose of this project is to understand how to:  

* create a Python package   
* create a command interpreter using the `cmd` module   
* serialize and deserialize a Class   
* write and read a JSON file   
* manage `datetime`   
* use `*args` and `**kwargs`   
* handle named arguments in a function

## Installation
If you want to run the command interpreter follow the next steps:

    1. Clone the repository: git clone https://github.com/dmac24/AirBnB_clone/

    2. Access AirBnB_clone directory: cd AirBnB_clone
    
    3. Run: ./console.py

## Usage.
After you execute the console you can use the following commands:

    * quit - Exit the program.
    * EOF - Exit the program.
    * help - Gives a little description of a command.
    * create - Creates a new instance.
    * show - Prints the string representation of an instance based on the class name and id.
    * detroy - Deletes an instance based on the class name and id.
    * all - Prints all string representation of all instances based or not on the class name.
    * update - Updates an instance based on the class name and id by adding or updating attribute.

## Usage Examples

### Interactive Mode

```python3
~/me$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
~/me$
```

### Non-Interactive Mode

```python3
~/me$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

~/me$ cat test_help
help
~/me$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
~/me$
```

## Bugs

None reported so far.

## Authors

Daniel Cerón | [GitHub](https://github.com/DanielCeron-Holberton)  
Diana Ayala | [GitHub](https://github.com/dmac24)


