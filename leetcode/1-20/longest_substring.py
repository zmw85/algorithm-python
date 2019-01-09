def longest_substring_1(s):
    'brutal force'
    if not s:
        return 0

    str_length = len(s)
    longest_substr = 0
    for i in range(str_length):
        map = {s[i]: 1}
        substr = s[i]

        for j in range(i + 1, str_length):
            if map.get(s[j]) is not None:
                break
            substr = substr + s[j]
            map[s[j]] = 1

        if len(substr) > longest_substr:
            longest_substr = len(substr)

    return longest_substr


def longest_substring_2(s):
    'sliding window'
    if not s:
        return 0

    str_length = len(s)
    longest_substr = i = j = 0
    char_set = set()

    while i < str_length and j < str_length:
        if s[j] not in char_set:
            char_set.add(s[j])
            j += 1
            longest_substr = max(longest_substr, j - i)
        else:
            char_set.remove(s[i])
            i += 1

    return longest_substr


def longest_substring_3(s):
    'sliding window optimized'
    if not s:
        return 0

    str_length = len(s)
    longest_substr = i = 0
    map = {}

    for j in range(str_length):
        if map.get(s[j]):
            i = max(map.get(s[j]), i)
        longest_substr = max(longest_substr, j - i + 1)
        map[s[j]] = j + 1

    return longest_substr
