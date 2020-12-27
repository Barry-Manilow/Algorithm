import random
import string

# 难度⭐️:排序数组、3个字符串拼接、不考虑超大数
def solution_1(nums_list, n):
    if nums_list is None or len(nums_list) == 0:
        return ""
    if len(nums_list) == 1:
        return nums_list[0]
    if len(nums_list) == 2:
        str_1 = nums_list[0] + nums_list[1]
        str_2 = nums_list[1] + nums_list[0]
        max_str = str_1 if str_1 > str_2 else str_2
        return max_str

    # 取出最后3个
    if all(nums_list) is False:
        return ""
    sorted_nums = list(map(str, sorted(map(int, nums_list), reverse=True)))
    last_three_num = sorted_nums[:3]
    if all(last_three_num) is False:
        return ""
    # 生成3个字符串所有可能组合
    str_list = [last_three_num[0] + last_three_num[1] + last_three_num[2],
                last_three_num[0] + last_three_num[2] + last_three_num[1],
                last_three_num[1] + last_three_num[0] + last_three_num[2],
                last_three_num[1] + last_three_num[2] + last_three_num[0],
                last_three_num[2] + last_three_num[0] + last_three_num[1],
                last_three_num[2] + last_three_num[1] + last_three_num[0]]
    max_str = str(max(map(int, str_list)))
    return max_str


# 难度⭐⭐️:排序数组、3个字符串拼接、考虑超大数
def solution_2(nums_list, n):
    if nums_list is None or len(nums_list) == 0:
        return ""
    if len(nums_list) == 1:
        return nums_list[0]
    if len(nums_list) == 2:
        str_1 = nums_list[0] + nums_list[1]
        str_2 = nums_list[1] + nums_list[0]
        max_str = str_1 if str_1 > str_2 else str_2
        return max_str

    # 取出最后3个
    if all(nums_list) is False:
        return ""
    sorted_nums = list(map(str, sorted(map(int, nums_list))))
    last_three_num = sorted_nums[len(sorted_nums) - 3:]
    # 生成3个字符串所有可能组合
    str_list = [last_three_num[0] + last_three_num[1] + last_three_num[2],
                last_three_num[0] + last_three_num[2] + last_three_num[1],
                last_three_num[1] + last_three_num[0] + last_three_num[2],
                last_three_num[1] + last_three_num[2] + last_three_num[0],
                last_three_num[2] + last_three_num[0] + last_three_num[1],
                last_three_num[2] + last_three_num[1] + last_three_num[0]]
    max_str = sorted(str_list, reverse=True)
    return max_str[0]


# 难度⭐⭐⭐️:排序数组、n个字符串拼接、考虑超大数
def solution_3(nums_list, n):
    if nums_list is None or len(nums_list) == 0:
        return ""
    if len(nums_list) == 1:
        return nums_list[0]
    if len(nums_list) == 2:
        str_1 = nums_list[0] + nums_list[1]
        str_2 = nums_list[1] + nums_list[0]
        max_str = str_1 if str_1 > str_2 else str_2
        return max_str

    class LargeValue(str):
        def __lt__(self, y):
            return self + y > y + self
    if all(nums_list) is False:
        return ""
    sorted_nums = list(map(str, sorted(map(int, nums_list), reverse=True)))
    last_n_num = sorted_nums[0:n]
    # 最长的3个字符串按str1 str2拼接后的字典序降序排序
    sorted_max_n = sorted(last_n_num, key=LargeValue)
    max_str = "".join(sorted_max_n)
    return max_str


# 难度⭐⭐⭐️⭐: 无序数组、n个字符串拼接、考虑超大数
def solution_4(nums_list, n):
    if nums_list is None or len(nums_list) == 0:
        return ""

    class LargeLen(str):
        def __lt__(x, y):
            if len(x) == len(y):
                return x + y > y + x
            else:
                return len(x) > len(y)

    class LargeValue(str):
        def __lt__(x, y):
            return x + y > y + x
    # 按字符串长度进行降序排序
    sorted_nums = sorted(nums_list, key=LargeLen)
    max_three = sorted_nums[:n]
    # 最长的3个字符串按ascii码值进行降序排序
    sorted_max_three = sorted(max_three, key=LargeValue)
    max_str = "0" if sorted_nums[0] == "0" else "".join(sorted_max_three)
    return max_str


def generate_random_str():
    """
    生成0-10位间任意位数的字符串，且不以0开头
    :return:
    """
    first_str = '123456789'
    str_length = random.randint(0, 20)
    random_str = str(random.choice(first_str))
    str_list = [str(random.choice(string.digits)) for m in range(str_length)]
    random_str = random_str + ''.join(str_list)
    return random_str


