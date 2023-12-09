# 偶奇判定の実行
def even_or_odd(number: int) -> bool:
    judgment_result = True  # TrueであればEven, FalseであればOdd
    if (number//2)*2 != number:
        judgment_result = False
    return judgment_result

# 除算の実行


def division(N: int, nums: list, count_devision: int) -> int:
    # 偶奇判定の実行
    nums_judge = True  # 全てEven
    for i in range(N):
        num_judge = even_or_odd(nums[i])
        if num_judge == False:
            nums_judge = False

    # 除算の実行
    if nums_judge == True:
        count_devision += 1
        nums = [num//2 for num in nums]
        count_devision = division(N, nums, count_devision)

    return count_devision


# 実行部分
if __name__ == '__main__':
    # 入力
    N = int(input())
    nums = list(map(int, input().split(' ')))

    # 除算のカウンタ変数
    count_devision = 0

    # 実行
    count_devision = division(N, nums, count_devision)

    # 出力
    print(count_devision)
