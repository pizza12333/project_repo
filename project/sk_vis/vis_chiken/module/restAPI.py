from urllib.request import urlopen
import json
import os
from pandas.io.json import json_normalize
import time
from get_access import get_access

def restAPI(pid, token, page=1, count=100, dire="../data/"):
    directory = dire
    token = token
    for num, pid in enumerate(pids):
        page = 1
        info_url = 'https://api.bigdatahub.co.kr/v1/datahub/datasets/datainfo.json?pid={0}&TDCAccessKey={1}'.format(pid,token)
        con_url = 'https://api.bigdatahub.co.kr/v1/datahub/datasets/search.json?pid={0}&$count=1000&$page={2}&TDCAccessKey={1}'.format(pid,token,page)
        print(pid)
        response_info = urlopen(info_url).read().decode('utf-8')
        response_con = urlopen(con_url).read().decode('utf-8')
        page_max = round(json.loads(response_con)['totalResult']/1000)
        with open(directory + json.loads(response_info)['productName'] + '_=' + str(page) + '.json', 'w', encoding='utf-8') as f:
            f.write(response_con)
    
        for page in range(1,page_max+1):
            # print(page)
            con_url = 'https://api.bigdatahub.co.kr/v1/datahub/datasets/search.json?pid={0}&$count=1000&$page={2}&TDCAccessKey={1}'.format(pid,token,page)
            response_con = urlopen(con_url).read().decode('utf-8')
    
            with open(directory + json.loads(response_info)['productName'] +'_=' + str(page) +'.json', 'w', encoding='utf-8') as f:
                f.write(response_con)

def json2csv(json_dir, save = True, file_name='2013_2017_치킨데이터.csv'):
    start_time = time.time()
    df = pd.DataFrame(columns=['성별','시군구','시도','업종','연령대','요일','이용건수','년','월','일'])
    i = 0
    for file in os.listdir(json_dir)[1:]:
        with open(json_dir + '/' + file, 'r') as f:
            json_f = f.read()
            json_f = json.loads(json_f)
            csv = json_normalize(json_f['entry'])
            csv['년'] = csv['기준일'].apply(lambda x : x[:4])
            csv['월'] = csv['기준일'].apply(lambda x : x[4:6])
            csv['일'] =  csv['기준일'].apply(lambda x : x[6:8])
            csv.drop('기준일', axis=1, inplace=True)
        df = pd.concat([df,csv], axis=0)
        i += 1 
        if i % 10==0:
            print(i, df.shape)
            print(time.time()-start_time)
    if save:
        df.to_csv(json_dir +'/' + file_name, index=False, encoding='utf-8')
    return df
