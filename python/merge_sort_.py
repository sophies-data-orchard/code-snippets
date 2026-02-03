# coding=utf-8


def merge_sort(array):
    tmp = [0 for _ in range(len(array))]
    merge_sort_helper(array, 0, len(array) - 1, tmp)


def merge_sort_helper(array, left, right, tmp):    # [left, right] sort btw these 2 index
    if left >= right:
        return

    mid = (left + right) // 2    # [left, mid]  [mid + 1, right] divide to 2 parts
    merge_sort_helper(array, left, mid, tmp) # recursion sort left
    merge_sort_helper(array, mid + 1, right, tmp) #recursion sort right
    merge(array, left, right, tmp)


def merge(array, left, right, tmp):   #merge lef and right
    n = right - left + 1

    mid = (left + right) // 2  # [left, mid], [mid + 1, right]
    i, j = left, mid + 1

    for k in range(n):
        if i <= mid and (j > right or array[i] <= array[j]):
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1

    for k in range(n):
        array[left + k] = tmp[k]


if __name__ == '__main__':
    array = [6, 4, 5, 7, 2, 4, 3, 4, 7, 8]
    merge_sort(array)

    for num in array:
        print(num, end=' ')
    print()
