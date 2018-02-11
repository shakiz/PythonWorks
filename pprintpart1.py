import pprint

message="My name is shakil and i am from barisal."

count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)
