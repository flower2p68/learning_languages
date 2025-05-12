print("hello word")
name=input("what`s your name?")
# let just one whitespace(in case i put a lot of it.):
name=name.strip()
#capitalize the first letter:
name=name.capitalize()
#( but, i wanna all the firsts letter), use:
name=name.title()
name=input("what`s your name?").strip().title()
# If I wanna just the last name, I can put: first, last= name.split(), in the input instead of name, put last or first:
first, last= name.split()
print(f"hello, {first}") # or last
print(f"hello, {name}")


