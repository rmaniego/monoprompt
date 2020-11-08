from monoprompt.monoprompt import decorator, message, keys, ask, catalog, request

decorator("#")
message(" App Name ", padding="#")
message(" Sample Code ", padding="#")
decorator("#")
decorator(" ")

decorator("*")
selection = ("Apple", "Banana", "Cherries")
catalog(selection)
message(" x: Cancel")

decorator(".")
indices = keys(selection, extend=["x"])
selected = request("Select: ", indices)
decorator("-")

if selected != "x":
    item = selection[int(selected)]
    message(item, centered=True)
decorator("x")