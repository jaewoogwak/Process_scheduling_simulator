'''
# AT(arriveTime), BT(BurstTime), RT(RemainingTime), WT(waitingTime), TT(TurnaroundTime), NTT(Normalized Turnaround Time)
processList = {'p1':[0, 3, 0, 0, 0], 'p2':[1, 7, 0, 0, 0], 'p3':[3, 2, 0, 0, 0], 'p4':[5, 5, 0, 0, 0], 'p5':[6, 3, 0, 0, 0]}
quantum = 2

# AT(arriveTime), BT(BurstTime), RT(RemainingTime), WT(WaitingTime), TT(Turnaroundtime), NTT(Normalized Turnaround Time)
for key, value in processList.items():
    processList[key] = {'AT': value[0], 'BT': value[1], 'WT': value[2], 'TT': value[3], 'NTT': value[4]}

queue = []
time = 0

# 각 프로세스의 AT, BT, RT, WT, TT, NTT 값을 계산합니다.
for key in processList:
    process = processList[key]
    process['RT'] = process['BT']
    process['WT'] = 0
    process['TT'] = 0
    process['NTT'] = 0

# 프로세스를 큐에 추가하고, 실행시간을 계산합니다.
while True:
    for key in processList:
        process = processList[key]
        if process['AT'] <= time and process['RT'] > 0 and key not in queue:
            queue.append(key)

    if not queue:
        break

    currentProcess = queue.pop(0)
    process = processList[currentProcess]
    if process['RT'] <= quantum:
        time += process['RT']
        process['WT'] = time - process['AT'] - process['BT']
        process['TT'] = time - process['AT']
        process['NTT'] = process['TT'] / process['BT']
        process['RT'] = 0
    else:
        time += quantum
        process['RT'] -= quantum
        process['WT'] = time - process['AT'] - process['BT']
        process['TT'] = time - process['AT']
        process['NTT'] = process['TT'] / process['BT']
        queue.append(currentProcess)

    for key in processList:
        process = processList[key]
        if process['AT'] > time or process['RT'] == 0:
            continue
        if key not in queue and key != currentProcess:
            process['WT'] += quantum

print("Process\tAT\tBT\tWT\tTT\tNTT")
for key in processList:
    process = processList[key]
    print("{}\t{}\t{}\t{}\t{}\t{}".format(key, process['AT'], process['BT'], process['WT'], process['TT'], round(process['NTT'], 2)))
totalTT = sum([processList[key]['TT'] for key in processList])
averageTT = totalTT / len(processList)
print("Average response time:", round(averageTT, 2))

'''

def RR(process, arrival_time, burst_time, quantum=2):
    processList = {}
    for i in range(process):
        processList[f'P{i+1}'] = {'AT': arrival_time[i], 'BT': burst_time[i], 'RT': burst_time[i], 'WT': 0, 'TT': 0, 'NTT': 0}

    queue = []
    time = 0

    while True:
        for key in processList:
            process = processList[key]
            if process['AT'] <= time and process['RT'] > 0 and key not in queue:
                queue.append(key)

        if not queue:
            break

        currentProcess = queue.pop(0)
        process = processList[currentProcess]
        if process['RT'] <= quantum:
            time += process['RT']
            process['WT'] = time - process['AT'] - process['BT']
            process['TT'] = time - process['AT']
            process['NTT'] = process['TT'] / process['BT']
            process['RT'] = 0
        else:
            time += quantum
            process['RT'] -= quantum
            process['WT'] = time - process['AT'] - process['BT']
            process['TT'] = time - process['AT']
            process['NTT'] = process['TT'] / process['BT']
            queue.append(currentProcess)

        for key in processList:
            process = processList[key]
            if process['AT'] > time or process['RT'] == 0:
                continue
            if key not in queue and key != currentProcess:
                process['WT'] += quantum

    print("Process\tAT\tBT\tWT\tTT\tNTT")
    for key in processList:
        process = processList[key]
        print("{}\t{}\t{}\t{}\t{}\t{}".format(key, process['AT'], process['BT'], process['WT'], process['TT'], round(process['NTT'], 2)))

    totalTT = sum([processList[key]['TT'] for key in processList])
    averageTT = totalTT / len(processList)
    print("Average response time:", round(averageTT, 2))


if __name__ == "__main__":
    process = 5
    processor = 2
    
    arrival_time = [0, 1, 3, 5, 6]
    burst_time = [3, 7, 2, 5, 3]

    #RR함수 호출
    RR(process, arrival_time, burst_time)