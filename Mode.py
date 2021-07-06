import csv 

from collections import Counter
with open('SOCR-HeightWeight (2).csv',newline='') as f:
     reader = csv.reader(f)
     fileData = list(reader)
fileData.pop(0)
new_data = []
for i in range(len(fileData)):
    n_num= fileData[i][1]
    new_data.append(float(n_num))

data = Counter(new_data)
mode = {
    "50-60":0,"60-70":0,"70-80":0
}
for height,occurrence in data.items():
    if 50<float(height)<60:
        mode["50-60"]+= occurrence
    elif 60<float(height)<70:
        mode["60-70"]+= occurrence

    elif 70<float(height)<80:
        mode["70-80"]+= occurrence

modeRange,modeOccurrence = 0,0
for range,occurrence in mode.items():
    if occurrence>modeOccurrence:
        modeRange, modeOccurrence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence
mode = float((modeRange[0] + modeRange[1]) / 2)
print(f"Mode is -> {mode:2f}")
    