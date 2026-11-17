# ASSESSMENT 3.2 - STACK (LIFO)
# Name: JEPHUNNEH E. BASTASA

stack = []

# Push letters into stack
for letter in "BASTASA":
    stack.append(letter)

print("Stack (bottom to top):", *stack)

# Pop letters from stack
while len(stack) > 0:
    removed = stack.pop()
    print("Pop:", removed)

print("Stack is EMPTY.")
