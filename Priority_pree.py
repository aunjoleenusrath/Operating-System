processes = [
    ["P1", 0, 3, 3],
    ["P2", 1, 4, 2],
    ["P3", 2, 6, 4],
    ["P4", 3, 4, 6],
    ["P5", 5, 2, 10]
]

n = len(processes)

remaining_bt = []
ct = [0] * n

for p in processes:
    remaining_bt.append(p[2])

time = 0
completed = 0

while completed < n:

    selected = -1
    highest_priority = 999


    for i in range(n):

        if processes[i][1] <= time and remaining_bt[i] > 0:

            if processes[i][3] < highest_priority:
                highest_priority = processes[i][3]
                selected = i


    if selected == -1:
        time += 1
        continue


    remaining_bt[selected] -= 1
    time += 1


    if remaining_bt[selected] == 0:
        ct[selected] = time
        completed += 1


total_wt = 0
total_tat = 0


print(f"{'P':<5}{'AT':<5}{'BT':<5}{'PR':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")

for i in range(n):

    pid = processes[i][0]
    at = processes[i][1]
    bt = processes[i][2]
    priority = processes[i][3]

    tat = ct[i] - at
    wt = tat - bt


    print(f"{pid:<5}{at:<5}{bt:<5}{priority:<5}{ct[i]:<5}{tat:<5}{wt:<5}")

    total_wt += wt
    total_tat += tat


print()

print(f"Average TAT = {total_tat / n:.2f}")
print(f"Average WT  = {total_wt / n:.2f}")