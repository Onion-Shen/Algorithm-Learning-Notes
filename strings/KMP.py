from typing import List


def get_next_array_by_pattern(pattern: str, size: int) -> List[int]:
    array = [-1] * size

    k = -1
    for i in range(1, size):
        while k > -1 and pattern[k + 1] != pattern[i]:
            k = array[k]

        if pattern[k + 1] == pattern[i]:
            k += 1

        array[i] = k

    return array


def kmp_string_match(source: str, pattern: str) -> int:
    s_len, p_len = len(source), len(pattern)
    next_array = get_next_array_by_pattern(pattern, p_len)

    k = -1
    for i in range(0, s_len):
        while k > -1 and pattern[k + 1] != source[i]:
            k = next_array[k]

        if pattern[k + 1] == source[i]:
            k += 1

        if k == p_len - 1:
            return i - p_len + 1

    return -1
