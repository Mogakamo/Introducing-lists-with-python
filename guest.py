guests = ['Caesar', 'Willy', 'Dan']
guests.insert(3, "Amos")
guests.insert(4, "Caleb")
guests.insert(5, "Reagan")
guests.append("Sweet")

message = "I've found a bigger dinning table and so you are invited to the party."

print("Hey, you are welcomed, " + guests[0].title() + " to the party")
print("Hey, you are welcomed, " + guests[1].title() + " to the party")
print("Hey, you are welcomed, " + guests[3].title() + " to the party")

print("Sorry, " + guests[2].title() + " will not be attending the party")
