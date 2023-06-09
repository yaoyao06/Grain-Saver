import csv,random,copy
'''
稻谷	"早稻：3-4月播种，7-8月收割 中稻：5-6月播种，8-9月收割 晚稻：6-7月播种，9-10月收割
大豆	5-6月份播种，10-12月份收割	
花生	"在南方，春花生3-4月播种，8-10月收割；夏花生6-7月播种，9-10月收割。在北方，春花生4-5月播种，9-10月收割；夏花生6-7月播种，9-10月收割。
棉花	4-5月份播种，9-11月份收割	
小麦	寒露播种，南方5-6月份收割，北方9-10月份收割
玉米	4-5月份播种，8-10月份收割		
芝麻	4-5月份播种，7-9月份收割	
'''

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
            if data1[i][4] == '':
                data1[i] = [data1[i][0], data1[i][1], data1[i][2], data1[i][3]]
    grain=['稻谷','玉米','小麦','大豆','棉花','花生']
    grainEN = ['rice', 'corn', 'wheat', 'bean', 'cotton', 'peanut', 'sesame']
    grainnum=[1,2,3,4,5,6]
    N=[[10,13],[45,90],[15,30],[30,40],[60,75],[20,30],[10,15]]
    P=[[4,7],[30,60],[10,15],[20,30],[30,40],[15,25],[5,7.5]]
    K=[[5,8],[30,60],[10,15],[20,30],[30,40],[15,25],[10,15]]
    seed=[[4,7.5],[15,25],[10,20],[5,6],[8,10],[12.5,15],[2.5,3.5]]
    ik = 0
    with open('model2.csv', 'w', encoding='utf-8', newline='') as merged_file:
        writer = csv.writer(merged_file)
        # 写入表头
        writer.writerow(['grain_type', 'lon', 'lat', 'ph', 'water', 'temper','fertilizer-n','fertilizer-p','fertilizer-k','seed','tool'])
        to_writer = []

        # 遍历第一个CSV文件的每一行
        for row1 in data1:
            # 获取地名
            if row1[2]=='纬度':
                continue
            for i in range(len(grain)):
                temper=random.randint(100, 300)*0.1
                x=(temper-10)/80
                if float(row1[2])>= 35:
                    x=x+0.2
                if float(row1[11])>8000:
                    x=x+0.1
                x=x+1
                merged_row = [grainnum[i], row1[1], row1[2], row1[3], row1[11], temper, N[i][0]*x, P[i][0]*x, K[i][0]*x, seed[i][0]*x, 1]
                ik = ik + 1
                print(ik, merged_row)
                # print(merged_row)
                # 写入新的CSV文件
                to_writer.append(copy.deepcopy(merged_row))
        for row3 in to_writer:
            writer.writerow(row3)

