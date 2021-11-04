가격 = 1000
부가가치세율 = 0.1
print(가격*부가가치세율)

# 변수는 데이터에 이름을 붙이고
# 리스트는 서로 연관된 데이터를 묶어서 이름을 붙인다.
# 함수를 서로 연관된 코드를 그룹핑해서 이름을 붙인다.

# 함수
def get_vat(가격):
    부가가치세율 = 0.1
    print(가격*부가가치세율)

get_vat(10000)
get_vat(20000)
get_vat(100)

get_vat(float(input('얼마요?')))

# 함수 none
# 함수를 print하면 none이 된다
def get_vat(가격):
    부가가치세율 = 0.1
    print(가격*부가가치세율)

print(get_vat(float(input('얼마요?'))))


# 함수 return
# 함수가 값이 되기 위해서 return을 써줘야한다
def get_vat(가격):
    부가가치세율 = 0.1
    return 가격*부가가치세율

print(get_vat(float(input('얼마요?'))))
