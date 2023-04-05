# HRRN algorithm
def findFirstArrived(arrival_time):
    pos = 0
    at = arrival_time[0]
    for i in range(1, len(arrival_time)):
        if arrival_time[i] < at:
            pos = i
            at = arrival_time[i]
            
    return pos


def searchReadyQueue(arrival_time, current_time, completed):
    arrived = []
    # print("completed", completed)
    for i in range(len(arrival_time)):
        if not completed[i] and arrival_time[i] <= current_time:
            arrived.append(i)
	
    return arrived


def checkCompletedProcess(completed, burst_time, terminated):
    for i in range(len(burst_time)):
        if burst_time[i] == 0:
            
            
            completed[i] = True
            
            # print("P", i+1, "프로세스 실행 완료")


def checkTerminated(burst_time, terminated):
    for i in range(len(burst_time)): 
        if burst_time[i] == 0:
            if i not in terminated:
                terminated.append(i)
                print("*** P",i+1, "실행 완료 ***")


def run(burst_time, pos):
    if burst_time[pos] > 0:
        burst_time[pos] -= 1


def sortByArrival(arrival_time, N):
	sorted(arrival_time)


def initProcess(process, burst_time, total_bt, N):
	for i in range(0, N):
		process.append("P" + str(i+1))
		total_bt += burst_time[i]
	
	return total_bt


def getResponseRatio(burst_time, current_time, arrival_time, pos):
		return ((burst_time[pos] + (current_time - arrival_time[pos])) / burst_time[pos])


def printResult(scheduling_info):
		process, arrival_time, burst_time, waiting_time, turnaround_time, normalized_tt, pos = scheduling_info
		print(process[pos], "\t\t", 
			arrival_time[pos], "\t\t", 
			burst_time[pos], "\t\t",
			waiting_time[pos], "\t\t",
			turnaround_time[pos], "\t\t",
			"{0:.6f}".format(normalized_tt))

	
def findHighestResponseRatio(N, completed, arrival_time, current_time, burst_time, prevPos):
	resopnse_ratio = -9999
	rt, pos = 0, 0
	
	ready_queue =  searchReadyQueue(arrival_time, current_time, completed)
	for i in range(0, N):
		if burst_time[prevPos] > 0:
			# print("아직 프로세서", prevPos, "실행중!")
			return prevPos
			
		# 아직 실행하지 않은 프로세스이면서 ready_queue에 존재한다면
		if not completed[i] and i in ready_queue and burst_time[i] > 0:
			
			# 응답률(Response ratio) 계산
			rt = getResponseRatio(burst_time, current_time, arrival_time, i)
			if resopnse_ratio < rt:
				resopnse_ratio = rt
				pos = i
				
	print(pos+1,"번 프로세스가 Response Ratio가 가장 높습니다.")
	return pos


def calSchedulingInfo(scheduling_info):
    current_time, arrival_time, burst_time, waiting_time, turnaround_time, normalized_tt, pos, sum_tt, sum_wt, bt_temp = scheduling_info
    N = len(arrival_time)

    # 반환시간(TT) = 현재시간 - Ready queue에 도착한 시간
    turnaround_time[pos] = current_time - arrival_time[pos]

	# 대기시간(WT) = 반환시간(TT) - 실행시간(BT)
    waiting_time[pos] = turnaround_time[pos] - burst_time[pos]
		
	# 평균 반환시간 계산
    sum_tt += turnaround_time[pos]
    avg_tt = sum_tt / N

	# 평균 대기시간 계산
    sum_wt += waiting_time[pos]
    avg_wt = sum_wt / N
	
	# Normalized TT = TT / BT
    normalized_tt = float(turnaround_time[pos] / bt_temp[pos])


def HRRN(N, arrival_time, burst_time, processor=1):
		total_bt = 0
		sum_wt = 0
		sum_tt = 0
		
		completed =[False] * N
		terminated = []
		waiting_time = [0] * N
		turnaround_time = [0] * N
		normalized_tt = [0] * N 
		bt_temp = list(burst_time)
		process = []
		
		total_bt = initProcess(process, burst_time, total_bt, N)
		pos = findFirstArrived(arrival_time)

		current_time = 1
		
		while(current_time < total_bt):
			print("---",current_time,"초 ---")
			
			# Ready Queue에 들어온 프로세스 확인하기
			searchReadyQueue(arrival_time, current_time, completed)

			# Response Ratio가 가장 높은 프로세스 찾기
			pos = findHighestResponseRatio(N, completed, arrival_time, current_time, burst_time, pos)
			
			# 완료된 프로세스 있는지 확인하기
			checkCompletedProcess(completed, burst_time, terminated)
			
			# 프로세스 실행
			run(burst_time, pos)
		
			
			# 현재 시간 += 1
			current_time += 1

			# 스케줄링 진행 정보 계산
			scheduling_info = current_time, arrival_time, burst_time, waiting_time, turnaround_time, normalized_tt, pos, sum_tt, sum_wt, bt_temp
			calSchedulingInfo(scheduling_info)
			
			print(process[pos],"실행 중..", "남은 실행 시간", burst_time[pos], "\n")
			# 실행 완료된 프로세스 terminated에 넣기
			checkTerminated(burst_time, terminated)



if __name__ == "__main__":
    process = 5
    processor = 2
    
    arrival_time = [0, 1, 3, 5, 6]
    burst_time = [3, 7, 2, 5, 3]

    
    HRRN(process, arrival_time, burst_time)