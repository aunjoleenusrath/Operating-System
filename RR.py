process = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4, 9]
]

quantum = 5
time = 0

queue = []
completed = []

remaining = {}
completion_time = {}

for p in process:
    remaining[p[0]] = p[2]

while len(completed) < len(process):

    for p in process:
        if p[1] <= time and p[0] not in queue and p[0] not in completed:
            queue.append(p[0])

    if len(queue) == 0:
        time = time + 1
        continue

    pid = queue.pop(0)

    run = min(quantum, remaining[pid])

    time = time + run
    remaining[pid] = remaining[pid] - run

    for p in process:
        if p[1] <= time and p[0] not in queue and p[0] not in completed and p[0] != pid:
            queue.append(p[0])

    if remaining[pid] > 0:
        queue.append(pid)


    else:
        completed.append(pid)
        completion_time[pid] = time

print("PID\tAT\tBT\tCT\tTAT\tWT")

total_TAT = 0
total_WT = 0

for p in process:
    pid = p[0]
    AT = p[1]
    BT = p[2]

    CT = completion_time[pid]
    TAT = CT - AT
    WT = TAT - BT

    total_TAT = total_TAT + TAT
    total_WT = total_WT + WT

    print(pid, AT, BT, CT, TAT, WT, sep="\t")

print("\nAverage TAT =", total_TAT / len(process))
print("Average WT =", total_WT / len(process))