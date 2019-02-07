# swimmers-management-demo in Python3

## Introduction
This is the first question of the design pattern's project

---
## Question (Original)
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
## System Requirements (Setup Guide):
A **Python 3.X.X environment** is along with `python3-tkinter` module is required to run a working demo of the app with a support for a cross-platform graphical user-interface(tkinter).
### On Windows:
By default, a python3 installtion should install `tkinter` on your platform - and you should be good to go without any additional setup. 
### On Fedora (or similiar Linux Distributions that uses `yum` package manager):
install **Python 3.X.X**(the latest version) first (if not installed)
```bash
[root@linux ~]$ sudo yum install python3
```

next install `tkinter` for the GUI support
```bash
[root@linux ~]$ sudo yum install python3-tkinter
```
And assuming everything worked without a flaw, you should be able to use the system :)

### On other platforms
It is possible to use the app as long as you have a working python3 (with tkinter) environment. <br/>
If these requirements are not fulfilled, please refer to [this page](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) for a guide on how to setup the environment.

## How to run the demo:
### Step 1: `Clone` the project
You can manually install the zip file or do this from terminal using the Git utility
```bash
[root@linux ~]$ sudo git clone https://github.com/Design-Patterns-Project-Group/swimming-mangement-in-python.git
```

### Step 2: `cd` into the newly created directory
use cd/chdir from terminal or open the folder from GUI (Nautilus or Windows Explorer)
```bash
[root@linux ~]$ cd swimming-mangement-in-python/
```

### Step 3: Launch the program
You can do this multiple ways.
#### Option #1: Using `Python3` Interpretor on Terminal
The easy and most straight-forward way would be to ue python3 command from terminal
> Note: You must add python3 to your $PATH or environment variable to access python3
```bash
[root@linux swimming-mangement-in-python/]$ python3 main.py
```

#### Option #2: Using Linux Terminal
alternatively, you can `chmod` it to be executable and run (the shebang directive is set to `/usr/bin/python3`)

```bash
[root@linux swimming-mangement-in-python/]$ sudo chmod +x main.py
[root@linux swimming-mangement-in-python/]$ ./main.py
```

#### Options #3: Using a file explorer of your choice!
just **double-click** on the file on your favourite File Explorer(like Nautilus on linux or File Explorer on Windows Machines) as you would to open - lets say - MP4 movie.
> Note: You must associate the `.py` and other python related file extensions to the python3 interpretor before-hand for this method to work.

#### Other Alternatives
Other methods to run include:
* using IDEs
* IDLE
* Online Web Services
* etc...

## Proposed Answer
### Structure
```
project
│
│
└─── main.py
│
└─── [ models/   ]   -  contains abstractions of the entities/actors involved
│
└─── [ services/ ]   -  contains logic(like repo) that populates the models
│
└─── [ views/    ]   -  All the user interface stuff (GUI implementation)
 
...
```

> **Note:** for more detailed explanation/documentation goto each module's page 

---
## Group Members
* Tibebeselasie Mehari ([Github](https://github.com/TibebeJS))
* Yosef Worku ([Github](https://github.com/mozartofmath))
* Nahom Derese ([Github](https://github.com/NahomD))
