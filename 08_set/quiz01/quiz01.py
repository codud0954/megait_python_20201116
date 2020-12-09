photo = {'황예지', '임나연', '황광희', '장원영', '하성운', '권은비'}
dance = {'박명수', '하성운', '유재석', '박지민', '임나연'}
band = {'하성운', '민경훈', "권은비", '황광희'}

# 1. 3개의 동아리 중 하나 이상 가입된 사람들의 전체 명단을 중복 없이 출력하세요.
# 3개의 집합의 합집합
print("동아리에 하나 이상 가입된 사람:", photo | dance | band)

# 2. 댄스 동아리에만 가입된 사람의 명단을 출력하세요.
# dance 집합에서 photo와 band 집합을 차집합
print("댄스 동아리에만 가입한 사람:", dance - photo - band)

# 3. 3개의 동아리에 모두 가입된 사람
# 3개의 집합의 교집합
print("3개의 동아리에 모두 가입된 사람:", photo & dance & band)


# 각각의 교집합을 모두 구하고, 3개의 모두 가입된 사람을 제거하면 된다.
a = photo.intersection(dance)
b = photo.intersection(band)
c = dance.intersection(band)


print("2개의 동아리에 모두 가입된 사람:", (a | b | c) - (photo & dance & band))
