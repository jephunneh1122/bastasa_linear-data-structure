# ASSESSMENT 3.2 - QUEUE (FIFO)
# Name: JEPHUNNEH E. BASTASA

queue = []

# Enqueue letters
for letter in "BASTASA":
    queue.append(letter)

print("Queue (front to rear):", *queue)

# Dequeue letters
while len(queue) > 0:
    removed = queue.pop(0)
    print("Dequeue:", removed)

print("Queue is EMPTY.")