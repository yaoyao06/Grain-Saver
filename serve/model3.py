import csv,random,copy


if __name__ == '__main__':
    with open('./merged.csv', 'r', encoding='utf-8') as file1:
        reader1 = csv.reader(file1)
        data1 = list(reader1)
        for i in range(len(data1)):
            data1[i][0] = data1[i][0].replace('城市:', '')
            data1[i][0] = data1[i][0].replace('自治区', '')
            data1[i][0] = data1[i][0].replace('回族', '')
            data1[i][1] = data1[i][1].replace('经度:', '')
            data1[i][1] = data1[i][1].replace(' 纬度', '')
            data1[i][2] = data1[i][2].replace('纬度:', '')


    grain=['稻谷','玉米','小麦','大豆','棉花','花生']
    grainEN = ['rice', 'corn', 'wheat', 'bean', 'cotton', 'peanut']
    cycle=[[120],[120],[200],[150],[120],[150]]
    seed=[[1],[1],[1],[1],[1],[1]]
    fertilizer=[[30,35,36,37,70],[7,8,9,10,60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
                ,[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,30,55,70,95,125,140],[1,2,3,4,5,80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],[12,13,14,30,45,60,75,90,105,120]
                ,[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]]
    pesticide=[[25,26,27,28,29,30,31,32,33,34,35,60,60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
               ,[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]
               ,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],[12,13,14,22,23,24,110,111,112,113,114,115,116,117,118,119],[7, 8, 9, 10,20, 21, 22, 23, 24, 25,30, 31, 32, 33, 34, 35, 36, 37, 38, 39,50,60,70,80,90]]
    dry=[[70,71,72,73,74,75,113,114,115,116,117,118,119,120],[110,111,112,113,114,115,116,117,118,119,120],[60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]
         ,[10,20,30,40,50],[60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],[]]
    flower=[[110],[110],[180],[140],[100],[45,46,47,48]]
    ik = 0
    with open('model3.csv', 'w', encoding='utf-8', newline='') as merged_file:
        writer = csv.writer(merged_file)
        # 写入表头 次日降雨量、次日最高气温、次日最低气温、土地ph值、土地含水量、作物种类、经度、纬度、时间、生长情况、碳排放总量，输出种植策略（施肥、农药、疏花和疏果、灌水、排水、播种）
        writer.writerow(['rain', 'temper_high', 'temper_low', 'ph', 'water', 'grain','lon','lat','time','growth','c','fertilizer_flag','pesticide_flag','flower_flag','water_flag','dry_flag','seed_flag'])
        to_writer = []
        k=0
        while k<10:
            k=k+1
            for row1 in data1:
                # 获取地名
                if row1[2] == '纬度':
                    continue
                for i in range(len(grain)):
                    for day in range(1, cycle[i][0]):
                        fertilizer_flag = 0
                        pesticide_flag = 0
                        dry_flag = 0
                        water_flag = 0
                        flower_flag = 0
                        seed_flag = 0
                        random_key = random.randint(1, 6)

                        c = random.randint(10, 45 * day)
                        rain = random.randint(-700, 1000) * 0.1
                        growth = day + random.randint(-5, 5)
                        if growth < 0:
                            growth = 0
                        temper1 = random.randint(10, 30)
                        temper2 = random.randint(10, 30)
                        earth_water = random.randint(10, 25)
                        while (temper2 < temper1):
                            temper2 = random.randint(10, 30)
                            temper1 = temper1 - 1
                        if rain < 0:
                            rain = 0
                        if day in fertilizer[i]:
                            fertilizer_flag = 1
                        if day in pesticide[i]:
                            pesticide_flag = 1
                        if day in dry[i]:
                            dry_flag = 1
                        else:
                            water_flag = 1
                        if day in flower[i]:
                            flower_flag = 1

                        if growth < day and day < 100:
                            fertilizer_flag = 1
                        if c > day * 40:
                            fertilizer_flag = 0
                            pesticide_flag = 0
                        if rain > 0:
                            water_flag = 0
                            fertilizer_flag = 0
                            pesticide_flag = 0
                        if rain == 0 and dry_flag == 1:
                            dry_flag = 0
                        if temper2 > 28:
                            fertilizer_flag = 0
                            dry_flag = 0
                        if temper1 < 12:
                            water_flag = 0
                        if earth_water > 23:
                            water_flag = 0
                        if day == 1:
                            seed_flag = 1
                        rain = int(rain)
                        # 次日降雨量、次日最高气温、次日最低气温、土地ph值、土地含水量、作物种类、经度、纬度、时间、生长情况、碳排放总量，输出种植策略（施肥、农药、疏花和疏果、灌水、排水、播种）
                        merged_row = [rain, temper2, temper1, row1[3], earth_water, grainEN[i], row1[1], row1[2], day,
                                      growth, c, fertilizer_flag, pesticide_flag, flower_flag, water_flag, dry_flag,
                                      seed_flag]
                        print(ik, merged_row)
                        to_writer.append(copy.deepcopy(merged_row))
                        ik = ik + 1
                # if ik > 300000:
                #     breakd
            for row3 in to_writer:
                writer.writerow(row3)
            to_writer=[]




