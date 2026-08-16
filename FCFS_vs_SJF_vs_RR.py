process = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4, 9]
]

n = len(process)


# ---------------- FCFS ----------------

fcfs = sorted(process, key=lambda x: x[1])

time = 0
total_TAT = 0
total_WT = 0

for p in fcfs:

    if time < p[1]:
        time = p[1]

    CT = time + p[2]
    TAT = CT - p[1]
    WT = TAT - p[2]

    time = CT

    total_TAT += TAT
    total_WT += WT

fcfs_TAT = total_TAT / n
fcfs_WT = total_WT / n


# ---------------- SJF ----------------

time = 0
completed = []
total_TAT = 0
total_WT = 0

while len(completed) < n:

    available = []

    for p in process:
        if p[1] <= time and p not in completed:
            available.append(p)

    if len(available) == 0:
        time += 1
        continue

    p = min(available, key=lambda x: x[2])

    time = time + p[2]

    CT = time
    TAT = CT - p[1]
    WT = TAT - p[2]

    total_TAT += TAT
    total_WT += WT

    completed.append(p)

sjf_TAT = total_TAT / n
sjf_WT = total_WT / n


# ---------------- ROUND ROBIN ----------------

quantum = 5
time = 0
queue = []
completed = []

remaining = {}
completion_time = {}

for p in process:
    remaining[p[0]] = p[2]

while len(completed) < n:

    for p in process:
        if p[1] <= time and p[0] not in queue and p[0] not in completed:
            queue.append(p[0])

    if len(queue) == 0:
        time += 1
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


total_TAT = 0
total_WT = 0

for p in process:

    CT = completion_time[p[0]]
    TAT = CT - p[1]
    WT = TAT - p[2]

    total_TAT += TAT
    total_WT += WT

rr_TAT = total_TAT / n
rr_WT = total_WT / n


# ---------------- COMPARISON ----------------

print("\n----- Comparison -----")

print("Algorithm\tAvg TAT\t\tAvg WT")

print("FCFS\t\t", round(fcfs_TAT, 2), "\t\t", round(fcfs_WT, 2))
print("SJF\t\t", round(sjf_TAT, 2), "\t\t", round(sjf_WT, 2))
print("Round Robin\t", round(rr_TAT, 2), "\t\t", round(rr_WT, 2))