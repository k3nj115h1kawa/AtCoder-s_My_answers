# 偶奇判定の関数
def evenorodd(num1, num2):
    judgment_result = True  # TrueならEven, FalseならOdd
    product = num1 * num2
    if int((int(product/2))*2) != product:
        judgment_result = False
    return judgment_result


# 実行部分
if __name__ == '__main__':
    # 入力
    a, b = map(int, input().split(' '))

    # 偶奇判定
    judgment_result = evenorodd(a, b)
    if judgment_result:
        print('Even')
    else:
        print('Odd')
