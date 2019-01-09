def twosum_1(arr, sum):
    if not arr or len(arr) < 2 or sum is None:
        return []

    length = len(arr)

    for index_1 in range(length - 1):
        for index_2 in range(index_1 + 1, length):
            if arr[index_1] + arr[index_2] == sum:
                return [index_1, index_2]

    return []


def twosum_2(arr, sum):
    if not arr or len(arr) < 2 or sum is None:
        return []

    map = {}
    for i in range(len(arr)):
        complement = sum - arr[i]
        complement_index = map.get(complement)

        if complement_index is not None:
            return [complement_index, i]

        map[arr[i]] = i
