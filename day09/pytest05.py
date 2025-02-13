# 5번 문제
# 클래스, 객체 생성 및 멤버변수 만들기

class SmartPhone:
    
    def __init__(self, phoneOwner, phoneNumber, company):
        self.phoneOwner = phoneOwner
        self.phoneNunber = phoneNumber
        self.company = company

    def __str__(self):
        retStr = f'{self.phoneOwner}\n{self.phoneNunber}\n{self.company}'
        return retStr
    
myPhone = SmartPhone('현민', '010-4222-5397', 'Samsung')
print(f'{myPhone.phoneOwner}의 전화번호는 {myPhone.phoneNunber}이고, 제조사는 {myPhone.company}입니다.')
print('전체 정보')
print(myPhone)