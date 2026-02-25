"""
Implement a function that works the same as `str.split` method
(without using `str.split` itself, ofcourse).
Pay attention to strings with multiple spaces. For example: '    Hi     Python    world!' 

Example:
```python
    def split(data: str, sep=None, maxsplit=-1):
        ...
"""

from typing import List

def split(data: str, sep=None, maxsplit=-1):
    """
    Add your code here or call it from here
    """
    if sep is None:
        # Handle maxsplit == 0
        if maxsplit == 0:
            i = 0
            while i < len(data) and data[i].isspace():
                i += 1
            if i < len(data):
                return [data[i:]]
            else:
                return []

        results = []
        current = ""
        splits = 0
        i = 0

        while i < len(data):
            char = data[i]

            if char.isspace():
                if current:
                    results.append(current)
                    current = ""
                    splits += 1

                    if maxsplit != -1 and splits >= maxsplit:
                        i += 1
                        while i < len(data) and data[i].isspace():
                            i += 1
                        if i < len(data):
                            results.append(data[i:])
                        return results
            else:
                current += char

            i += 1

        if current:
            results.append(current)

        return results

    else :
        if maxsplit == 0:
            return [data]

        results = []
        start = 0
        splits = 0
        sep_len = len(sep)
        i = 0

        while i <= len(data) - sep_len:
            if data[i:i + sep_len] == sep and (maxsplit == -1 or splits < maxsplit):
                results.append(data[start:i])
                start = i + sep_len
                i = start
                splits += 1
            else:
                i += 1

        results.append(data[start:])
        return results


if __name__ == '__main__':
    assert split('') == []
    print(split(''))
    assert split(',123,', sep=',') == ['', '123', '']
    print(split(',123,', sep=','))
    assert split('test') == ['test']
    print(split('test'))
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    print(split('Python    2     3', maxsplit=1))
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    print(split('    test     6    7', maxsplit=1))
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    print(split('    Hi     8    9', maxsplit=0))
    assert split('    set   3     4') == ['set', '3', '4']
    print(split('    set   3     4'))
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    print(split('set;:23', sep=';:', maxsplit=0))
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
    print(split('set;:;:23', sep=';:', maxsplit=2))