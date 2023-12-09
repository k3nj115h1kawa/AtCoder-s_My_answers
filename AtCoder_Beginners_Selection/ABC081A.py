# 1がある部分のカウント
def count_only_1(s1s2s3):
    count = 0  # 1がある部分をカウントする変数
    s1 = s1s2s3[0]
    s2 = s1s2s3[1]
    s3 = s1s2s3[2]

    # 1のカウント実行
    if s1 == '1':
        count += 1
    if s2 == '1':
        count += 1
    if s3 == '1':
        count += 1

    # 結果を返す
    return count


# 実行部分
if __name__ == '__main__':
    # 入力
    s1s2s3 = input()

    # 計算の実行
    nums = count_only_1(s1s2s3)

    # 出力
    print(nums)
