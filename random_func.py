import random


def draw_lotto():
    num_list = []
    for i in range(45):
        num_list.append(i+1)
    lotto = random.sample(num_list, k=6)
    return sorted(lotto)

