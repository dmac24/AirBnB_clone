# AirBnB_clone

![image](https://user-images.githubusercontent.com/56034849/156102955-559f8659-bee1-44a6-9355-e4919fe8c097.png)

## Table of Contents

* [Description](#description)
* [Purpose](#purpose)
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


