def isFinished(completed):
    for i in range(len(completed)):
        if not completed[i]:
            return False

    return True


def FCFS(inputInfo: tuple, arrivalTime: list, workLoad: list):

    N, core = inputInfo
    P = len(core)  # 프로세서
    readyQueue = []

    # 프로세스 할당 받은 여부, 코어의 종류, 현재 실행중인 프로세스 번호
    # on = True, off = False
    processor = []
    for i in range(P):
        processor.append([False, core[i], -1])

    prevState = [False for _ in range(P)]
    notArrived = [True for _ in range(N)]
    completed = [False for _ in range(N)]
    allocated = [False for _ in range(N)]
    burstTime = [0 for _ in range(N)]

    waitingTime = [0] * N
    turnaroundTime = [0] * N
    normalizedTT = [0] * N

    currentTime = 0
    consumedPower = 0

    while not isFinished(completed):
        p = 0
        print("---", currentTime, "초---", workLoad)

        # 종료할 프로세스가 있는지 확인
        for i in range(P):
            p = processor[i][2]

            if workLoad[p] <= 0:
                if processor[i][2] != -1:
                    completed[p] = True
                    print("*** 프로세스", processor[i][2]+1, " 종료 ***")
                    turnaroundTime[p] = currentTime - arrivalTime[p]
                    processor[i][0] = False
                    processor[i][2] = -1

        if isFinished(completed):
            print("종료!")
            break

        # Ready queue에 넣기
        for i in range(N):
            if arrivalTime[i] <= currentTime and not completed[i] and not allocated[i] and notArrived[i]:
                readyQueue.append(i)
                notArrived[i] = False

        # Ready queue에서 빼기
        for i in range(P):
            if not processor[i][0]:
                if len(readyQueue) > 0:
                    p = readyQueue.pop(0)

                # 아직 프로세서 할당 못받은 프로세스라면, 할당 받음
                if not allocated[p] and processor[i][0] == False and p != -1:
                    processor[i][2] = p
                    processor[i][0] = True
                    print("프로세스", p+1, "는 프로세서를", i+1, "할당받음")
                    allocated[p] = True

        # 시동할 프로세서 있는지 확인
        for i in range(P):
            if prevState[i] == False and processor[i][0] == True:
                print("### 프로세서", i+1, "ON ###")
                prevState[i] = True

                if processor[i][1] == 'E':
                    consumedPower += 0.1

                else:
                    consumedPower += 0.5

        # 프로세서 할당 받은 프로세스는 실행함
        for i in range(P):
            p = processor[i][2]
            if processor[i][0]:

                if processor[i][1] == 'E':
                    workLoad[p] -= 1
                    consumedPower += 1
                    burstTime[p] += 1

                else:
                    workLoad[p] -= 2
                    consumedPower += 3
                    burstTime[p] += 1

                print("프로세서", i+1, ": 프로세스", p+1, "처리")

            if workLoad[p] <= 0:
                workLoad[p] = 0

        # 현재 시간 증가
        currentTime += 1

        # 시동 종료할 프로세서 있는지 확인
        for i in range(P):
            if prevState[i] == True and processor[i][0] == False and len(readyQueue) == 0:
                print("### 프로세서", i+1, "OFF ###")
                prevState[i] = False

        # Ready Q에서 대기 중인 애들 waitingTime += 1
        for i in readyQueue:
            waitingTime[i] += 1

        print()

    # Nomalized TT 구하기
    for i in range(N):
        normalizedTT[i] = round(turnaroundTime[i] / burstTime[i], 2)

    # Return output
    output = [burstTime, waitingTime,
              turnaroundTime, normalizedTT, consumedPower]
    return output
