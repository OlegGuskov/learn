# from datetime import datetime
# start_time = datetime.now()
# print(datetime.now() - start_time)

# import time
# s_1 = time.time()
# s_2 = time.time() - s_1
# print(s_2)

# import random


"""
    привет!
           /> - フ
          |  o  o|
         /`ミ _x 彡
        /        |
       /   ヽ　  ﾉ
    ／￣|   | | |
    | (￣ヽ__ヽ_)_)
    ＼二つ
"""
"""

"""


# Тесты функций


def testing_function(func):

    print()
    print(f'Testing:  {func.__doc__}', end='\n\n')

    ref = 0

    # print('testcase 1', end='   ')
    print('testcase 1', end='\n\n')
    for key, value in ref.items():
        print(f'"{key}"', end='   ')
        result = f'{func(key)}'
        print(f'{result} OK!' if result == value else f'''Fail!
    reseived:{result} expected:{value}''')

#     # print('testcase 2', end='   ')
#     print('testcase 2', end='\n\n')
#     for n in range(1, 18):
#         print(f'"{str(n)}"', end='   ')
#         result = func(n)
#         print(f'{result} OK!' if r_list[r_list.index(result) - 1] <= n else
#               f'''Fail! There is a result less than {result}''')


# if __name__ == '__main__':
#     testing_function(is_password_good)
#     print(clean_dict)
