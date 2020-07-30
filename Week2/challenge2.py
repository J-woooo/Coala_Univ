data = ["조회 수: 1,500", "조회 수: 1,002","조회 수: 300","조회 수: 251","조회 수: 13,432","조회 수: 998"]
sum = 0
#LV1: for문을 사용하여 조회수를 출력
for d in data:
    print(d)
#LV2: 문자열을 수정하여 숫자만 출력
for d in data:
    score = d[6:].replace(",","")
    print(score)
#LV3: 조회수의 총합 출력
for d in data:
    score = d[6:].replace(",","")
    sum+=int(score)
print("총 합:",sum)