from queue import PriorityQueue


def SPN(inputInfo, arrivalTime, workLoad):

    def isFinished(completed):
        for i in range(len(completed)):
            if not completed[i]:
                return False

        return True

    N, core = inputInfo
    P = len(core)  # 프로세서
    readyQueue = PriorityQueue()

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

        # ready queue에 넣기
        for i in range(N):
            if arrivalTime[i] <= currentTime and not completed[i] and not allocated[i] and notArrived[i]:
                readyQueue.put((workLoad[i], i))
                notArrived[i] = False

        # ready queue에서 빼기
        for i in range(P):
            if not processor[i][0]:
                if readyQueue.qsize() > 0:
                    w, p = readyQueue.get()

                # 아직 프로세서 할당 못받은 프로세스라면, 할당 받음
                if not allocated[p] and processor[i][0] == False and p != -1:
                    processor[i][2] = p
                    processor[i][0] = True
                    print("프로세스", p+1, "는 프로세서를", i+1, "할당받음")
                    allocated[p] = True

        for i in range(P):
            if prevState[i] == False and processor[i][0] == True:
                # print("### 프로세서", i+1, "ON ###")
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

                print("프로세서", i+1, ": 프로세서", p+1, "처리")

            if workLoad[p] <= 0:
                workLoad[p] = 0

        currentTime += 1

        for i in range(P):
            if prevState[i] == True and processor[i][0] == False and readyQueue.qsize() == 0:
                print("### 프로세서", i+1, "OFF ###")
                prevState[i] = False

        temp = []
        # Ready Q에서 대기 중인 애들 waitingTime += 1
        while readyQueue.qsize() > 0:
            w, p = readyQueue.get()
            waitingTime[p] += 1
            temp.append((w, p))

        for w, p in temp:
            readyQueue.put((w, p))

        print()

    # Nomalized TT 구하기
    for i in range(N):
        normalizedTT[i] = turnaroundTime[i] / burstTime[i]

    # Return output
    output = [burstTime, waitingTime,
              turnaroundTime, normalizedTT, consumedPower]
    return output


def generateProcessor(core, P, E):
    if core != P + E:
        print("프로세서 분배가 올바르지 않습니다.")
        return False

    processor = []
    for i in range(P):
        processor.append("P")

    for i in range(E):
        processor.append("E")

    return processor


def checkValidate(process, arrivalTime, workLoad):
    if process != len(arrivalTime) or process != len(workLoad):
        return False

    return True


if __name__ == "__main__":
    process = 5
    core = 1
    Pcore = 0
    Ecore = 1
    processor = generateProcessor(core, Pcore, Ecore)
    inputInfo = (process, processor)
    arrivalTime = [0, 1, 3, 5, 6]
    workLoad = [3, 7, 2, 5, 3]

    # 입력이 올바른지 검사
    if not checkValidate(process, arrivalTime, workLoad):
        print("프로세스 수와 arrivalTime, workLoad 데이터 길이가 일치하지 않습니다.")

    else:
        # 프로세스 스케줄링 실행
        output = SPN(inputInfo, arrivalTime, workLoad)
        burstTime, waitingTime, turnaroundTime, normalizedTT, consumedPower = output

        print("소비전력", consumedPower)
        print("실행시간", burstTime)
        print("대기시간", waitingTime)
        print("반환시간", turnaroundTime)
        print("Nomalized TT", normalizedTT)
        print("output", output)
