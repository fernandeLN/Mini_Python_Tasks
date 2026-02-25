"""
Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
```python
>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>> split_by_index("no luck", [42])
["no luck"]
```
"""
from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Add your code here or call it from here   
    """
    results = []
    current_index = 0
    if not s :
        return []
    elif s and not indexes:
        results.append(s)
        return results
    else:
        for i in indexes:
            if i <= current_index or i<0 or i >= len(s):
                continue

            current_string = s[current_index:i]
            current_index = i
            results.append(current_string)
        results.append(s[current_index:])
        return results

if __name__ == '__main__':
    assert split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == ["python", "is", "cool", ",", "isn't", "it?"]
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))

    print (split_by_index("no luck", [42]))
