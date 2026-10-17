requests = [0, 14, 30, 41, 50, 62, 79, 100, 114]
head = 50

total_movement = 0
print("head movement:")

for requests in requests:
    movement = abs(requests - head)

    print(head, "->", requests, "=", movement)

    total_movement += movement
    head = requests

print("Total Head Movement =" , total_movement)