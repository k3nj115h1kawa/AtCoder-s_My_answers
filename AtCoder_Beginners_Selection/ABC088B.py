# リストのソートの実行(バブルソート)
def bubble_sort(nums: list) -> list:
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] < nums[j+1]:  # 降順にソート
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# 得点差の計算


def score_diff(nums: list, N: int, score: int) -> int:
    nums = bubble_sort(nums)
    for i in range(N):
        if i % 2 == 0:
            score += nums[i]
        else:
            score -= nums[i]
    return score


# 実行部分
if __name__ == '__main__':
    # 入力
    N = int(input())
    card_list = list(map(int, input().split(' ')))

    score = 0  # 得点差

    # 計算の実行
    score = score_diff(card_list, N, score)

    # 出力
    print(score)
