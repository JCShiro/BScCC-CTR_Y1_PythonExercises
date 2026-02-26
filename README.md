# Python Exercises

This repository contains a series of exercises that will help understand the basics of python especially when working in the context of data analysis and ML. This document serves as a guide to navigate the repository that can be used alongside the exercises to better complete them. This repository is thought for students with a knowledge of JavaScript who are moving on to data analysis / ML with Python.

## General Python rules

Some general Python rules that vary from JavaScript are:

- Python uses `snake_case` as opposed to JavaScript's `cammelCase`
- Python **does not** use semicolonds at the end of a line -> in fact a semicolon will break the script
- Python uses indentation instead of curly brackets (`{ }`) to signify scope changes. We will see this in more detail at exercises in file **01** and **02**.

## Executing a Python script

To execute a python script:

- Open this repository in VSC
- At the top menu, select `Terminal` -> `New Terminal`
- To run a script, execute the command in the terminal:

```cmd
python3 name_of_script
```

For example, to execute `00_basics.py`, you would run from the terminal:

```cmd
python 00_basics.py
```

## 00_basics

In basics we learn how to print and assign different values to python variables. 
Key similarities and differences with JavaScript are listed here:

| Action | JavaScript Command | Python Command |
| ---- | ----- | ----- |
| print / display | `console.log()` | `print()` |
| create a variable | `let x = <value>` | `x = <value>` |
| string value | `"string"` or `'string'` | `"string"` or `'string'` |
| number value | `<number>` | `<number>` |
| boolean value | `true` / `false` | `True` / `False` |
| concatenate strings and numbers | `"This is a number:" + 1` | `"This is a number:" + str(1)` |

## 01_variables_and_functions

In Variables and Functions we learn how to operate with variables and functions as well as how to define and execute functions.

Defining a function in python is very different from defining a function in JavaScript.
In JavaScript, you may be used to seeing functions like so:

```JS

function doSomething() {
    let something = "something";
}

```

The equivalent function in python would be the following one:

```Python
def do_something():
    something = "something"
```

As you can see, the key differences are:

- A function is defined with the keyword `def`instead of `function`.
- A colon is added at the end of the function name.
- Instead of the curly bracket system, Python uses indentation to mark different scopes. This means that the following code would be wrong, and the `do_something`function would be detected as blank:

```Python
def do_something:
something = "something"
```

Whereas this function in JS would be acceptable:

```JS
function doSomething() {
let something = "something";
}
```

## 02_conditionals_and_loops
