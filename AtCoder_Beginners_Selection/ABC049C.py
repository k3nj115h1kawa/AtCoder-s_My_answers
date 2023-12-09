# 文字列の中に該当するものがあるか判定(文末から)
def fit_judge(line, fit_line):
    judgment = True
    if len(line) < len(fit_line):
        judgment = False
        return judgment
    for i in range(1, len(fit_line)+1):
        if line[-i] != fit_line[-i]:
            judgment = False
            break
    return judgment

# 判定の繰り返し


def judge_loop(line, fit_list):
    msg = 'YES'
    while len(line) > 0:
        valid_idx = 0  # 文字列が該当する部分があるときの, fit_listのインデックス
        judgment_result_idx = [i for i in range(
            len(fit_list)) if fit_judge(line, fit_list[i]) == True]
        if len(judgment_result_idx) == 0 and len(line) > 0:
            msg = 'NO'
            return msg
        elif len(judgment_result_idx) > 0:
            valid_idx = judgment_result_idx[-1]   # リスト内で最後の部分を選択
            line = line[:-len(fit_list[valid_idx])]  # 該当する部分の文字列削除
    return msg


# 実行部分
if __name__ == '__main__':
    # 入力
    line = input()

    fit_list = ['dream', 'dreamer', 'erase', 'eraser']

    # 計算の実行
    msg = judge_loop(line, fit_list)

    # 出力
    print(msg)
