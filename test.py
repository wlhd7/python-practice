def fibonacci(n: int, _memo: dict[int, list[int]] = None, count: list = [0]) -> list[int]:
    count[0] += 1
    print(count[0])
    if n <= 0:
        return []
    if _memo is None:
        _memo = {1: [0], 2: [0, 1]}
    if n in _memo:
        return _memo[n]
    prev = fibonacci(n - 1, _memo, count)
    _memo[n] = prev + [prev[-1] + prev[-2]]
    return _memo[n]

count1 = [0]
fibonacci(5, None, count1)
print(f"fibonacci(5): 调用次数={count1[0]}") 

def fibonacci2(n: int, count: list = [0]) -> list[int]:
    count[0] += 1
    print(count[0])
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    prev = fibonacci2(n-1, count)
    return prev + [prev[-1] + prev [-2]]

count2 = [0]
fibonacci2(5, count2)
print(f"fibonacci2(5): 调用次数={count2[0]}")

def fibonacci3(n: int) -> tuple[list[int], int]:
    count = [0]
    def _fibonacci(n: int) -> list[int]:
        count[0] += 1
        if n <= 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        prev = _fibonacci(n-1)
        return prev + [prev[-1] + prev[-2]]
    return _fibonacci(n), count[0]

print(fibonacci3(5))

def fibonacci4(n: int) -> tuple[int, int]:
    count = [0]
    def _fibonacci(n: int):
        count[0] += 1
        if n == 1:
            return 0
        if n == 2:
            return 1
        return _fibonacci(n-1) + _fibonacci(n-2)
    return _fibonacci(n), count[0]

print(fibonacci4(5))

def fibonacci5(n: int, count: list[int] | None = None) -> int:
    if count is None:
        count = [0]
    count[0] += 1
    print(count[0])
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci5(n-1, count) + fibonacci5(n-2, count)

fibonacci5(5)

def fibonacci6(n: int, _memo: dict[int, list[int]] = None, count = [0]) -> list[int]:
    count[0] += 1
    print(count[0])
    if n <= 0:
        return []
    if _memo is None:
        _memo = {0: [0], 1: [0, 1]}
    if n in _memo:
        return _memo[n]
    prev = fibonacci6(n-1)
    _memo[n] = prev + [prev[-1] + prev[-2]]
    return _memo[n]

print('')
fibonacci6(5)
fibonacci6(5)

print('')
_memo = {}
fibonacci6(5, _memo)
fibonacci6(5, _memo)
