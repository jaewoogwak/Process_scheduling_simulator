def isFinished(completed):
    for i in range(len(completed)):
        if not completed[i]:
            return False
        
    return True


# 기본 로직
# 1. 종료할 프로세스 있는지 확인 
# 2. ready Q 넣기
# 3. ready Q에서 빼기
# 4. 프로세스에게 프로세서 할당 
# 5. 실행

def FCFS(arrival_time, burst_time):
    N = 5
    core = 1
    readyQueue = []
    processorInfo = [True, "E", -1]
    processor = [processorInfo[:] for _ in range(core)]
    completed = [False for _ in range(N)]
    allocated = [False for _ in range(N)]
    currentTime = 0
    
    while not isFinished(completed):
        readyQueue = []
        p = 0
        
        print("---",currentTime,"초---", burst_time)
        
        # 종료할 프로세스가 있는지 확인
        for i in range(core):
            p = processor[i][2]
        
            if burst_time[p] <= 0 and processor[i][2] != -1:
                completed[p] = True
                print("*** 프로세스", processor[i][2], " 종료 ***")
                processor[i][0] = True
                processor[i][2] = -1
        
        # ready queue에 넣기
        for i in range(N):
            if arrival_time[i] <= currentTime and not completed[i] and not allocated[i]:
                readyQueue.append(i)
        
        print(readyQueue)
        
        # ready queue에서 빼기
        for i in range(core):
            if len(readyQueue) > 0: 
                p = readyQueue.pop(0)

            # 프로세서가 사용 가능하면
            print("프로세서", processor)
            if processor[i][0]:
                # 아직 프로세서 할당 못받은 프로세스라면, 할당 받음
                if not allocated[p]:
                    processor[i][2] = p
                    processor[i][0] = False
                    allocated[p] = True
        
        # 프로세서 할당 받은 프로세스는 실행함
        for i in range(core):
            p = processor[i][2]   
            if not processor[i][0]:
                burst_time[p] -= 1
                print("p",p, "실행")

        currentTime += 1
    
    
    
    

if __name__ == "__main__":
    process = 5
    processor = 2
    
    arrival_time = [0, 1, 3, 5, 6]
    burst_time = [3, 7, 2, 5, 3]

    
    FCFS(arrival_time, burst_time)