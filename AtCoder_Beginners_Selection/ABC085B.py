# 選択ソート
def select_sort(nums: list) -> list:
    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

# 段数の計測


def diameter_diff(nums: list, N: int, stages: int) -> int:
    # ソートの実行
    nums = select_sort(nums)

    # 段数の計測(ソート後)
    for tmp_idx in range(N-1):
        if nums[tmp_idx] < nums[tmp_idx + 1]:
            stages += 1
    stages += 1
    return stages


# 実行部分
if __name__ == '__main__':
    # 入力
    N = int(input())
    diameter_list = [int(input()) for i in range(N)]

    stages = 0  # 合計段数

    # 計算の実行
    stages = diameter_diff(diameter_list, N, stages)

    # 出力
    print(stages)
