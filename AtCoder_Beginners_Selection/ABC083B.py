# A <= 各桁の和 <= B であるかの判定と, そのときの数
def judge_each_digit(num, A, B):
    judgment_result = False
    num_str = str(num)
    # 各桁の和を計算
    total = 0
    for i in range(len(num_str)):
        total += int(num_str[i])
    if A <= total <= B:
        judgment_result = True

    return judgment_result, num


# 実行部分
if __name__ == '__main__':
    # 入力
    N, A, B = map(int, input().split(' '))

    # 計算の実行
    judgment_true_num = [judge_each_digit(num, A, B)[1] for num in range(
        1, N+1) if judge_each_digit(num, A, B)[0] == True]

    # 出力
    print(sum(judgment_true_num))
