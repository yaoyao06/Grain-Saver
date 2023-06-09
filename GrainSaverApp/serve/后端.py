from flask import Flask, jsonify, request
import pymysql,json
import datetime
import requests
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from ibm_watson import AssistantV1
assistant = AssistantV1(version='v1')
assistant.set_service_url('{https://api.jp-tok.assistant.watson.cloud.ibm.com/instances/9c649e5f-948d-490a-9d16-03afc02d953b}')

app = Flask(__name__)
connection = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='123456', db='test_database')
cur = connection.cursor()
create_workspace_data = {
    "name":    "grain-saver",
    "description":
    "just talk",
    "language":
    "en",
    "intents": [{    }],
    "entities": [{    }],
    "counterexamples": [{
        "text": "string"
    }],
    "metadata": {},
}
response = assistant.create_workspace(
    name=create_workspace_data['name'],
    description=create_workspace_data['description'],
    language='en',
    intents=create_workspace_data['intents'],
    entities=create_workspace_data['entities'],
    counterexamples=create_workspace_data['counterexamples'],
    metadata=create_workspace_data['metadata']).get_result()
print(json.dumps(response, indent=2))
workspace_id = response['workspace_id']


@app.route('/talk', methods=['GET'])
def talk():
    word = request.args.get('word')
    examples = [{"text": word}]
    response = assistant.create_intent(
        workspace_id=workspace_id,
        intent='test_intent',
        description='Test intent.',
        examples=examples).get_result()
    print(json.dumps(response, indent=2))
    return json.dumps(response, indent=2)

#http://127.0.0.1:5000/api
@app.route('/apitest', methods=['GET'])
def apitest():
    data = {'name': 'John', 'age': 30, 'thoughts': 'hello,world!你好世界！'}
    print(data,'&&\n',jsonify(data))
    return jsonify(data)

@app.route('/c_account_table', methods=['GET'])#http://127.0.0.1:5000/c_account_table
def c_account_table():
    sql='SELECT * FROM test_database.c_account_table'

    return json_data

@app.route('/c_account_table', methods=['GET'])#http://127.0.0.1:5000/c_account_table
def c_account_table():
    sql='SELECT * FROM test_database.c_account_table'
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date_time_str," -api-/c_account_table- ",sql)
    cur.execute(sql)
    data=cur.fetchall()
    json_data = []
    for row in data:
        d = {}
        d['user_id'] = row[0]
        d['c_total'] = row[1]
        d['c_rank'] = row[2]
        d['money'] = row[3]
        d['m_rank'] = row[4]
        d['m_condition'] = row[5]
        d['credit'] = row[6]
        d['debt_flag'] = row[7]
        d['debt_out'] = row[8]
        d['location_id'] = row[9]
        d['user_name'] = row[10]
        json_data.append(d)
    # 将列表类型转化为JSON格式的字符串
    json_data = json.dumps(json_data)
    print(json_data)
    return json_data

@app.route('/c_trajectory_table', methods=['GET'])#http://127.0.0.1:5000/c_trajectory_table
def c_trajectory_table():
    sql='SELECT * FROM test_database.c_trajectory_table'
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date_time_str," -api-/c_trajectory_table- ",sql)
    cur.execute(sql)
    data=cur.fetchall()
    json_data = []
    for row in data:
        d = {}
        d['change_id'] = row[0]
        d['change_time'] = row[1]
        d['user_id'] = row[2]
        d['plant_id'] = row[3]
        d['other_id'] = row[4]
        d['c_change'] = row[5]
        d['plant_plan'] = row[6]
        d['grow_condition'] = row[7]
        json_data.append(d)
    # 将列表类型转化为JSON格式的字符串
    json_data = json.dumps(json_data)
    print(json_data)
    return json_data

    location_table=[('location_id', 'int(11)'), ('location_name', 'varchar(45)'), ('location_lon', 'float'), ('location_lat', 'float'), ('location_source', 'varchar(45)'), ('location_factory', 'varchar(45)')]

