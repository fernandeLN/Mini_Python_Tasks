"""
Write a Python program to print all the unique values of all the dictionaries in a list.
Example:

Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    values_list = []
    for item in lst:
        for key, value in item.items():
            values_list.append(value)
    return set(values_list)

if __name__ == "__main__":
    list1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    assert check(list1) == {'S005', 'S002', 'S007', 'S001', 'S009'}
    print(check(list1))