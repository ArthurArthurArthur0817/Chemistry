def get_correct_classifications():
    # 定義正確的分類答案
    correct_safe = ["佩戴護目鏡"]
    correct_danger = ["使用未經允許的化學品"]
    return correct_safe, correct_danger

def validate_classification(safe, danger):
    # 取得正確的答案
    correct_safe, correct_danger = get_correct_classifications()

    # 驗證用戶的分類是否正確
    is_correct = set(safe) == set(correct_safe) and set(danger) == set(correct_danger)
    return is_correct