@app.route('/location_table', methods=['GET'])#http://127.0.0.1:5000/location_table
def location_table():
    sql='SELECT * FROM test_database.location_table'
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date_time_str," -api-/location_table- ",sql)
    cur.execute(sql)
    data=cur.fetchall()
    json_data = []
    for row in data:
        d = {}
        d['location_id'] = row[0]
        d['location_name'] = row[1]
        d['location_lon'] = row[2]
        d['location_lat'] = row[3]
        d['location_source'] = row[4]
        d['location_factory'] = row[5]
        json_data.append(d)
    # 将列表类型转化为JSON格式的字符串
    json_data = json.dumps(json_data)
    # print(json_data)
    return json_data

@app.route('/market_table', methods=['GET'])#http://127.0.0.1:5000/market_table
def market_table():
    sql='SELECT * FROM test_database.market_table'
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date_time_str," -api-/market_table- ",sql)
    cur.execute(sql)
    data=cur.fetchall()
    json_data = []
    for row in data:
        d = {}
        d['trade_id'] = row[0]
        d['seller_id'] = row[1]
        d['buyer_id'] = row[2]
        d['goods_type'] = row[3]
        d['goods_amount'] = row[4]
        d['goods_price'] = row[5]
        d['location_id'] = row[6]
        d['trade_flag'] = row[7]
        json_data.append(d)
    # 将列表类型转化为JSON格式的字符串
    json_data = json.dumps(json_data)
    # print(json_data)
    return json_data

@app.route('/plant_table', methods=['GET'])#http://127.0.0.1:5000/plant_table
def plant_table():
    sql='SELECT * FROM test_database.plant_table'
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date_time_str," -api-/plant_table- ",sql)
    cur.execute(sql)
    data=cur.fetchall()
    json_data = []
    for row in data:
        d = {}
        d['plant_id'] = row[0]
        d['plant_type'] = row[1]
        d['location_id'] = row[2]
        d['plant_area'] = row[3]
        d['seed_achieve'] = row[4]
        d['fertilizer_achieve'] = row[5]
        d['tool_achieve'] = row[6]
        d['c_output'] = row[7]
        d['user_id'] = row[8]
        d['plant_plan'] = row[9]
        d['grow_cycle'] = row[10]
        d['grow_progress'] = row[11]
        d['grow_condition'] = row[12]
        json_data.append(d)
    # 将列表类型转化为JSON格式的字符串
    json_data = json.dumps(json_data)
    # print(json_data)
    return json_data

@app.route('/close', methods=['GET'])
def close():
    connection.close()
    cur.close()
    return "connection closed"

@app.route('/init_user')# http://127.0.0.1:5000/init_user?user_id=1234&user_name=鼠标
def init_user():
    sql_default=[10,0,'D',0,'D','D','D','Y',0,0,'TEST']
    sql_in = [10, 0, 'D', 0, 'D', 'D', 'D', 'Y', 0, 0, 'TEST']
    sql_in[0] = request.args.get('user_id')
    sql_in[1]  = request.args.get('c_total')
    sql_in[2]  = request.args.get('c_rank')
    sql_in[3]  = request.args.get('money')
    sql_in[4]  = request.args.get('m_rank')
    sql_in[5]  = request.args.get('m_condition')
    sql_in[6]  = request.args.get('credit')
    sql_in[7]  = request.args.get('debt_flag')
    sql_in[8]  = request.args.get('debt_out')
    sql_in[9] = request.args.get('location_id')
    sql_in[10]  = request.args.get('user_name')
    for i in range(len(sql_in)):
        if sql_in[i] is None:
            sql_in[i]=sql_default[i]
    sql="INSERT INTO `test_database`.`c_account_table` (`user_id`, `c_total`, `c_rank`, `money`, `m_rank`, `m_condition`, " \
        "`credit`, `debt_flag`, `debt_out`, `location_id`, `user_name`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor = connection.cursor()
    try:
        cursor.execute(sql, tuple(sql_in))
        connection.commit()
    except:
        print("执行错误")
    row_count = cursor.rowcount

    if row_count > 0:
        result = "操作成功"
    else:
        result = "操作失败"
    return "--" + result + "--" + sql + str(sql_in)

