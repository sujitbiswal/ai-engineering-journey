# 3-1. Names: Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a
#time
names = ['uma','sumit','shakti']
print(names[0])
print(names[1])
print(names[2])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of
#just printing each person’s name, print a message to them. The text of each
#message should be the same, but each message should be personalized
#with the person’s name.
names = ['uma','sumit','shakti']
msg = f"Hello, {names[0].title()}!"
print(msg)
msg = f"Hello, {names[1].title()}!"
print(msg)
msg = f"Hello, {names[2].title()}!"
print(msg)

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner,
#who would you invite? Make a list that includes at least three people you’d
#like to invite to dinner. Then use your list to print a message to each person,
#inviting them to dinner.
guests = ["sujit biswal",'sumit daya','varun kumar']

name = guests[0].title()
print(f"{name}, please come for dinner.")
name = guests[1].title()
print(f"{name}, please come for dinner.")
name = guests[2].title()
print(f"{name}, please come for dinner.")

# 3-5. Changing Guest List
guests = ["sujit biswal",'sumit daya','varun kumar']
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# sumit can't make it, lets invite pratik instead
del(guests[1])
guests.insert(1,'pratik rath')

# Print the invitations again

name = guests[0].title()
print(f"\n{name}, please come to dinner. ")

name = guests[1].title()
print(f"\n{name}, please come to dinner. ")

name = guests[2].title()
print(f"\n{name}, please come to dinner. ")

#3-6. More Guests
# we got a bigger table, so let's add more people to the list.
print("\nWe got bigger table!")

guests.insert(0,'ankit bhut')
guests.insert(2,'shasank mishra')
guests.append('swapna prakash')

name = guests[0].title()
print(f"{name}, please come to the dinner.")

name = guests[1].title()
print(f"{name}, please come to the dinner. ")

name = guests[2].title()
print(f"{name}, please come to the dinner. ")

name = guests[3].title()
print(f"{name}, please come to the dinner. ")

name = guests[4].title()
print(f"{name}, please come to the dinner. ")

name = guests[5].title()
print(f"{name}, please come to the dinner")

#3-7.Shrinking Guest List
# oh no, the table wont arrive on time!

print(f"\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# There should be two people left. Lets invite them
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner")

# Empty out the list.
del(guests[0])
del(guests[0])

print(guests)