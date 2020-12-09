books_dict = {'말 그릇':'김윤나', '마음의 미래':'미치오 카쿠', '메모의 마법':'마에다 유지', '시간은 흐르지 않는다':'카를로 로벨리', '평행우주':'미치오 카쿠'}

# 1. 책 이름으로 저자 찾기
print(books_dict['시간은 흐르지 않는다'])
#또는
print(books_dict.get('시간은 흐르지 않는다'))

# 2. 책 추가하기
'''
* 책: 코스모스, 저자: 칼 세이건
* 책: 해변의 카프카, 저자: 무라카미 하루키
'''

books_dict['코스모스'] = '칼 세이건'
books_dict['해변의 카프카'] = '무라카미 하루키'
print(books_dict)

# 3. 책 이름 출력하기
book_names = list(books_dict.keys())
print(book_names)

# 4. 책의 저자 출력하기
book_writers = set(list(books_dict.values()))
print(book_writers)