@app.route('/update_debt')# http://127.0.0.1:5000/update_debt?user_id=1234&debt_out=10000000&money=100000000
def update_debt():
    sql_in=[0,0,0]
    sql_in[2] = request.args.get('user_id')
    sql_in[0]  = request.args.get('money')
    sql_in[1]  = request.args.get('debt_out')
    for i in range(len(sql_in)):
        if sql_in[i] is None:
            return 'input illegal !!!'
    sql="UPDATE `test_database`.`c_account_table` SET `money` = %s, `debt_out` = %s WHERE (`user_id` = %s AND debt_flag = 'Y');"
    cursor = connection.cursor()
    try:
        cursor.execute(sql, tuple(sql_in))
        connection.commit()
    except:
        print("执行错误")
    row_count = cursor.rowcount
    if row_count > 0:
        result = "操作成功"
    else:
        result = "操作失败"
    return "--" + result + "--" + sql + str(sql_in)

# http://127.0.0.1:5000/plant_init?plant_id=12345&plant_type=小麦&location_id=1&plant_area=1&seed_achieve=1000&fertilizer_achieve=1000&tool_achieve=1000&c_output=100&user_id=1234&plant_plan=暂无&grow_cycle=100&grow_progress=0&grow_condition=0
@app.route('/plant_init')
def plant_init():
    sql_in=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    sql_in[0] = request.args.get('plant_id')
    sql_in[1] = request.args.get('plant_type')
    sql_in[2] = request.args.get('location_id')
    sql_in[3]  = request.args.get('plant_area')
    sql_in[4]  = request.args.get('seed_achieve')
    sql_in[5] = request.args.get('fertilizer_achieve')
    sql_in[6] = request.args.get('tool_achieve')
    sql_in[7] = request.args.get('c_output')
    sql_in[8] = request.args.get('user_id')
    sql_in[9] = request.args.get('plant_plan')
    sql_in[10] = request.args.get('grow_cycle')
    sql_in[11] = request.args.get('grow_progress')
    sql_in[12] = request.args.get('grow_condition')
    for i in range(len(sql_in)):
        if sql_in[i] is None:
            return 'input illegal !!! '+str(sql_in)
    sql = "INSERT INTO `test_database`.`plant_table` (`plant_id`, `plant_type`, `location_id`, `plant_area`, `seed_achieve`," \
          " `fertilizer_achieve`, `tool_achieve`, `c_output`, `user_id`, `plant_plan`, `grow_cycle`, `grow_progress`, `grow_condition`) " \
          "VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s);"
    cursor = connection.cursor()
    try:
        cursor.execute(sql, tuple(sql_in))
        connection.commit()
    except:
        print("执行错误")
    row_count = cursor.rowcount
    if row_count > 0:
        result="操作成功"
    else:
        result="操作失败"
    return "--"+result+"--"+sql+str(sql_in)

@app.route('/process')# http://127.0.0.1:5000/process?change_id=2&change_time=2022-02-02T15:15:15&user_id=1234&other_id=1&c_change=100
def process():
    sql_in=[0,0,0,0,0]
    sql_in[0] = request.args.get('change_id')
    sql_in[1] = request.args.get('change_time')
    sql_in[2] = request.args.get('user_id')
    sql_in[3]  = request.args.get('other_id')
    sql_in[4]  = request.args.get('c_change')
    for i in range(len(sql_in)):
        if sql_in[i] is None:
            return 'input illegal !!! '+str(sql_in)
    sql = "INSERT INTO `test_database`.`c_trajectory_table` (`change_id`, `change_time`, `user_id`, `other_id`, `c_change`)" \
          " VALUES (%s, %s, %s,%s, %s);"
    cursor = connection.cursor()
    try:
        cursor.execute(sql, tuple(sql_in))
        connection.commit()
    except:
        print("执行错误")
    row_count = cursor.rowcount
    if row_count > 0:
        result="操作成功"
    else:
        result="操作失败"
    return "--"+result+"--"+sql+str(sql_in)

