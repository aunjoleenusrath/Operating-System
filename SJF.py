process = [
    ["p1", 3, 3],
    ["p2", 2, 5],
    ["p3", 5, 4],
    ["p4", 1, 3],
    ["p5", 6, 2]
]

time = 0
completed = []
t_TAT = 0
t_WAT = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")

while len(completed) < 5:
    available =[]
    for p in process:
        if p[1]<=time and p not in completed:
            available.append(p)
    if len(available)==0:
        time += 1
        continue
    shortest=min(available,key=lambda x: x[2])

    pid = shortest[0]
    AT = shortest[1]
    BT = shortest[2]

    time = time + BT
    CT = time
    TAT = CT - AT
    WT = TAT - BT

    t_TAT += TAT
    t_WAT += WT

    completed.append(shortest)
    print(pid, AT, BT, CT, TAT, WT, sep='\t')

print("\naverage TAT =",t_TAT/5)
print("\naverage WT =",t_WAT/5)

print("\nEXECUTION SEQUENCE:")
for p in completed:
    print(p[0], end=" -> ")