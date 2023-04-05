ready=[]
processName=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15']

# ppt에 나와있는 예시 
processList={'p1':3, 'p2':7, 'p3':2, 'p4':5, 'p5':3} 
burstT={'p1':3, 'p2':7, 'p3':2, 'p4':5, 'p5':3} 
arrivalT={'p1':0,'p2':1,'p3':3,'p4':5,'p5':6}
waitingT={'p1':0, 'p2':0, 'p3':0, 'p4':0, 'p5':0}
turnAroundT={'p1':0, 'p2':0, 'p3':0, 'p4':0, 'p5':0}
NTT={'p1':0, 'p2':0, 'p3':0, 'p4':0, 'p5':0}

totalT=20
processN=5

def calculate(FinishedP):
    p=FinishedP
    turnAroundT[p]=waitingT[p]+burstT[p]
    NTT[p]=turnAroundT[p]/burstT[p]
    
def SRTN():
    # arrange()
    for t in range(totalT):
        for arrival in arrivalT:
            if arrivalT.get(arrival) == t: # t초에 프로세스가 들어오면
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
        print("%d초"%t, currentP) # 현재 프로세스 1초동안 진행
        processList[currentP]-=1 # burst time 1초 감소
        if processList[currentP] !=0: # 프로세스 안 끝나면 
            ready.append(currentP) # 다음 프로세스가 큐에 들어오기 전에 작업중이던 프로세스가 큐에 다시 먼저 들어가는 것으로 기준삼음
        else: # 프로세스가 끝나면
            calculate(currentP) # TT, NTT 계산
    # 다 끝나면
    for result in range(processN):
        n=processName[result]
        print("프로세서 %d WT : %d , TT : %d , NTT : %d" % (result+1, waitingT[n], turnAroundT[n], NTT[n]))
            

SRTN()
print(3/2) # 소수 계산 고치기
