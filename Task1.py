def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

assert average_num([1, 1]) == 1
assert average_num([2.5, 3.5]) == 3

assert average_num([000, 'OOO', 333]) == "Bad request" #1
assert average_num([1, 2, 3, 4, 5]) == 3 #2
assert average_num([1.0, 2.0, 3.0, 4.0, 5.0]) == 3 #3
assert average_num([1, 2.5, 3, 4.5, 5]) == 3.2 #4
assert average_num([-1, 2, -3, 4, -5]) == -0.6 #5
assert average_num([10, 50, 30]) == 30 #6
assert average_num([1, '2', 3]) == 2 #7
assert average_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5 #8
