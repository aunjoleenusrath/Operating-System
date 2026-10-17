pages = [1, 2, 3, 4, 2, 3, 1]
capacity = 3

frames = []
faults = 0

for page in pages:

    if page in frames:
        print(page, "->", frames, "Hit")

    else:
        faults += 1

        if len(frames) < capacity:
            frames.append(page)

        else:
            frames.pop(0)
            frames.append(page)

        print(page, "->", frames, "Fault")

print("Total Page Faults =", faults)