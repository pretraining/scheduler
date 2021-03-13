import random

MEMBERS = ['고우영', '김보섭', '김형석', '김형준', '류민호', '류인제', '문영기', '양승무', '유원준', '최정', '최태균', '황동현']
TEAMS = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

def assign(members, teams):
    random.shuffle(members)
    print("************")
    for i, (member, team) in enumerate(zip(members, teams)):
        print("%s\t-> %d" % (member, team))
        if (i + 1) % 4 == 0:
            print("------------")
    print("************")

if __name__ == "__main__":
    assign(MEMBERS, TEAMS)
