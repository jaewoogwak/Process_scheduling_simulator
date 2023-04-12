# AT(arriveTime), BT(BurstTime), RT(RemainingTime), WT(waitingTime), TT(TurnaroundTime), NTT(Normalized Turnaround Time)
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




if __name__ == "__main__":
    process = 5
    processor = 2
    
    arrival_time = [0, 1, 3, 5, 6]
    burst_time = [3, 7, 2, 5, 3]

    #FCFS 함수 호출
    FCFS(process, arrival_time, burst_time)
