def count_vowelsPer_word(sentence: str) -> dict[str, int]:
    vowels = 'aeiouAEIOU'
    return {word: sum(1 for char in word if char in vowels and char.isalnum()) for word in sentence.split()}


from string
def count_vowels_per_word(sentence: str) -> dict[str, int]:
    vowels = set('aciouAEIOU')
    res = {}
    for word in sentence.split()
        key = word.strip(string.punctuation)
        count = sum(1 for ch in key if ch in vowels)
        res[key] = count
    return res
    

def fibonacci_sequence(n: int) -> list[int]:
    """
        ？
    """
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    seq = finonacci_sequence(n-1)
    return seq + [seq[-1] + seq[-2]]
    :q
def fibonacci_sequence(n: int, _memo: dict[int, list[int]] | None = None) -> list[int]:
    """ 使用 `_memo` 字典缓存已计算的前 k 项，避免重复子问题计算 """
    if n <= 0:
        return []
    if _memo is None:
        _memo = {}
    if n in _memo:
        return _memo[n]
    if n == 1:
        _memo[1] = [0]
        return [0]
    if n == 2:
        _memo[2] = [0, 1]
        return [0, 1]
    prev = fibonacci_sequence(n-1, _memo)
    _memo[n] = prev + [prev[-1] + prev[-2]]
    return _memo[n]


def char_frequency(s: str) -> dict[str, int]:
    


from fractions import Fraction
def subtract_fractions(fraction1: str|tuple[int, int], fraction2: str|tuple[int, int]) -> str:
    frac = Fraction(fraction1) - Fraction(fraction2)
    return f'{frac.numerator}/{frac.denominator}'



from collections import defaultdict
def word_length_distribution(sentence: str, min_len: int = 0, max_len: int | None = None) -> dict[int, int]:
    res = defaultdict(int)
    for word in sentence.split():
        len_word = sum(1 for char in word if char.isalnum())
        if len_word >= min_len and len_word <= max_len:
            res[int(len_word)] += 1
    return dict(res)
