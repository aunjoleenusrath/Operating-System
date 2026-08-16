process = [
    ["p1", 3, 3],
    ["p2", 2, 5],
    ["p3", 5, 4],
    ["p4", 1, 3],
    ["p5", 6, 2]
]

# ---------------- FCFS ----------------
process.sort(key=lambda x: x[1])

T = 0
fcfs_TAT = 0
fcfs_WT = 0

print("----- FCFS -----")
print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in process:
    if T < p[1]:
        T = p[1]

    CT = T + p[2]
    TAT = CT - p[1]
    WT = TAT - p[2]

    T = CT

    fcfs_TAT += TAT
    fcfs_WT += WT

    print(p[0], p[1], p[2], CT, TAT, WT, sep='\t')

fcfs_avg_TAT = fcfs_TAT / len(process)
fcfs_avg_WT = fcfs_WT / len(process)

print("\nAverage TAT =", fcfs_avg_TAT)
print("Average WT =", fcfs_avg_WT)

# ---------------- SJFs ----------------
time = 0
completed = []
sjfs_TAT = 0
sjfs_WT = 0

print("\n----- SJF -----")
print("PID\tAT\tBT\tCT\tTAT\tWT")

while len(completed) < len(process):

    available = []

    for p in process:
        if p[1] <= time and p not in completed:
            available.append(p)

    if len(available) == 0:
        time += 1
        continue

    shortest = min(available, key=lambda x: x[2])

    CT = time + shortest[2]
    TAT = CT - shortest[1]
    WT = TAT - shortest[2]

    sjfs_TAT += TAT
    sjfs_WT += WT

    time = CT
    completed.append(shortest)

    print(
        shortest[0],
        shortest[1],
        shortest[2],
        CT,
        TAT,
        WT,
        sep='\t'
    )

sjfs_avg_TAT = sjfs_TAT / len(process)
sjfs_avg_WT = sjfs_WT / len(process)

print("\nAverage TAT =", sjfs_avg_TAT)
print("Average WT =", sjfs_avg_WT)

# ---------------- Comparison ----------------
print("\n----- Comparison -----")

print("Algorithm\tAvg TAT\tAvg WT")
print("FCFS\t\t", fcfs_avg_TAT, "\t", fcfs_avg_WT)
print("SJFS\t\t", sjfs_avg_TAT, "\t", sjfs_avg_WT)

if sjfs_avg_WT < fcfs_avg_WT:
    print("\nSJFS gives better waiting time.")
elif fcfs_avg_WT < sjfs_avg_WT:
    print("\nFCFS gives better waiting time.")
else:
    print("\nBoth algorithms give the same waiting time.")