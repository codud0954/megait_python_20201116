def word_count(word, char):
    count = word.count(char)
    return count


word = input("단어를 입력하세요:")
print("e의 개수는 %d개 입니다." % word_count(word, 'e'))
