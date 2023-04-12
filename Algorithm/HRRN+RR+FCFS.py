# HRRN algorithm
#arrival_time에서 가장 먼저 도착한 프로세스의 인덱스를 반환하는 함수
def findFirstArrived(arrival_time):
    pos = 0 #가장 먼저 도착할 프로세스 저장하는 곳
    at = arrival_time[0] #
    for i in range(1, len(arrival_time)): #현재 인덱스가 at 보다 작으면 pos에 저장
        if arrival_time[i] < at:
            pos = i
            at = arrival_time[i] #at 변수에 현재 인덱스의 도착시간 저장
            
    return pos #첫 번째 프로세스 인덱스 반환


def searchReadyQueue(arrival_time, current_time, completed):
    arrived = [] #arrival_time을 받은 리스트
    # print("completed", completed)
    for i in range(len(arrival_time)):
        if not completed[i] and arrival_time[i] <= current_time:
            #completed 실행이 완료되지 않는 프로세스면서 현재시간보다 이전에 도착한 프로세스를
            arrived.append(i)
            #arrived에 추가
	
    return arrived #arrived 리스트 반환


def checkCompletedProcess(completed, burst_time, terminated): #프로세스가 완료되었는지 체크
    for i in range(len(burst_time)): #burst time 길이 만큼 반복
        if burst_time[i] == 0: #burst time 인덱스가 0이면 --> 완료되어 terminated
            
            
            completed[i] = True
            
            # print("P", i+1, "프로세스 실행 완료")


def checkTerminated(burst_time, terminated): #실행완료된 것을 다시 체크
    for i in range(len(burst_time)): 
        if burst_time[i] == 0:
            if i not in terminated:
                terminated.append(i)
                print("*** P",i+1, "실행 완료 ***") #실행완료하는 문구 출력


def run(burst_time, pos):
    if burst_time[pos] > 0:
        burst_time[pos] -= 1 #현재 프로세스의 인덱스의 실행시간이 줄어들음


def sortByArrival(arrival_time, N): #도착시간 정렬
	sorted(arrival_time)


def initProcess(process, burst_time, total_bt, N):
	for i in range(0, N):
		process.append("P" + str(i+1))
		total_bt += burst_time[i]
	
	return total_bt #총 실행시간 출력


def getResponseRatio(burst_time, current_time, arrival_time, pos): #응답률 계산
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

# FCFS algorithm
def FCFS(process, arrival_time, burst_time):
    #프로세스 리스트 만들기
    process_list = [{'Process': i+1, 'AT': arrival_time[i], 'BT': burst_time[i], 'WT': 0, 'TT': 0, 'NTT': 0} for i in range(process)]
    #리스트 정리하기(arrival time이 순서대로 오지 않을 수도 있기 때문에)
    arrange_list = sorted(process_list, key=lambda e: e['AT'])
    
    #AT, BT, WT, TT, NTT 계산
    for i in range(process):
        if i == 0:
            arrange_list[i]['WT'] = arrange_list[i]['AT']
        else:
            wt = arrange_list[i-1]['AT'] + arrange_list[i-1]['BT'] + arrange_list[i-1]['WT']
            arrange_list[i]['WT'] = wt - arrange_list[i]['AT'] if wt >= arrange_list[i]['AT'] else 0

        arrange_list[i]['TT'] = arrange_list[i]['BT'] + arrange_list[i]['WT']
        arrange_list[i]['NTT'] = arrange_list[i]['TT'] / arrange_list[i]['BT'] if arrange_list[i]['BT'] != 0 else 0

    #총 소요 시간 계산(코어를 적용하면 어떻게 될지 모르겠음)
    full_time = arrange_list[-1]['AT'] + arrange_list[-1]['BT'] + arrange_list[-1]['WT']

    #프린트
    print("Process\tAT\tBT\tWT\tTT\tNTT")
    for i in arrange_list:
        print("{}\t{}\t{}\t{}\t{}\t{}".format(i['Process'], i['AT'], i['BT'], i['WT'], i['TT'], round(i['NTT'], 2)))

    print("Fulltime: ", full_time)

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

    #FCFS 함수 호출
    FCFS(process, arrival_time, burst_time)

    #RR함수 호출
    RR(process, arrival_time, burst_time)
    
    #HRRN 함수 호출
    HRRN(process, arrival_time, burst_time)