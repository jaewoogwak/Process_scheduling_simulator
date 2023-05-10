import random
from Algorithm.HRRN import HRRN
from Algorithm.FCFS import FCFS
from Algorithm.RPN import RPN
from Algorithm.RR import RR
from Algorithm.SPN import SPN
from Algorithm.SRTN import SRTN


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


def isCoreInputValid(core, P, E):
    if core == P + E:
        return True

    return False


if __name__ == "__main__":
    process = 5
    core = 2
    Pcore = 1
    Ecore = 1
    timeQuantum = 2  # optional value(parameter)
    if not isCoreInputValid(core, Pcore, Ecore):
        print("프로세서 분배가 올바르지 않습니다.")

    else:
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
            burstTime, waitingTime, turnaroundTime, normalizedTT, consumedPower, result = output

            print("실행시간", burstTime)
            print("대기시간", waitingTime)
            print("반환시간", turnaroundTime)
            print("Nomalized TT", normalizedTT)
            print("소비전력", consumedPower)

            for r in range(len(result)):
                print(r, "초", result[r])
            print(result)
