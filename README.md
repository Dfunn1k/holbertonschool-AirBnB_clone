<h1 align="center" >
<br>
    <img src="https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg" height="50%" width="30%">
</h1>

<h2 align="center">
    AirBnB (clone)
</h2>

<p align="center">
<img src="https://user-images.githubusercontent.com/68792144/141602345-7b71c4ea-a4dd-42d9-b706-7fc2c7b85ca5.png" height="50%" width="20%">
</p>

<p align="center">
    <a href="https://github.com/cristhian1107/printf/commits/main">
        <img src="https://img.shields.io/github/last-commit/cristhian1107/AirBnB_clone.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub last commit">
    </a>
    <a href="https://github.com/cristhian1107/printf/issues">
    <img src="https://img.shields.io/github/issues-raw/cristhian1107/AirBnB_clone.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub issues">
    </a>
    <a href="https://github.com/cristhian1107/printf/pulls">
    <img src="https://img.shields.io/github/issues-pr-raw/cristhian1107/AirBnB_clone.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub pull requests">
    </a>
</p>

<h4 align="center"> This project is WepApp in Python </h4>

<p align="center">
    <a href="#Description">Description</a> •
    <a href="#The console">The console</a> •
    <a href="#Contact Information">Contact Information</a> •
</p>

# Overview
This is first step for the project AirBnB-Clone called ´´The console´´.
First we create a command line interpreter like we did in Shell Project.
Then we have to manage Classes in order to create, show, update and destroy objects.

# Description
This project is the first step of the AirBnB project, which is an AirBnB clone that includes design, layout, infrastructure and database.

It consists of the implementation of a command line interface in the PYTHON programming language, which simulates the interaction with a RESTful API and data persistence. As well as basic functions such as create, show, update, destroy that simulate a CRUD (Create, Read, Update, Delete) of a lifetime towards a database.

We will not implement all the features, just some of them to cover all the fundamental concepts of the higher level programming track.

# The console

<p align="center"><img src="https://user-images.githubusercontent.com/68792144/141602516-90e36740-e66e-4edd-8baf-08f318b10a58.png" width="700"></p>

## Files Contained on this repository

| File | Description |
|--|--|
| **AUTHORS** | Contains the authors of the AirBnB-Clone Project. |
| **README.md** | Contains an overview of AirBnB-Clone Project. Important things that you should know before executes our AirBnB-Clone command line program. |
| **console.py** |  **HBNBCommand:** Class that defines the command line interpreter. **do_EOF:** command to exit the program. **do_quit:** command to exit the program. **emptyline:** when the line is empty does not perform any action. **do_precmd:** parses command input **help_help:** Prints help command description. **do_create:** Creates a new instance of BaseModel. **do_show:** Prints the string representation of an instance. **do_destroy** Deletes an instance based on the class name and id. **do_all** Prints all string representation of all instances. **do_update** Updates an instance by adding or updating its attribute. **do_count** counts number of instances of a class. |
| **models** | **engine** file storage directory. **__init__.py ** Create a unique FileStorage instance for your application. **amenity.py ** Class based on BaseModel. **base_model.py ** Base class that defines all common attributes/methods for other classes. **city.py ** Class based on BaseModel. **place.py ** Class based on BaseModel. **review.py ** Class based on BaseModel. **state.py ** Class based on BaseModel. **user.py ** Class based on BaseModel. |
| **tests** | **test_models** Test files directory. **__init__.py ** Packages the tests files. |

## Install
```shell
git clone https://github.com/BigDany1792/holbertonschool-AirBnB_clone
```

## Execution
`Interactive Mode`
 ```shell
 $ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
 ```
`Non-Interactive Mode`
```shell
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
```

## Commands
| CMD   | Description | Usage |
|--------|--------|--------|
| **`help`**   | Displays help manual and usage of command specified | `help` `<command>` <br> `help`|
| **`quit`**   | Exit the program | `quit` |
| **`EOF`**    | Exit the program | `EOF` <br>`Ctrl + D`|
| **`create`** | Creates new id for a new class | `create <class name>` |
| **`show`**   |  Prints the string representation of an instance based on the class name  | `show <class name> id`|
| **`destroy`**| Deletes an instance based on the class name and id | `destroy <class name> id`|
| **`all`**    | Prints all string representation of all instances based or not on the class name | `all` <br> `all <class name>`|
| **`update`** | Updates an instance based on the class name and id by adding or updating attribute | `update <class name> <id> <attribute> <value>` |


## Authors and Github

* **Please, read the [AUTHORS](https://github.com/BigDany1792/holbertonschool-AirBnB_clone) file**

# Contact Information
Please feel free to contact us regarding any matter (specially about mistakes, recomendations and gramar errors)

<p align="center">
Mauricio Carrasco -
<a href="https://github.com/mauricodev">
        <img src="https://img.shields.io/badge/Mauricio-mainPage-blue">
</a>
</p>



<p align="center">
Dany Chavez -
<a href="https://github.com/BigDany1792">
        <img src="https://img.shields.io/badge/Dany-mainPage-blue">
</a>

</p>