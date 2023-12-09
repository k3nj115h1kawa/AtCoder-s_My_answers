# 合計金額の計算
def calc_total_amount(N, Y):
    for num10000 in range((Y//10000)+1):  # (Y//10000)+1 より多い枚数は考える必要がない
        if 10000*num10000 > Y:
            break
        for num5000 in range((Y//5000)-num10000+1):
            if (10000*num10000 + 5000*num5000) > Y:
                break

            num1000 = N - num10000 - num5000  # 10000円, 5000円, 1000円の合計枚数はNと同じである
            total = 10000*num10000 + 5000*num5000 + 1000*num1000
            if total == Y:
                return num10000, num5000, num1000
    else:
        return -1, -1, -1


# 実行部分
if __name__ == '__main__':
    # 入力
    N, Y = map(int, input().split(' '))

    # 合計金額の計算実行
    num10000, num5000, num1000 = calc_total_amount(N, Y)

    # 出力
    print(num10000, num5000, num1000)
