# 딕셔너리
member = {'name':'egoing', 'city':'Seoul', 'job':'WEB'}
print(member['name'])
print(member['city'])

# 순서가 있는 것은 리스트에 담고 색인을 통해서 식별하고
# 순서가 없는 것은 딕셔너리에 담고 이름을 통해서 식별한다.
# 자릿수는 기억하기 어렵지만 이름은 기억하기가 쉽다.

# 2차원 딕셔너리
member = [
    {'name':'egoing', 'city':'Seoul', 'job':'WEB'},
    {'name':'leezche', 'city':'Jeju', 'job':'Design'}
]
print(members[0]['city'])
for member in members:
    print(member['name'], member['city'], member['job'])


