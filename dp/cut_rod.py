from typing import Dict, List, Tuple

P: Dict[int, int] = {1: 1, 2: 5, 3: 8, 4: 9,
                     5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}


def cut_rod(n: int) -> int:
    if n == 0:
        return 0

    result = 0
    for i in range(1, n + 1):
        result = max(result, P[i] + cut_rod(n - i))

    return result


def memoized_cut_rod_aux(n: int, r: List[int]) -> int:
    if r[n] and r[n] >= 0:
        return r[n]

    result = 0
    if n > 0:
        for i in range(1, n + 1):
            result = max(result, P[i] + memoized_cut_rod_aux(n - i, r))

    r[n] = result
    return result


def memoized_cut_rod(n: int) -> int:
    r = [None] * (n + 1)
    return memoized_cut_rod_aux(n, r)


def bottom_up_cut_rod(n: int) -> int:
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        result = 0
        for i in range(1, j + 1):
            result = max(result, P[i] + r[j - i])
        r[j] = result
    return r[n]


def extented_bottom_up_cut_rod(n: int) -> Tuple[List[int], List[int]]:
    r = [None] * (n + 1)
    s = [None] * (n + 1)

    for j in range(1, n + 1):
        result = 0
        for i in range(1, j + 1):
            r_item = r[j - i] if r[j - i] else 0
            if result < P[i] + r_item:
                result = P[i] + r_item
                s[j] = i
                r[j] = result

    return (r, s)


def print_cut_rod_solution(n: int):
    _, s = extented_bottom_up_cut_rod(n)
    while n > 0:
        print(s[n])
        n -= s[n]
