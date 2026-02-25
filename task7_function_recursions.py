"""
Define a function seq_sum(sequence) which allows to count sum of elements. Elements of all nested sequences should be included.
Example:

def seq_sum(sequence):
    pass

sequence = [1,2,3,[4,5, (6,7)]]

>> print(seq_sum(sequence))
28
"""
from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    total = 0
    for i in sequence:
        if type(i) == int or type(i) == float:
            total += i
        else:
            total += seq_sum(i)
    return total


if __name__ == "__main__":
    sequence1 = [1, 2, 3, [4, 5, (6, 7)]]
    assert seq_sum(sequence1) == 28
    print(seq_sum(sequence1))

    sequence2 = [1, 0, 3, 5, -1, (4, 5, [6, 7])]
    assert seq_sum(sequence2) == 30
    print(seq_sum(sequence2))