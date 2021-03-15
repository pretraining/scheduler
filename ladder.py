import sys
import time
import random
from termcolor import colored


MEMBERS = ['강재호', '고우영', '김대규', '김보섭', '김형석', 
           '김형준', '류민호', '류인제', '문영기', '백혜림',
           '양승무', '유원준', '최정', '최태균', '황동현']
TEAMS = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]


assert len(MEMBERS) == len(TEAMS)


def count_down():
    print("===========================")
    print("=      o o o o o o o      =")
    print("=                  o      =")
    print("=                  o      =")
    print("=                  o      =")
    print("=      o o o o o o o      =")
    print("=                  o      =")
    print("=                  o      =")
    print("=                  o      =")
    print("=      o o o o o o o      =")
    print("===========================")
    time.sleep(1)
    print("===========================")
    print("=      o o o o o o o      =")
    print("=                  o      =")
    print("=                  o      =")
    print("=                  o      =")
    print("=      o o o o o o o      =")
    print("=      o                  =")
    print("=      o                  =")
    print("=      o                  =")
    print("=      o o o o o o o      =")
    print("===========================")
    time.sleep(1)
    print("===========================")
    print("=            o            =")
    print("=            o            =")
    print("=            o            =")
    print("=            o            =")
    print("=            o            =")
    print("=            o            =")
    print("=            o            =")
    print("=            o            =")
    print("=            o            =")
    print("===========================")
    time.sleep(1)

def assign(members, teams):
    random.shuffle(members)
    print("***************************")
    for i, (member, team) in enumerate(zip(members, teams)):
        if i % 5 == 0:
            print(colored("%s\t-> t%d (team leader)" % (member, team), 'yellow'))
        else:
            print("%s\t-> t%d" % (member, team))
        if (i + 1) % 5 == 0 and i < len(MEMBERS) - 1:
            print("---------------------------")
    print("***************************")

if __name__ == "__main__":
    count_down()
    assign(MEMBERS, TEAMS)
