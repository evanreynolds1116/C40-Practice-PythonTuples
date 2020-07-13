# Create a tuple named zoo that contains 10 of your favorite animals.

zoo = ("Great White Shark", "Grey Wolf", "Jaguar", "Black Panther", "Lion", "Tiger", "Black Bear", "Killer Whale", "Highland Cow", "French Bulldog")

# Find one of your animals using the tuple.index(value) syntax on the tuple
zoo.index("Grey Wolf")
print(f'{zoo.index("Grey Wolf")}')

# Determine if an animal is in your tuple by using value in tuple syntax

animal_to_find = "Highland Cow"
if animal_to_find in zoo:
    print(f'{animal_to_find} was found')
else: 
    print(f'{animal_to_find} not found')

# Convert your tuple into a list.

zoo_list = []
for animal in zoo:
    zoo_list.append(animal) 
print(f'{zoo_list}')

# Use extend() to add three more animals to your zoo.

zoo_list.extend(["Pug", "Dolphin", "Pitbull"])
print(f'{zoo_list}')

# Convert the list back into a tuple.

def convert(list):
    return tuple(list)
new_zoo = convert(zoo_list)
print(f'{new_zoo}')
