#0x00. AirBnB clone - The console

##Getting Started
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
cmd module
cmd module in depth
packages concept page
uuid module
datetime
unittest module
args/kwargs
Python test cheatsheet
cmd module wiki page
python unittest

##Learning Objectives

##General
-How to create a Python package
-How to create a command interpreter in Python using the cmd module
-What is Unit testing and how to implement it in a large project
-How to serialize and deserialize a Class
-How to write and read a JSON file
-How to manage datetime
-What is an UUID
-What is *args and how to use it
-What is **kwargs and how to use it
-How to handle named arguments in a function

##More Info
##Execution

Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

##Example Usage

