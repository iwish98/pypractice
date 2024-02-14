import random

male = ['수퍼맨','배트맨','아쿠아맨','아이언맨','스파이더맨']
female = ['원더우먼','캡틴마블','블랙윈도우','배트걸','수퍼걸']

random.shuffle(male)
random.shuffle(female)

for i in range(1,6):
    print("커플 ",i,"[",male[i],"]")
    print("커플 ",i,"[",female[i],"]")


