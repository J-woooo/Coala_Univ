#비만도 계산기
#1. 필요한 변수: height(키), weight(몸무게), BMI(BMI계산 결과)
#2. input함수로 받은 키와 몸무게가 문자열이기 때문에 int형으로 변환하여야 한다.
#3. 173/75의 BMI: 25.05930702662969
#4. 소스 코드
print("BMI 계산기 입니다.")
height = input("신장: ")
weight = input("몸무게: ")
height = int(height)
weight = int(weight)
BMI = weight / pow(height,2) * pow(10,4)
print("BMI:",BMI)