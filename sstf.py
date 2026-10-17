requests = [82, 170, 43, 140, 24, 16, 190]
head = 50

total_seek = 0

while requests:

    closest = min(requests, key=lambda x: abs(x - head))

    seek = abs(closest - head)
    total_seek += seek

    print(head, "->", closest, "Seek =", seek)

    head = closest
    requests.remove(closest)

print("Total Seek Time =", total_seek)