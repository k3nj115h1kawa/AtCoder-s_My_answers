# 実行部分
if __name__ == '__main__':
    # 入力
    a = int(input())
    b, c = map(int, input().split(' '))
    s = input()

    # 合計の計算
    total = a + b + c

    # 出力
    print(str(total) + ' ' + s)
