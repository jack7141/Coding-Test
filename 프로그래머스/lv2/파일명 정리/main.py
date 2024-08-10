import re

def solution(files):
    answer = []

    for file in files:
        match = re.findall(r'(\D+)(\d+)(.*)', file)
        answer.append(match[0])
    # 람다에 두개 넣기!
    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(_answer) for _answer in answer]
    return answer



test_cases = [
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
]


for files in test_cases:
    print(solution(files))