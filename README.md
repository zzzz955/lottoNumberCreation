# lottoNumberCreation
--------기능--------
1. 로또 번호 무작위 생성
2. N회차 당첨 번호 확인
3. 지난 회차 기간 당첨번호 조회
4. 회차 데이터 분석 및 로또 번호 추천

# mainwindow.py
앱 실행 시 나타나는 메인 UI

1. 랜덤 뽑기
   ※ 45개 숫자 중 무작위로 6개의 숫자 추첨
2. 원하는 숫자만 선택
   ※ 내가 원하는 숫자만 선택하여 해당 숫자 중 무작위로 6개의 숫자 추첨
3. 당첨 정보 확인
   ※ 특정 회차의 당첨 번호 확인(웹 페이지 이동)
4. 지난 회차 당첨 데이터 추출
   ※ 특정 기간을 입력, 해당 기간 내 모든 회차의 당첨 번호 크롤링 후 다운로드
   ※ json, excel, csv 파일 지원
5. 데이터 기반 뽑기
   ※ 4. 번에서 추출한 데이터를 기반으로 사용자가 전달하는 데이터에 맞추어 분석 후 숫자 추첨

# mainfunc.py
모듈간 상호 작용을 위한 기능 모듈

# dialog.py
다이얼로그 기능 모음 모듈

# random_func.py
랜덤 기능 함수 모듈

# to_excel_csv.py
엑셀 및 csv 파일 다운로드 함수 모듈

# to_json_text.py
json 및 텍스트 파일 다운로드 함수 모듈

# crawling.py
네이버 웹 페이지 크롤링 함수 모듈

# lotto_prize_solution.py
업로드 데이터 가공 함수 모듈

# label_ui.py
로또 추첨 관련 QLabel ui 적용을 위한 모듈

# custom.xml
qt-materiar GUI 서식, 실행 파일과 동일한 경로에 위치 필요

# requiremodules.txt
설치가 필요한 모듈 모음
