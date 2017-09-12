## Dajngo와 Python Seleinum을 활용한 <br> Microsoft Azure 기반 분석 Restful API 서버 만들기.

## 프로젝트 하위 목표 
1. python selenium을 활용한 SK 데이터허브 공공데이터에 대한 자동 RestAPI 권한 획득 봇 개발.
2. 획득한 권한을 바탕으로 RestAPI 데이터 수집 크롤러 개발.
3. Python Django Framework와 MySQL을 활용한 ~~Microsoft Azure cloud~~ 기반 API서버 제작(무료 평가기간 만료로 python-anywhere로 마이그레이션) 

## 프로젝트 사용 데이터.
1. Sktelecom 사용자의 2013년부터 2017년 4월 까지의 치킨 주문 데이터<br>
데이터 예시: 2017년 1월 데이터 [바로가기](https://www.bigdatahub.co.kr/product/view.do?pid=1001463)

## 프로젝트 일정 (2017.6.14 ~ 2017.6.18(목표))

**2017.6.15**
* REST API 이용권한 자동 획득 봇 개발, [소스설명 코드바로가기](https://github.com/pizza12333/project_repo/blob/master/project/sk_vis/vis_chiken/DAY_2_REST_API_JSON_2_CSV.ipynb) // [완성코드 바로가기](https://github.com/pizza12333/project_repo/blob/master/project/sk_vis/vis_chiken/module/get_access.py)

* REST API를 통한 2013.08 ~ 2017.04의 치킨데이터 자동수집 [소스설명 코드바로가기](https://github.com/pizza12333/project_repo/blob/master/project/sk_vis/vis_chiken/DAY_2_REST_API_JSON_2_CSV.ipynb) // [완성코드 바로가기](https://github.com/pizza12333/project_repo/blob/master/project/sk_vis/vis_chiken/module/restAPI.py)

**2017.6.16 ~ 2017.6.17**
* Django Framework RestAPI web application 개발 ~~Microsoft Azure~~(수정:30일 무료평가기간 만료, python-anywhere로 마이그레이트)

**2017.6.18 ~ 2017.6.18**
* REST API 이용권한 자동 획득 봇 개발 + 치킨데이터 자동수집 크롤러 + Django RestAPI web application 완성
