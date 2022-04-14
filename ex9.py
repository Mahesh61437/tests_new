import json


def add_dept(d, p1, p2, m):
    if d.get(p1):
        d[p1]['tot_dept'] += m
    else:
        d[p1] = {"tot_dept": m, "tot_owns": 0}

    if d[p1].get(p2):
        d[p1][p2]["dept"] += m
    else:
        d[p1][p2] = {"dept": m, "owns": 0}


def add_owns(d, p1, p2, m):
    if d.get(p2):
        d[p2]['tot_owns'] += m
    else:
        d[p2] = {"tot_dept": 0, "tot_owns": m}

    if d[p2].get(p1):
        d[p2][p1]["owns"] += m
    else:
        d[p2][p1] = {"dept": 0, "owns": m}


def max_debt(d):
    max_d = 0
    person = None
    for key, value in d.items():
        if value['tot_dept'] > max_d:
            max_d = value['tot_dept']
            person = key

    print(person, max_d)


def max_owns(d):
    max_o = 0
    person = None
    for key, value in d.items():
        if value['tot_owns'] > max_o:
            max_o = value['tot_owns']
            person = key

    print(person, max_o)

n = int(input())

d = {}

for _ in range(n):
    p1 = input()
    p2 = input()
    m = int(input())
    add_owns(d, p1, p2, m)
    add_dept(d, p1, p2, m)

print(json.dumps(d))
max_debt(d)
max_owns(d)
