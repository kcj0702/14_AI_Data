# ======================================
#  27.2 예제 문자열 여러 줄을 파일에 쓰기, 읽기
print("="*5, "27.2 예제", "="*5)

with open('hello.txt', mode='w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
with open('hello.txt', mode='a', encoding='utf-8') as file:
    file.writelines(lines)

with open('hello.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)

with open('hello.txt', mode='r', encoding='utf-8') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

with open('hello.txt', 'r', encoding='utf-8') as file:
    for line in file:               # file 객체는 iterator이므로 언패킹도 가능(줄개수와 변수 개수 일치)
        print(line.strip())

print("="*21)
# ======================================
#  27.4 퀴즈
print("="*5, "27.4.1 퀴즈", "="*5)
print("""다음 중 파일에 문자열을 쓸 때 파일 열기 방법으로 올바른 것을 고르세요. ----- 답(d)
 a. file = open('hello.txt', 'r')           #  ==> X
 b. file = open('hello.txt', 'b')           #  ==> X
 c. file = open('hello.txt', 'rb')          #  ==> X
 d. file = open('hello.txt', 'w')           #  ==> O, wt에서 t를 생략하여 w만 적어도 무방
 e. file = open('hello.txt', 'wb')          #  ==> X""")
print("="*23)

print("="*5, "27.4.2 퀴즈", "="*5)
print("""다음 중 파일에서 문자열을 한 줄씩 읽어서 리스트 형태로 가져오는 메서드로 올바른 것을 고르세요. ----- 답(c)
 a. read                                    #  ==> X, 괄호 안에 값이 없다면 전체 데이터를 읽음
 b. readline                                #  ==> X, 파일의 첫 줄만 읽어서 반환
 c. readlines                               #  ==> O
 d. writelines                              #  ==> X, 인수로 리스트가 들어가며, 리스트 내의 요소들을 한 줄에 씀
 e. write                                   #  ==> X, 괄호 내의 인수를 씀""")
print("="*23)

# ======================================
#  27.5 연습문제: 파일에서 10자 이하인 단어 개수 세기
print("="*5, "27.5 연습문제", "="*5)

with open('words_prac.txt', 'w', encoding='utf-8') as f:
    words = ['anonymously\n', 'compatibility\n', 'dashboard\n', 'ex[experience\n', 'photography\n', 'spotlight\n', 'warehouse\n']
    f.writelines(words)

with open('words_prac.txt', 'r', encoding='utf-8') as f:
    cnt = 0
    for word in f:
        if len(word.rstrip('\n')) >= 10:
            cnt += 1
    print(cnt)

print("="*25)
# ======================================
#  27.6 심사문제: 특정 문자가 들어있는 단어 찾기
print("="*5, "27.6 심사문제", "="*5)

with open('words_exam.txt', 'w', encoding='utf-8') as f:
    f.write('Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.')

import string
with open('words_exam.txt', 'r', encoding='utf-8') as f:
    words = f.readline().split()
    print(*[word.strip(string.punctuation) for word in words if word.find('c')!=-1], sep='\n')

print("="*25)
# ======================================
#  28.1 예제 회문 판별하기 
print("="*5, "28.1 예제", "="*5)

word = input('단어를 입력하세요.')
ispalindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        ispalindrome = False
        break
print(ispalindrome)

print(word == word[::-1])

print(list(word) == list(reversed(word)))

print(word == "".join(reversed(word)))

print("="*21)
# ======================================
#  28.2 예제 N-gram 만들기
print("="*5, "28.2 예제", "="*5)

text = 'Hello'
for i in range(len(text) - 1):
    print(text[i], text[i+1], sep='')

text = 'this is python script'
words = text.split()
for i in range(len(words)-1):
    print(words[i], words[i+1])

text = 'hello'
two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep="")

text = 'this is python script'
words = text.split()
for i in zip(words, words[1:]):
    print(i[0], i[1])

text = 'hello'
three_gram = [text[i:] for i in range(3)]
for i in zip(*three_gram):
    for j in range(3):
        print(i[j], end="")
    print()

print("="*21)
# ======================================
#  28.3 연습문제: 단어 단위 N-gram 만들기
print("="*5, "28.3 연습문제", "="*5)

n = int(input())
text = input()
words = text.split()

if len(words) < n:
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)

print("="*25)
# ======================================
#  28.4 심사문제: 파일에서 회문인 단어 출력하기
print("="*5, "28.4 심사문제", "="*5)

txt = ['apache', 'decal', 'did', 'neep', 'noon', 'refer', 'river']
with open('words_28exam.txt', 'w', encoding='utf-8') as f:
    f.writelines([word+'\n' for word in txt])

with open('words_28exam.txt', 'r', encoding='utf-8') as f:
    for word in f:
        temp = word.strip('\n')
        if temp == temp[::-1]:
            print(temp)

print("="*25)
# ======================================