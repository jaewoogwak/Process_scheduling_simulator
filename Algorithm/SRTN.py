
def transToDict(processN, arrival_time, burst_time): 
    processName=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15']
    at={}
    bt={}
    
    for i in range(processN):
        p=processName[i]
        at[p]=arrival_time[i]
        bt[p]=burst_time[i]
    return at, bt

def init(processN):
    processName=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15']
    
    wt={}
    tt={}
    ntt={}
    
    for i in range(processN):
        p=processName[i]
        wt[p]=0
        tt[p]=0
        ntt[p]=0
    return wt,tt,ntt

def calculateTotalT(burstT):
    sum=0
    for p in burstT:
        sum+=burstT[p]
    return sum

def calculateTT(FinishedP,burstT,waitingT):
    p=FinishedP
    tt=waitingT[p]+burstT[p]
    return tt

def calculateNTT(FinishedP,burstT,turnAroundT):
    p=FinishedP
    ntt=float(turnAroundT[p]/burstT[p])
    return ntt
    
def printData(arrivalT, burstT, waitingT, turnAroundT, NTT):
        print()
        print("Result")
        print("ID\tAT\tBT\tWT\tTT\tNTT")
        print("-------------------------------------------")

        for p in waitingT:
            print("{}\t{}\t{}\t{}\t{}\t{:.1f}".format(p, arrivalT[p], burstT[p], waitingT[p], turnAroundT[p], NTT[p]))

        # print(f'Average Turnaround Time: {average_turnaround_time}')

        # print(f'Average Waiting Time: {average_waiting_time}')
    
def SRTN(processN, arrival_time, burst_time):
    
    ready=[]
    
    processList={} # srtn 도중 t 깍임
    arrivalT={}
    burstT={}
    waitingT={}
    turnAroundT={}
    NTT={}
    
    arrivalT, burstT=transToDict(processN, arrival_time, burst_time) # arrivalT, burstT 딕셔너리로 변경
    processList=burstT.copy()
    
    waitingT, turnAroundT, NTT= init(processN) # waitingT, turnAroundT, NTT 0으로 초기화
    
    totalT=calculateTotalT(burstT) # totalT 계산
    
    t=0
    while t<totalT:
        for arrival in arrivalT:
            if arrivalT.get(arrival) == t: #  t초에 프로세스가 들어오면
                ready.append(arrival) # 레디에다가 넣어줌
                
        if len(ready)==1:
            currentP=ready[0] # 레디 안에 하나밖에 없으면 바로 꺼내옴
            del ready[0]
        else: # 레디 안에 여러개 프로세스가 있으면
            minT=processList[ready[0]]
            index=0
            for i in range(1,len(ready)):
                if minT>processList[ready[i]]:
                    minT=processList[ready[i]]
                    index=i
            currentP=ready[index] # bt 가장 작은 프로세스 꺼내옴
            del ready[index]
            for p in ready: # ready에 남은 프로세스들은 wt 1 증가
                waitingT[p]+=1 
        # currentP는 i초에 진행할 프로세스
        # coreScheduling(currentP) # 코어스케쥴링
        print("%d초 실행 중 "%t, currentP) # 현재 프로세스 1초동안 진행
        processList[currentP]-=1 # burst time 1초 감소
        if processList[currentP] !=0: # 프로세스 안 끝나면 
            ready.append(currentP) # 다음 프로세스가 큐에 들어오기 전에 작업중이던 프로세스가 큐에 다시 먼저 들어가는 것으로 기준삼음
        else: # 프로세스가 끝나면
            turnAroundT[currentP]=calculateTT(currentP,burstT,waitingT) # TT, NTT 계산
            NTT[currentP]=calculateNTT(currentP,burstT,turnAroundT)
        t+=1
    # 다 끝나면
    printData(arrivalT, burstT, waitingT, turnAroundT, NTT)

            

if __name__ == "__main__":
    processN = 5
    processor = 2
    
    arrival_time = [0, 1, 3, 5, 6]
    burst_time = [3, 7, 2, 5, 3]
    
    
    SRTN(processN, arrival_time, burst_time)