# http://127.0.0.1:5000/grow?change_id=12345&change_time=2022-10-11T12:12:12&user_id=1&plant_id=1234&c_change=1000&plant_plan=排水&grow_condition=10
@app.route('/grow')
def grow():
    sql_in=[0,0,0,0,0,0,0]
    sql_in[0] = request.args.get('change_id')
    sql_in[1] = request.args.get('change_time')
    sql_in[2] = request.args.get('user_id')
    sql_in[3]  = request.args.get('plant_id')
    sql_in[4]  = request.args.get('c_change')
    sql_in[5] = request.args.get('plant_plan')
    sql_in[6] = request.args.get('grow_condition')
    for i in range(len(sql_in)):
        if sql_in[i] is None:
            return 'input illegal !!! '+str(sql_in)
    sql = "INSERT INTO `test_database`.`c_trajectory_table` (`change_id`, `change_time`, `user_id`, `plant_id`, `c_change`," \
          " `plant_plan`, `grow_condition`) VALUES ( %s,  %s,  %s,  %s ,  %s,  %s,  %s);"
    cursor = connection.cursor()
    try:
        cursor.execute(sql, tuple(sql_in))
        connection.commit()
    except:
        print("执行错误")
    row_count = cursor.rowcount
    if row_count > 0:
        result="操作成功"
    else:
        result="操作失败"
    return "--"+result+"--"+sql+str(sql_in)

@app.route('/update_c')# http://127.0.0.1:5000/update_c?user_id=1234&c_total=10000000&c_rank=100000000
def update_c():
    sql_in=[0,0,0]
    sql_in[2] = request.args.get('user_id')
    sql_in[0]  = request.args.get('c_total')
    sql_in[1]  = request.args.get('c_rank')
    for i in range(len(sql_in)):
        if sql_in[i] is None:
            return 'input illegal !!!'
    sql="UPDATE `test_database`.`c_account_table` SET `c_total` = %s, `c_rank` = %s WHERE (`user_id` = %s );"
    cursor = connection.cursor()
    try:
        cursor.execute(sql, tuple(sql_in))
        connection.commit()
    except:
        print("执行错误")
    row_count = cursor.rowcount
    if row_count > 0:
        result = "操作成功"
    else:
        result = "操作失败"
    return "--" + result + "--" + sql + str(sql_in)

@app.route('/timejump')# http://127.0.0.1:5000/timejump?jump=30
def timejump():
    print(timejump)
    time=request.args.get('jump')
    return f'timejump'

@app.route('/hello')# http://127.0.0.1:5000/hello?name=1
def hello():
    name = request.args.get('name')
    return f'Hello, {name}!'


