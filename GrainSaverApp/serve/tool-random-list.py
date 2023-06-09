import random
import csv

# 生成随机数列
data = [random.randint(1400, 2100) for _ in range(2000)]

# 将数据保存到csv文件中
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Index', 'Data'])
    for i, d in enumerate(data):
        writer.writerow([i+1, d/100])