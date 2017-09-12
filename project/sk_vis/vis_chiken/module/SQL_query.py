import pymysql
import pandas as pd

def settingDB(host, user, pw, unix_socket, db_name, table_name):
    con = pymysql.connect(host=host,
                      user=user,
                      password=pw,
                      unix_socket =unix_socket)
    
    with con.cursor() as cursor:
        query = 'CREATE DATABASE {0};'.format(db_name)
        cursor.execute(query)
        result = cursor.fetchall() 
        print('데이터베이스 :{0} 가 생성됐습니다. 데이터베이스에 접속합니다.'.format(db_name))
    
    with con.cursor() as cursor:
        query = 'CREATE DATABASE {0};'.format(db_name)
        cursor.execute(query)
        result = cursor.fetchall() 
        print('데이터베이스 :{0} 가 생성됐습니다. 데이터베이스에 접속합니다.'.format(db_name))
    
    with con.cursor() as cursor:
        query = 'USE SK_DATA;'
        cursor.execute(query)
        
        query= '''CREATE TABLE {0} (
        ID int,
        Year int,
        Month int,
        Day int,
        Day_of_weeks varchar(255),
        Gender varchar(255),
        Age varchar(255),
        Loc_mid varchar(255),
        Loc_small varchar(255),
        Num_Call int);'''.format(table_name)
        cursor.execute(query)
        print('테이블 :{0} 가 생성됐습니다.'.format(table_name))
        
    print('데이터를 저장시작합니다.')
    
    start_time = time.time()
    
    try:
        with con.cursor() as cursor:
            for idx in range(0,data.shape[0]):
                query = '''INSERT INTO Chicken 
                (ID, Year, Month, Day, Day_of_weeks, Gender, Age, Loc_mid, Loc_small, Num_Call)
                VALUES 
                ({0},{1},{2},{3},"{4}","{5}","{6}","{7}","{8}",{9});'''.format(data.ix[idx][9],
                                                                     data.ix[idx][0],
                                                                     data.ix[idx][1],
                                                                     data.ix[idx][2],
                                                                     data.ix[idx][3],
                                                                     data.ix[idx][4],
                                                                     data.ix[idx][5],
                                                                     data.ix[idx][6],
                                                                     data.ix[idx][7],
                                                                     data.ix[idx][8])
    
                cursor.execute(query.encode('utf8'))
                result = cursor.fetchall() #fetchone은 한 개체만 출력
                if idx % 10000 == 0:
                    print(idx,'행 완료', time.time() - start_time)
    finally:
        con.commit()
        con.close()
        print('저장이 완료돼 연결을 종료합니다.')