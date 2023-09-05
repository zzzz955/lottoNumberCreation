import random


def draw_lotto():
    num_list = []
    for i in range(45):
        num_list.append(i+1)
    lotto = random.sample(num_list, k=6)
    return sorted(lotto)


def draw_lotto_fixed_range(appearance_nums):
    num_list = []
    for num in appearance_nums:
        num_list.append(int(num))
    lotto = random.sample(num_list, k=6)
    return sorted(lotto)