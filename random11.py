import random

male = ['수퍼맨', '배트맨', '아쿠아맨', '아이언맨', '스파이더맨']
female = ['원더우먼', '캡틴마블', '블랙윈도우', '배트걸', '수퍼걸']

random.shuffle(male)
random.shuffle(female)

for i, (m, f) in enumerate(zip(male, female), 1):
    print(f"커플 {i} [{m}] - {i} [{f}]")