def generate_random_str_array():
    """
    # 生成0-100个长度在10以内的数组字符串
    :return:
    """
    str_array = []
    array_length = random.randint(0, 100)
    for i in range(array_length):
        random_str = generate_random_str()
        str_array.append(random_str)
    # 对生成的随机数字字符串按数值大小进行升序排序
    # sorted_nums = list(map(str, sorted(map(int, str_array))))
    return str_array


def test_manual_case(solution_function, num_count=3):
    test_case_list = [None,
                      [],
                      [""],
                      ["234"],
                      ["", ""],
                      ["", "12"],
                      ["10", "19"],
                      ["2", "13"],
                      ["2", "33"],
                      ["2", "20"],
                      ["3333333", "33333333333334"],
                      ["3333333", "33333333333332"],
                      ["24853", "2485324853248532485324853247"],
                      ["24853", "2485324853248532485324853249"],
                      ["", "", ""],
                      ["", "12", "13"],
                      ["10", "18", "19"],
                      ["2", "13", "122"],
                      ["2", "33", "345"],
                      ["2", "220", "2220"],
                      ["333", "3333334", "3333333332"],
                      ["24853", "2485324853247", "2485324853248532486"],
                      ["24853", "2485324853249", "2485324853248532484"],
                      ["1", "20", "300", "400", "3000", "23000", "220000", "3450000"],
                      ["39", "38", "37", "36", "35"],
                      ["30", "32", "44", "46", "59"],
                      ["9", "80", "7000", "6000", "50000", "400000"],
                      ["9", "80", "6000", "7000", "50000", "400000"],
                      ["900000", "80000", "7000", "600", "50", "4"],
                      ["100000", "20000","3000","400","50","6",],
                      ["9", "80", "700", "6000", "50000", "400000"],
                      ["1", "20", "300", "4000", "50000", "600000"],
                      ["9", "80", "7000", "6000", "50000", "400000"],
                      ["9", "80", "6000", "7000", "50000", "400000"],
                      ["1", "20", "300", "400", "50", "6", "70", "800", "9000", "910", "92"]
    ]
    result_list = ["", "", "", "234", "",
                   "12",
                   "1910",
                   "213",
                   "332",
                   "220",
                   "333333333333343333333",
                   "333333333333333333332",
                   "248532485324853248532485324853247",
                   "248532485324853248532485324924853",
                   "",
                   "1312",
                   "191810",
                   "213122",
                   "345332",
                   "22220220",
                   "33333343333333333332",
                   "2485324853248532486248532485324853247",
                   "2485324853249248532485324853248532484",
                   "345000023000220000",
                   "393837",
                   "594644",
                   "700050000400000",
                   "700050000400000",
                   "900000800007000",
                   "300020000100000",
                   "600050000400000",
                   "600000500004000",
                   "700050000400000",
                   "700050000400000",
                   "9109000800"]
    wrong_result = []
    test_times = len(test_case_list)

    for i in range(test_times):
        res_1 = solution_function(test_case_list[i], num_count)
        res_2 = result_list[i]
        if res_1 and res_2 and int(res_1) != int(res_2):
            wrong_result.append(["测试用例编号：{0}, 算法输出结果：{1}, 预期结果：{2}".format(i, res_1, res_2)])
    precision_rate = 1 - len(wrong_result) / test_times
    print("错误用例：\n")
    for i in range(len(wrong_result)):
        print(wrong_result[i])
    print("准确率：", precision_rate)


def test_auto_case(test_times, solution_function, base_compare_func, num_count=3):
    wrong_result = []

    for i in range(test_times):
        # 生成随机测试用例
        nums = generate_random_str_array()
        res_1 = base_compare_func(nums, num_count)
        res_2 = solution_function(nums, num_count)

        if res_1 and res_2:
            if int(res_1) != int(res_2):
                wrong_result.append(["测试用例编号：{0}, 预期结果：{1}, 算法输出结果：{2}".format(i, res_1, res_2)])
    precision_rate = 1 - len(wrong_result)/test_times
    print("错误用例：")
    for i in range(len(wrong_result)):
        print(wrong_result[i])
    print("准确率：", precision_rate)


if __name__ == '__main__':
    # 测试：solution_1
    test_manual_case(solution_1, 3)

    # 测试：solution_2
    test_manual_case(solution_2, 3)

    # 测试：solution_3
    # 测试10万次
    test_times = 100000
    test_manual_case(solution_3, 3)
    test_auto_case(test_times, solution_3, solution_2, 3)

    # 测试：solution_4
    # 测试10万次
    test_times = 100000
    test_manual_case(solution_4, 3)
    test_auto_case(test_times, solution_4, solution_3, 10)



