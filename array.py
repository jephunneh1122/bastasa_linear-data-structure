# ASSESSMENT 3.2 - ARRAY
# Name: JEPHUNNEH E. BASTASA

letters = []

# Add letters
for letter in "BASTASA":
    letters.append(letter)

print("Array:", *letters)

# Remove letters from the end
while len(letters) > 0:
    removed = letters.pop()
    print("Remove:", removed)

print("Array is EMPTY.")