# 合計金額が合致するものの計測
def sum_result(nums500, nums100, nums50, total_amount, result_count):
    for num500 in range(0, nums500 + 1):
        for num100 in range(0, nums100 + 1):
            for num50 in range(0, nums50 + 1):
                total = 500*num500 + 100*num100 + 50*num50
                if total == total_amount:
                    result_count += 1
    return result_count


# 実行部分
if __name__ == '__main__':
    # 入力
    A = int(input())  # 500円玉の枚数
    B = int(input())  # 100円玉の枚数
    C = int(input())  # 50円玉の枚数
    X = int(input())  # 合計金額

    result_count = 0

    # 計算の実行
    result_count = sum_result(A, B, C, X, result_count)

    # 出力
    print(result_count)
