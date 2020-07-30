#문자열 슬라이싱 연습하기
yymmdd = input("생년월일을 6자리로 입력해주세요.(yymmdd): ")
print("-----------------")
year = yymmdd[0:2]
month = yymmdd[2:4]
day = yymmdd[4:]
print("당신의 생일은 "+year+"년"+month+"월"+day+"일입니다.")