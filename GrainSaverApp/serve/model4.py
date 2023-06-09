import csv ,copy
from fuzzywuzzy import fuzz

# 读取第一个CSV文件
with open('../智能辅助生产参考经纬度.csv', 'r') as file1:
    reader1 = csv.reader(file1)
    data1 = list(reader1)
    for i in range(len(data1)):
        data1[i][0]=data1[i][0].replace('城市:','')
        data1[i][0] = data1[i][0].replace('自治区', '')
        data1[i][0] = data1[i][0].replace('回族', '')
        data1[i][1] = data1[i][1].replace('经度:', '')
        data1[i][1] = data1[i][1].replace(' 纬度', '')
        data1[i][2] = data1[i][2].replace('纬度:', '')
        if data1[i][4]=='':
            data1[i]=[data1[i][0],data1[i][1],data1[i][2],data1[i][3]]
        # print(data1[i])


# 读取第二个CSV文件
with open('../智能辅助生产参考降雨量.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    data2 = list(reader2)
    for i in range(len(data2)):
        data2[i][0]=data2[i][0].replace('自治区','')
        data2[i][0] = data2[i][0].replace('省', '')
        data2[i][0] = data2[i][0].replace('市', '')
        data2[i][0] = data2[i][0].replace('维吾尔', '')
        data2[i][0] = data2[i][0].replace('壮族', '')
        data2[i][0] = data2[i][0].replace('回族', '')
        data2[i][0] = data2[i][0].replace('特别行政区', '')

        data2[i][9] = data2[i][9].replace('县', '')
        data2[i][9] = data2[i][9].replace('区', '')
        data2[i][9] = data2[i][9].replace('市', '')
        data2[i][9] = data2[i][9].replace('特别行政', '')
        data2[i][0]=data2[i][0]+data2[i][9]
        # print(data2[i])


# 创建一个新的CSV文件，用于存储合并后的数据
with open('merged.csv', 'w', encoding='utf-8', newline='') as merged_file:
    writer = csv.writer(merged_file)

    # 写入表头
    writer.writerow(['地名', '经度',	'纬度',	'ph','年份',	'省代码','省'	,'市代码','市',	'县代码'	'县',	'降水量'])
    to_writer=[]
    i=0
    # 遍历第一个CSV文件的每一行
    for row2 in data2:
        # 获取地名
        name2 = row2[0]
        # if row2[1]!="2019":
        #     continue

        # 遍历第二个CSV文件的每一行
        for row1 in data1:
            # 获取地名
            name1 = row1[0]

            # 使用模糊匹配算法计算两个地名的相似度
            similarity = fuzz.ratio(name1, name2)

            # 如果相似度大于等于80，则认为是同一个地名
            if similarity >= 80:
                # 合并两行数据 (['地名', '经度',	'纬度',	'ph','年份',	'省代码','省'	,'市代码','市',	'县代码'	'县',	'降水量'])
                merged_row = [name1, row1[1], row1[2],row1[3],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6],row2[7],row2[8]]
                i=i+1
                print(i, name1,name2)
                # print(merged_row)
                # 写入新的CSV文件
                to_writer.append(copy.deepcopy(merged_row))

                # 跳出内层循环，继续遍历下一行数据
                break
    for row3 in to_writer:
        writer.writerow(row3)