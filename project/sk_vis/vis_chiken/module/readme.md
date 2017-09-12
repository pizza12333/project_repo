## 모듈 디렉토리

1. get_access.py : 
  - get_access(Id, pw, query) 함수가 존재합니다. 
  
  - get_access(Id, pw, query) 함수
  
  - 인자 설명
    * Id (문자형[str]) : Sk 데이터허브의 로그인 아이디를 전달 받아 로그인합니다.
    * pw (문자형[str]) : Sk 데이터허브의 로그인 비밀번호를 전달 받아 로그인합니다.
    * query (문자형[str]) : 로그인 후 전체 데이터 찾기 페이지에서 검색할 키워드를 입력 받아 검색합니다. 프로젝트에 사용되는 데이터를 위해서 "치킨" 을 입력합니다.
  
  
  - 반환 : 
    * pid_num (리스트 혹은 문자형[List | str]) : query 인자를 통해 검색된 모든 데이터들의 Data_Id를 반환합니다. 이 Data_Id는 추후 REST API의 $pid 파라미터에 입력됩니다.
    
2. restAPI.py
  - restAPI(pid, token, page=1, count=100) 함수와 json2csv(json_dir, save = True, file_name='2013_2017_치킨데이터.csv') 함수가 존재합니다.
  
  - restAPI(pid, token, page=1, count=100) 함수
  
  - 인자설명 
    * pid (리스트 혹은 정수형[List | int]) : get_access.py의 get_access함수의 반환값으로 REST API의 $pid 파라미터를 전송합니다.
    * token (문자형[str]) : Sk 데이터허브의 API token 값을 전송합니다.
    * page (정수형[int] default=1) : REST API의 $page 파라미터를 전송합니다. default값은 1입니다.
    * count (정수형[int] default=100) : REST API의 $count 파라미터를 전송합니다. default값은 100입니다.
   
  - json2csv(json_dir = '.', save = True, file_name='2013_2017_치킨데이터.csv')함수

  - 인자설명 
    * json_dir (문자형[str], default='.') : json 파일이 저장된 디렉토리입니다. default 값은 '.'로 현재 작업 디렉토리입니다.
    * save (불리언[bool], default=True) : Ture일 경우 REST API의 모든 page를 json파일로 로컬에 저장합니다. False일 경우 로컬에 저장하지 않습니다. default 값은 True 입니다.
    * file_name (문자형[str], default='2013_2017_치킨데이터.csv') : json을 결합한 csv파일명을 지정합니다. default 값은 '2013_2017_치킨데이터.csv' 입니다.
    - 반환 : 
    * df (pandas.DataFrame) : 설정된 디렉토리내 모든 json파일을 결합하여 pandas 데이터프레임으로 반환합니다.


3. restAPI.py
  - settingDB(host, user, pw, unix_socket, db_name, table_name)
  - 인자설명 
  * host(문자형[str]) : 사용할 MySQL의 host의 주소입니다.
  * user(문자형[str]) : 사용할 MySQL의 권한을 갖은 user name입니다.
  * pw (문자형[str]) : 사용할 MySQL의 user name의 비밀번호 입니다.
  * unix_socket(문자형[str]) : MySQL의 소켓 경로입니다.
  * db_name(문자형[str]) :  생성할 DB의 이름입니다.
  * table_name(문자형[str]) :  생성할 테이블 이름입니다.
