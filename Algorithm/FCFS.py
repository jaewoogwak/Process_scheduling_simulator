processList = {'p1':[0, 3, 0, 0, 0], 'p2':[1, 7, 0, 0, 0], 'p4':[5, 5, 0, 0, 0], 'p5':[6, 3, 0, 0, 0], 'p3':[3, 2, 0, 0, 0]}

for key, value in processList.items():
    processList[key] = {'AT': value[0], 'BT': value[1], 'WT': value[2], 'TT': value[3], 'NTT': value[4]}

arrangeList = [{'Process': key, 'AT': value['AT'], 'BT': value['BT'], 'WT': 0, 'TT': 0, 'NTT': 0} for key, value in sorted(processList.items(), key=lambda e: e[1]['AT'])]

for i in range(len(arrangeList)):
    if i == 0:
        arrangeList[i]['WT'] = arrangeList[i]['AT']
    else:
        wt = arrangeList[i-1]['AT'] + arrangeList[i-1]['BT'] + arrangeList[i-1]['WT']
        arrangeList[i]['WT'] = wt - arrangeList[i]['AT'] if wt >= arrangeList[i]['AT'] else 0

    arrangeList[i]['TT'] = arrangeList[i]['BT'] + arrangeList[i]['WT']
    arrangeList[i]['NTT'] = arrangeList[i]['TT'] / arrangeList[i]['BT'] if arrangeList[i]['BT'] != 0 else 0

Fulltime = arrangeList[-1]['AT'] + arrangeList[-1]['BT'] + arrangeList[-1]['WT']

print("Arranged List")
print("Process\tAT\tBT\tWT\tTT\tNTT")
for i in arrangeList:
    print("{}\t{}\t{}\t{}\t{}\t{}".format(i['Process'], i['AT'], i['BT'], i['WT'], i['TT'], round(i['NTT'], 2)))

print("Fulltime: ", Fulltime)