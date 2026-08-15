
# LEVEL 00: Python Setup & Mental Model
## 0.1 Check Python
```bash
python --version
```
or:
```bash
python3 --version
```
### Run Python interactively:
```bash
python
```
### Run a script:
```bash
python app.py
```
### Run a module:
```bash
python -m module_name
```

## 0.2 Virtual Environment
### Create:
```bash
python -m venv .venv
```
### Activate on Windows:
```bash
.venv\Scripts\Activate.ps1
```
### macOS/Linux:
```bash
source .venv/bin/activate
```
### Install:
```bash
python -m pip install requests
```
### Deactivate:
```bash
deactivate
```

# LEVEL 01: Python Syntax Fundamentals
## 1.1 Hello World
```
print("Hello, World!")
```
### Multiple values:
```
print("Hello", "James")
```
### Separator
```
print("Hello", "James", sep=", ")
```
### End character:
```
print("Hello", end=" ")
print("James")
```
## 1.2 Comments
```
# This is a comment
x = 10  # This is also a comment
```
### Docstring:
```
def greet():
    """Return a greeting."""
    return "Hello"
```