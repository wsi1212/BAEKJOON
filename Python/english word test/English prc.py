import random
numbers = list(range(0, 60))
random.shuffle(numbers)
print(numbers)
words = [["task", "업무"],
["achievement", "성취"],
["depend on", "~에 달려있다"],
["feedback", "반응, 의견"],
["ignore", "무시하다"],
["negative", "부정적인"],
["limit", "한계"],
["assume", "여기다. 생각하다"],
["determine", "결정하다"],
["mirror", "반영하다"],
["springboard", "발판"],
["ingrained", "깊이배어든. 타고난"],
["shift", "바꾸다"],
["be composed of", "~로 구성된"],
["bittions of", "수십억의"],
["transmit", "전송하다"],
["renew", "새로워지다"],
["stimulate", "자극하다"],
["discouraged", "낙담한"],
["neuron", "뉴런, 신경단위"],
["reveal", "드러내다"],
["on the other hand", "다른 한편으로는"],
["fixed", "고정된"],
["according to", "~에 따르면"],
["psychologist", "심리학자"],
["inherent", "타고난, 내재된"],
["determine", "결정하다"],
["tough", "어려운"],
["accomplish", "성취하다"],
["trait", "특성"],
["confirm", "확인하다"],
["neuroscience", "신경과학"],
["connection", "연결"],
["strengthen", "강화하다"],
["repeat", "반복하다"],
["lead to", "~로 이끌다. ~결과가 나오게 한다"],
["take on", "~에 도전하다. ~을 맡다"],
["progress", "발전"],
["recollection", "회상"],
["in terms of", "~의 측면에서"],
["install", "설치하다"],
["to the fullest", "최대한으로"],
["spooil", "망치다"],
["retain", "유지하다"],
["persistence", "끈기"],
["conquer", "정복하다"],
["exhausting", "지치게하는"],
["match", "시합"],
["optimism", "낙관주의"],
["get ahead", "나아가다"],
["take a step", "걸음을 내딛다"],
["keep your chin up", "기운내"],
["desire", "욕망, 갈망"],
["take in", "받아들이다, 섭취하다"],
["lack", "결핍"],
["speech", "연설, 말하기"],
["faith", "믿음"],
["closing remark", "맺음말"],
["draft", "원고"],
["edit", "편집하다"]]
for i in range(1, len(words)):
    print(words[numbers[i]][1], end=": ")
    a=input()
    print(words[numbers[i]][0], end="\n")