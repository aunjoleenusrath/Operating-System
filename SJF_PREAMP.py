processes = [
    ["P1", 4, 2],
    ["P2", 2, 2],
    ["P3", 1, 3],
    ["P4", 0, 6],
    ["P5", 3, 1],
]

quantum = 2
n = len(processes)

remaining = []

for p in processes:
    remaining.append(p[2])

ct = [0] * n

time = 0
completed = 0

while completed < n:

    selected = -1
    shortest = 999


    for i in range(n):

        if processes[i][1] <= time and remaining[i] > 0:

            if remaining[i] < shortest:
                shortest = remaining[i]
                selected = i



    if selected == -1:
        time += 1
        continue


    run_time = min(quantum, remaining[selected])

    remaining[selected] -= run_time
    time += run_time


    if remaining[selected] == 0:
        ct[selected] = time
        completed += 1



total_wt = 0
total_tat = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):

    pid = processes[i][0]
    at = processes[i][1]
    bt = processes[i][2]

    tat = ct[i] - at
    wt = tat - bt

    print(pid, at, bt, ct[i], tat, wt)

    total_wt += wt
    total_tat += tat


print("Average WT =", total_wt / n)
print("Average TAT =", total_tat / n)