def isFinished(completed):
    for i in range(len(completed)):
        if not completed[i]:
            return False
        
    return True


def setPreemption(i, processor, allocated):
    # if processor[i][3] == timeQuantum:
    print("프로세서",i+1,"에서 선점 발생")
    processor[i][0] = False
    processor[i][2] = -1
    processor[i][3] = 0

# 기본 로직
# 1. 종료할 프로세스 있는지 확인 
# 2. ready Q 넣기
# 3. ready Q에서 빼기
# 4. 프로세스에게 프로세서 할당 
# 5. 실행
# 6. Time quantum 지나면 현재 프로세서의 실행 멈추고 2번으로 넘어감

def RoundRobin(inputInfo, arrival_time, workLoad, timeQuantum):
    N, core = inputInfo
    P = len(core) # 프로세서
    readyQueue = []
    
    # 프로세스 할당 받은 여부, 코어의 종류, 현재 실행중인 프로세스 번호, timeSlice
    # on = True, off = False
    processor = []
    for i in range(P):
        processor.append([False, core[i], -1, 0])    
    
    prevState = [False for _ in range(P)]
    notArrived = [True for _ in range(N)]
    completed = [False for _ in range(N)]
    allocated = [False for _ in range(N)]
    burstTime = [0 for _ in range(N)]
    isOccurPreemption = [False for _ in range(N)]
    
    burstTimeTemp = workLoad[:]
    waitingTime = [0] * N
    turnaroundTime = [0] * N
    normalizedTT = [0] * N 
    
    
    currentTime = 0
    consumedPower = 0
    
    while not isFinished(completed):
        # readyQueue = []
        p = 0
        
        print("---",currentTime,"초---", workLoad)
        
        # 종료할 프로세스가 있는지 확인
        for i in range(P):
            p = processor[i][2]
        
            if workLoad[p] <= 0:
                if processor[i][2] != -1:
                    completed[p] = True
                    print("*** 프로세스", processor[i][2]+1, " 종료 ***")
                    turnaroundTime[p] = currentTime - arrival_time[p]
                    processor[i][0] = False
                    processor[i][2] = -1
                    processor[i][3] = 0

        if isFinished(completed):
            print("종료!")
            break
        
        # 선점당할 프로세스 있는지 확인
        preemption = False
        toBePreemption = []
        for i in range(P):
            if processor[i][3] == timeQuantum:
                p = processor[i][2]
                toBePreemption.append(p)
                processor[i][2] = -1
                isOccurPreemption[p] = True
                allocated[p] = False
                preemption = True
                processor[i][0] = False
        
        # ready queue에 넣기
        for i in range(N):
            if arrival_time[i] <= currentTime and not completed[i] and not allocated[i] and notArrived[i]:
                readyQueue.append(i)
                notArrived[i] = False
                
        if preemption:
            print("선점 발생")
            for p in toBePreemption:
                readyQueue.append(p)
                isOccurPreemption[p] = False
            preemption = False
            

        # ready queue에서 빼기            
        for i in range(P):
            if not processor[i][0]:
                if len(readyQueue) > 0: 
                    p = readyQueue.pop(0)
                
                # 아직 프로세서 할당 못받은 프로세스라면, 할당 받음
                if not allocated[p] and processor[i][0] == False and p != -1:
                    processor[i][2] = p
                    processor[i][0] = True
                    print("프로세스",p+1,"는 프로세서를",i+1,"할당받음")           
                    allocated[p] = True
                    processor[i][3] = 0
        
        for i in range(P):
            if prevState[i] == False and processor[i][0] ==  True:
                print("### 프로세서",i+1, "ON ###")
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
                
                # timeSlice += 1
                processor[i][3] += 1
                    
                print("프로세서",i+1 ,": 프로세서",p+1, "처리")
            
            if workLoad[p] <= 0:
                workLoad[p] = 0    

        currentTime += 1
        
        for i in range(P):
            if prevState[i] == True and processor[i][0] == False and len(readyQueue) == 0:
                print("### 프로세서",i+1, "OFF ###")
                prevState[i] = False
        
        # Ready Q에서 대기 중인 애들 waitingTime += 1
        for i in readyQueue:
            waitingTime[i] += 1
        
        print("실행하지 못한애들 Ready Q", readyQueue)
        print("소비전력", consumedPower)

        print() 
        
        if currentTime > 25:
            return

    # Nomalized TT 구하기
    for i in range(N):
        normalizedTT[i] = turnaroundTime[i] / burstTime[i]
        
    print("소비전력", consumedPower)
    print("실행시간", burstTime)
    print("대기시간", waitingTime)
    print("반환시간", turnaroundTime)
    print("Nomalized TT", normalizedTT)
    
    
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


if __name__ == "__main__":
    process = 5
    core = 1
    Pcore = 0
    Ecore = 1
    processor = generateProcessor(core, Pcore, Ecore)
    inputInfo = (process, processor)
    
    arrivalTime = [0, 1, 3, 5, 6]
    workLoad = [3,7,2,5,3]
    
    timeQuantum = 2
    
    
    RoundRobin(inputInfo, arrivalTime, workLoad, timeQuantum)