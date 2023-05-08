def isFinished(completed):
    for i in range(len(completed)):
        if not completed[i]:
            return False
        
    return True
def SRTN(inputInfo, arrivalTime, workLoad):
    N, core = inputInfo # 프로세스 수, 프로세서 정보
    P = len(core) # 프로세서 수
    readyQueue = []
    
    # 프로세스 할당 받은 여부, 코어의 종류, 현재 실행중인 프로세스 번호, 현재 실행중인 프로세스 남은 workLoad 시간
    # on = True, off = False
    processor = []
    for i in range(P):
        processor.append([False, core[i], -1, -1])    
    
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
                    processor[i][3] = -1
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
            
            processor_full = 1 # 프로세서 전부 가동중인지 확인 
            for k in range(P):
                if processor[k][0] == False:
                    processor_full = 0
             
            if processor_full == 1:
                break       
                    
            if len(readyQueue) == 1:  # Ready queue에 하나 있으면 바로 꺼냄
                p = readyQueue.pop(0)  
            elif len(readyQueue) >= 2: # Ready queue에 여러개 있으면
                min = workLoad[readyQueue[0]]
                index = 0
                for j in range(1, len(readyQueue)):
                    if min > workLoad[readyQueue[j]]:
                        index = j
                p=readyQueue.pop(index) # workload 가장 적은 프로세스 꺼냄
            else:
                p = -1
                
                
            if not allocated[p] and processor[i][0] == False and p != -1:                     
                processor[i][2] = p
                processor[i][0] = True
                processor[i][3] = workLoad[p] 
                print("프로세스", p+1, "는 프로세서를", i+1, "할당받음")           
                allocated[p] = True
            elif processor[i][0] == 1 and p != -1:
                readyQueue.append(p)


        if processor_full == 1 : # 프로세서가 다 가동중이면
            
            if len(readyQueue) == 1:  # Ready queue에 하나 있으면 바로 꺼냄
                p = readyQueue.pop(0)  
            elif len(readyQueue) >= 2: # Ready queue에 여러개 있으면
                min = workLoad[readyQueue[0]]
                index = 0
                for j in range(1, len(readyQueue)):
                    if min > workLoad[readyQueue[j]]:
                        index = j
                p = readyQueue.pop(index) # workload 가장 적은 프로세스 꺼냄
            else :
                p = -1
            
            
            max_workload = processor[0][3]
            running_process = processor[0][2]
            processor_num = 0
            
            for l in range(1, P):
                if processor[l][3] > max_workload :
                    max_workload = processor[l][3]
                    running_process = processor[l][2]
                    processor_num = l
                    
            if max_workload > workLoad[p] and p!= -1 : # Ready queue에서 나온 프로세스 workload와 비교
                readyQueue.append(running_process)   
                allocated[running_process] = False                
                processor[processor_num][2] = p
                processor[processor_num][0] = True
                processor[processor_num][3] = workLoad[p]          
                print("프로세스", p+1, "는 프로세서를", processor_num+1, "선점함")           
                allocated[p] = True

            elif max_workload <= workLoad[p] and p!= -1 : # Ready queue에서 꺼내온 프로세스 다시 Ready queue로 삽입
                readyQueue.append(p)
                            
                    
        # 시동할 프로세스 있는지 확인
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
                    
                print("프로세서", i+1 , ": 프로세스", p+1, "처리")
            
            if workLoad[p] <= 0:
                workLoad[p] = 0  
            
            processor[i][3] = workLoad[p]
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
        normalizedTT[i] = turnaroundTime[i] / burstTime[i]
        
    # Return output
    output = [burstTime, waitingTime, turnaroundTime, normalizedTT, consumedPower]
    return output