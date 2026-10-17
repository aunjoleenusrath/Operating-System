requests = [82, 170, 43, 140, 24, 16, 190]
head = 50


# ---------- FCFS ----------
fcfs_head = head
fcfs_seek = 0

for r in requests:
    fcfs_seek += abs(r - fcfs_head)
    fcfs_head = r


# ---------- SSTF ----------
sstf_head = head
sstf_seek = 0
data = requests.copy()

while data:
    closest = min(data, key=lambda x: abs(x - sstf_head))

    sstf_seek += abs(closest - sstf_head)

    sstf_head = closest
    data.remove(closest)


# ---------- Comparison ----------
print("FCFS Total Seek =", fcfs_seek)
print("SSTF Total Seek =", sstf_seek)

if fcfs_seek < sstf_seek:
    print("FCFS is better")
elif sstf_seek < fcfs_seek:
    print("SSTF is better")
else:
    print("Both are equal")