@app.route('/grain_three')# http://127.0.0.1:5000/grain_three?longitude=30&latitude=50&ph=5.4&rain=6000&water=200
def grain_three():
    print('start')
    #longitude	latitude	ph	rain	water	PH	rice	corn	wheat	bean	peanut	cotton
    longitude=request.args.get('longitude')
    latitude=request.args.get('latitude')
    ph=request.args.get('ph')
    rain=request.args.get('rain')
    water=request.args.get('water')

    API_KEY = "2QCnQ5HrE7yWD58qYFzec9Vq98qi3v4jz5w8kcSLqsfv"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
                                                                                         API_KEY,
                                                                                     "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": ['longitude', 'latitude', 'ph', 'rain(mm)', 'water%', 'PH'],
                                       "values": [[longitude, latitude, ph, rain, water,ph]]}]}

    response_scoring = requests.post(
        'https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/bd186d4f-25f8-48c8-9484-6c3379d03d24/predictions?version=2023-06-01',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    return response_scoring.json()

@app.route('/plant_need')# http://127.0.0.1:5000/plant_need?grain_type=rice&lon=30&lat=50&ph=60&water=12000&temper=20
def plant_need():
    print('start')
    #grain_type	lon	lat	ph	water	temper	fertilizer-n	fertilizer-p	fertilizer-k	seed	tool
    grain_type=request.args.get('grain_type')
    lon=request.args.get('lon')
    lat=request.args.get('lat')
    ph=request.args.get('ph')
    water=request.args.get('water')
    temper=request.args.get('temper')
    API_KEY = "2QCnQ5HrE7yWD58qYFzec9Vq98qi3v4jz5w8kcSLqsfv"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
                                                                                         API_KEY,
                                                                                     "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {
        "input_data": [{"fields": ['grain_type', 'lon', 'lat', 'ph', 'water', 'temper'],
                        "values": [[grain_type, lon, lat, ph, water, temper]]}]}

    response_scoring = requests.post(
        'https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/8f01f5c6-fde4-44f0-8f7b-395123002fb3/predictions?version=2023-06-01',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    json = response_scoring.json()
    print(response_scoring.json())
    return response_scoring.json()

@app.route('/golden_finger')# http://127.0.0.1:5000/golden_finger?rain=10&temper_high=25&temper_low=15&ph=8.1&water=13&grain=rice&lon=120&lat=10&time=15&growth=12&c=18
def golden_finger():
    #rain	temper_high	temper_low	ph	water	grain	lon	lat	time	growth	c	fertilizer_flag	pesticide_flag	flower_flag	water_flag	dry_flag	seed_flag

    rain=request.args.get('rain')
    temper_high=request.args.get('temper_high')
    temper_low=request.args.get('temper_low')
    ph=request.args.get('ph')
    water=request.args.get('water')
    grain=request.args.get('grain')
    lon=request.args.get('lon')
    lat=request.args.get('lat')
    time=request.args.get('time')
    growth=request.args.get('growth')
    c=request.args.get('c')

    API_KEY = "2QCnQ5HrE7yWD58qYFzec9Vq98qi3v4jz5w8kcSLqsfv"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
                                                                                         API_KEY,
                                                                                     "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'},
                                   verify=False)
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {
        "input_data": [{"fields": ['rain','temper_high','temper_low','ph','water','grain','lon','lat','time','growth','c'],
                        "values": [[rain,temper_high,temper_low,ph,water,grain,lon,lat,time,growth,c]]}]}

    response_scoring = requests.post(
        'https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/0b86f853-ee19-4c26-a2c5-5cf902431292/predictions?version=2023-05-25',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    json = response_scoring.json()
    print("Scoring response: ", json['predictions'][0]['values'][0][0])
    return json['predictions'][0]['values'][0][0]

@app.route('/debt')# http://127.0.0.1:5000/debt?credit_score=372&carbon_score=638
def debt():
    #credit_score	carbon_score	credit_level 	discount_levels
    credit_score=int(request.args.get('credit_score'))
    carbon_score=int(request.args.get('carbon_score'))
    print('carbon_core')


    API_KEY = "2QCnQ5HrE7yWD58qYFzec9Vq98qi3v4jz5w8kcSLqsfv"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
                                                                                         API_KEY,
                                                                                     "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'},
                                   verify=False)
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


    payload_scoring = {
        "input_data": [{"fields": ['credit_score','carbon_score'],
                        "values": [[credit_score,carbon_score]]}]}
    # payload_scoring = {
    #     "input_data": [{"fields": ['credit_score','carbon_score'],
    #                     "values": [[372,759	]]}]}

    response_scoring = requests.post(
        'https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/58516071-f75a-4156-8e28-80d15a897130/predictions?version=2021-05-01',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    json = response_scoring.json()
    # print("Scoring response: ", json['predictions'][0]['values'][0][0])
    return json['predictions']

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()
    print("hi")

