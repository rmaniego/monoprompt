# monoprompt
Decorate your command-line interface and simplify complex user input with an allowlist or blocklist.

## Install
```bash
pip install monoprompt
```

## Usage

**1. Import** 
```python
from monoprompt.monoprompt import ask, request, message, decorator, catalog, keys
```

**2. Ask an input from the user.** 
```python
# basic usage
ask("What is your name? ")

# removes extra characters
ask("What is your age? ", chars="3")

# allows empty input
ask("Where do you live? ", once=True)
```

**3. Request input and compare to allowed values.** 
```python
# basic usage
request("Choose a number? ", ("1", "2", "0"))

# allows only to choose between Apple, Banana, and Cherry, and never Durian
request("Select? ", ("Apple", "Banana", "Cherry"), blocklist=("Durian"))

# allows empty input
request("Select? ", ("Apple", "Banana", "Cherry", ""), blocklist=("Durian"))
```

**4. Decorate line with any characters.** 
```python
# fills the whole console line with the specified character
decorate("#")

# limits only to 50 characters in length
decorate("#", chars=50)

# fills the whole console line with the specified word, up to the max limit
decorate("hello")

# fills the whole console line with the specified word, up to a hundred characters
decorate("hello", 100)
```

**5. Print a message to the console.** 
```python
# basic usage
message(string)

# centers message in console
message(string, centered=True)

# centers message in a 50-character length
message(string, chars=50, centered=True)

# padds a string to the leading and trailing ends of the message
message(string, padding="#", centered=True)

# fills the leading and trailing white spaces with the specified character
message(string, chars=0, fill="-", centered=True)
```

**6. Print an ordered list.** 
```python
# basic usage
catalog(("Apple", "Banana", "Cherries"))

# or
selection = ("Apple", "Banana", "Cherries")
catalog(selection)
```

**7. Get indices of a list.** 
```python
# basic usage
indices = keys(("Apple", "Banana", "Cherries"))

# extend list
indices = keys(("Apple", "Banana", "Cherries"), extend=["x"])
```