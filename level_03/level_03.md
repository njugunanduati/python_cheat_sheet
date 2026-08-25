# LEVEL 03: Data Types
## 3.1 Built-in Types
```
int
float
complex
bool
str
list
tuple
set
frozenset
dict
NoneType
bytes
bytearray
```
### Check
```
x = 42

type(x)
```
### Better type checking
```
isinstance(x, int)
```

### Example 
Patient object
    |
    +-- name             str
    +-- age              int
    |
    +-- vitals           dict
    |     |
    |     +-- blood pressure -> tuple
    |     +-- temperature    -> float
    |     +-- pulse          -> int
    |
    +-- symptoms         set
    |
    +-- medications      list
    |
    +-- allergies        set