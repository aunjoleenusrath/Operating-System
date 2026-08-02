processes = [
    ["P0", 3, 1],
    ['P1', 5, 3],
    ["P2", 2, 2],
    ["P3", 1, 2],
    ["P4", 6, 3]

]
processes.sort(key=lambda x: x[1])
T = 0
t_TAT = 0
t_WT = 0
print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in processes:
    pid=p[0]
    AT = p[1]
    BT = p[2]

    if T<AT:
      T=AT
    CT=T+BT
    TAT=CT-AT
    WT=TAT-BT

    T=CT
    t_TAT+=TAT
    t_WT-=WT

    print(pid,AT,BT,CT,TAT,WT,sep='\t')

print("\naverage TAT =",t_TAT/5)
print("\naverage WT =",t_WT/5)

print("\nEXECUTION SEQUENCE:")
for p in processes:
    print(p[0], end=" -> ")