bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
# Accessing elements in a list
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Modifying Elements in a List
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles_1 = []
motorcycles_1.append('honda')
motorcycles_1.append('yamaha')
motorcycles_1.append('suzuki')
print(motorcycles_1)

# Inserting elements into a list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

# Removing elements from a list
del motorcycles[0]
print(motorcycles)

# Removing elements using pop() method
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f" The last motorcycle i owned was a {last_owned.title()}.")

# Popping items from any position in a List
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle i owned was a {first_owned.title()}.")
print(motorcycles) # The item we pop wont be available in List

# Removing an Item by Value
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")