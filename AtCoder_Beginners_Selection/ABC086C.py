# num1, num2が偶数同士であるか, または奇数同士であるかの判定
def even_or_odd_numbers(num1, num2, judgment_result):
    if (num1-num2) % 2 != 0:
        judgment_result = False
    return judgment_result

# 時間tの差が, xとyの合計の差以下であるかの判定


def movement_diff(t_x_y):
    judgment_result = True
    for i in range(len(t_x_y)-1):
        t_diff = t_x_y[i+1][0] - t_x_y[i][0]  # tの差
        x_y_diff = abs((t_x_y[i+1][1]+t_x_y[i+1][2]) -
                       (t_x_y[i][1]+t_x_y[i][2]))  # xとyの合計の差(絶対値)
        if t_diff < x_y_diff:
            judgment_result = False
        judgment_result = even_or_odd_numbers(
            t_diff, x_y_diff, judgment_result)  # 偶数同士であるか, または奇数同士であるかの判定
    return judgment_result


# 実行部分
if __name__ == '__main__':
    # 入力
    N = int(input())

    t_x_y_init = [0, 0, 0]  # 初期位置
    t_x_y = [list(map(int, input().split())) for i in range(N)]
    t_x_y.insert(0, t_x_y_init)

    # 出力
    if movement_diff(t_x_y):
        print('Yes')
    else:
        print('No')
