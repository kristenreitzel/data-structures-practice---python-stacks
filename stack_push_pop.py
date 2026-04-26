# Simple stack demo using a Python list
# Operations: push (append) and pop (remove last item)
# Follows LIFO: Last In, First Out

stack = []

# push operations
stack.append("Dog")
stack.append("Puppy")
stack.append("Cat")

print("Initial stack:", stack)

first = stack.pop()   # removes "Cat"
second = stack.pop()  # removes "Puppy"

print("Popped items (in order):", first, second)
print("Stack after pops:", stack)  # should contain just "Dog"
