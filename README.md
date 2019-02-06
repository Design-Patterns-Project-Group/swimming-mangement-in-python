# swimmers-management-demo in Python3

## Introduction
This is the first question of the design pattern's project

---
## Question (unedited)
> **Q1)** Consider a database of a large number of swimmers in a league or statewide
organization. Each swimmer swims several strokes and distances throughout a season. The
best times for swimmers are tabulated by age group. Within a single four-month season,
many swimmers will have birthdays and therefore move into new age groups.<br/>
    **1.1.** Write a program which displays list of swimmers who did best in their age groups
in a given season<br/>
    **1.2.** sort it by sex, allow your program to be flexible enough to also be sorted by time
or by actual age rather than by age group without destroy the original data order.
(Display the original list at all times,probably on the right side of your contain)
---
## System Requirements:
A python 3 environment is required to run the project as well as a `python3-tkinter` installtion for a graphical user-interface support of the application.
### On Windows:
Just the python3 installtion should install `tkinter` on your platform as well. 
### On Fedora (or similiar Linux Distributions that uses `yum` package manager):
install python3 first (if not installed)
```bash
[root@linux ~]$ sudo yum install python3
```

next install `tkinter` for GUI
install python3 first (if not installed)
```bash
[root@linux ~]$ sudo yum install python3-tkinter
```
And you should be okay to use the system :)

### On other platforms
It is possible to use app as long as you have a working python3 environment and a tkinter support. <br/>
please refer to [this page](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) for a guide on how to setup the environment.

## Proposed Answer
### Structure
```
project
│
│   README.md
└─── models/     -  contains abstractionof the entities/actors involved in the system
│
└─── services/   -  contains logic that populates the models (think of them as Repositories for the models)
...
```

> **Note:** for more detailed explanation/documentation goto each module's page 

---
## Group Members
* Tibebeselasie Mehari ([Github](https://github.com/TibebeJS))
* Yosef Worku ([Github](https://github.com/mozartofmath))
* Nahom Derese ([Github](https://github.com/NahomD))
