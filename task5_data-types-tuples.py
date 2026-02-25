"""
Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements. The pairs should be formed as in the example. If there is only one element in the list, return [] instead.

Example:

get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]
get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
get_pairs([1])
[]
"""
from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # TODO: Add your code here
    if len(lst) == 1:
        return []
    list_tuples = []
    for i in range(len(lst)-1):
        list_tuples.append((lst[i], lst[i+1]))
    return list_tuples


if __name__ == "__main__":
    data = [1, 2, 3, 8, 9]
    assert get_pairs([1, 2, 3, 8, 9]) == [(1, 2), (2, 3), (3, 8), (8, 9)]
    print(get_pairs([1, 2, 3, 8, 9]))

    data1 = [1]
    assert get_pairs(data1) == []
    print(get_pairs(data1))

    data2 = ['need', 'to', 'sleep', 'more']
    assert get_pairs(data2) == [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
    print(get_pairs(data2))