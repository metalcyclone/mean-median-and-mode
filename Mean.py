import csv
with open('SOCR-HeightWeight (2).csv',newline='') as f:
     reader = csv.reader(f)
     fileData = list(reader)
fileData.pop(0)
new_data = []
for i in range(len(fileData)):
    n_num= fileData[i][1]
    new_data.append(float(n_num))

n = len(new_data)
sum = 0
for x in new_data:
    sum = sum + x

mean = sum/n
print("mean: "+str(mean))
    