processes = [
    ["P1", 0, 3, 3],
    ["P2", 1, 4, 2],
    ["P3", 2, 6, 4],
    ["P4", 3, 4, 6],
    ["P5", 5, 2, 10]
]

time = 0
total_wt = 0
total_tat = 0
completed = []


print(f"{'P':<5}{'AT':<5}{'BT':<5}{'PR':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")

while len(completed) < len(processes):

    ready = []


    for p in processes:
        if p[1] <= time and p not in completed:
            ready.append(p)


    if len(ready) == 0:
        time += 1
        continue


    ready.sort(key=lambda x: x[3])

    p = ready[0]

    pid = p[0]
    at = p[1]
    bt = p[2]
    priority = p[3]

    ct = time + bt
    tat = ct - at
    wt = tat - bt


    print(f"{pid:<5}{at:<5}{bt:<5}{priority:<5}{ct:<5}{tat:<5}{wt:<5}")

    time = ct
    total_wt += wt
    total_tat += tat


    completed.append(p)

print()

print(f"Average TAT = {total_tat / len(processes):.2f}")
print(f"Average WT  = {total_wt / len(processes):.2f}")