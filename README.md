# MyModules

A collection of reusable Python utility modules that I frequently use in my Python projects.

## Modules

### Md_ShowTheMenu

Displays a simple console menu with a custom title and user-defined options.

#### Example

```python
from Md_ShowTheMenu import show_menu

show_menu(
    "Main Menu",
    [
        "Start",
        "Settings",
        "Exit"
    ]
)
```

#### Output

```text
======= MAIN MENU =======
1. Start
2. Settings
3. Exit
----------------------------------------
```

---

### Md_Validators

Provides helper functions for validating user input.

#### Available Functions

##### get_yes_no()

Requests a yes/no answer from the user.

```python
answer = get_yes_no()
```

##### get_int(message)

Requests a valid integer value.

```python
age = get_int("Enter your age: ")
```

##### get_float(message)

Requests a valid float value.

```python
salary = get_float("Enter your salary: ")
```

---

### Md_WaitTime

Provides a countdown timer before program termination.

#### Example

```python
from Md_WaitTime import waitBeforeQuit

waitBeforeQuit(5)
```

#### Output

```text
The programme will be ended in 5 seconds...
The programme will be ended in 4 seconds...
The programme will be ended in 3 seconds...
The programme will be ended in 2 seconds...
The programme will be ended in 1 seconds...
```

---

## Purpose

The purpose of this repository is to build a personal Python utility library and avoid rewriting common code in every project.

New modules will be added over time as new reusable functions are developed.

## Author

Merve Tasali
