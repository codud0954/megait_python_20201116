# OmrCard
class OmrCard:
    # 생성자
    def __init__(self, name, school_id):
        self.name = name
        self.school_id = school_id
        self.answer_list = list()

    # 정답을 입력 받는 메소드
    def marking_answer(self, *answers):
        for answer in answers:
            self.answer_list.append(answer)

# OmrCardReader
class OmrCardReader:
    # 정답
    def __init__(self, *answer):
        self.real_answer_list = list()
        for answer in answer:
            self.real_answer_list.append(answer)

    # 카드를 읽어서 그 안에 있는 이름, 학번, 점수 계산 => 출력
    def read_omr_card(self, omr_card):
        i = 0  # index
        score = 0
        for real_answer in self.real_answer_list:   # 0 1 2 3 4
            if real_answer == omr_card.answer_list[i]: # 정답이면
                # 한 문제당 점수: 100 / 문제 개수
                score += 100 / len(self.real_answer_list)
            
            i += 1  # index 값을 1 증가

        print("이름:%s, 학번:%d, 점수:%g" % (omr_card.name, omr_card.school_id, score))

# 객체 생성
omrCard1 = OmrCard("신보람", 1)
omrCard1.marking_answer(1, 2, 3, 4, 5)
print(omrCard1.answer_list)

omrCardReader = OmrCardReader(1, 2, 2, 4, 5)
print(omrCardReader.real_answer_list)
omrCardReader.read_omr_card(omrCard1)

omrCard2 = OmrCard("김바다", 2)
omrCard2.marking_answer(1, 2, 2, 4, 5)

omrCardReader.read_omr_card(omrCard2)
