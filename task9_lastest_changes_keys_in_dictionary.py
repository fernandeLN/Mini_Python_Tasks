"""
OOP Basics
Implement a custom dictionary that will memorize the 5 latest changed keys.
Using method "get_history" return these keys.

Example:
```python
>> d = HistoryDict({"foo": 42})
>> d.set_value("bar", 43)
>> d.get_history()

["bar"]
```
"""
class HistoryDict:
    def __init__(self, init_dict=None):
        self.data = dict(init_dict) if init_dict else {}
        self.history = []

    def set_value(self, key, value):
        self.data[key] = value

        if key in self.history:
            self.history.remove(key)

        self.history.append(key)

        if len(self.history) > 5:
            self.history.pop(0)

    def get_history(self):
        return self.history

if __name__ == "__main__":
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    d.set_value("bar1", 44)
    d.set_value("bar", 44)

    print(d.get_history())

# # version with deque
#
# from collections import deque
#
# class HistoryDict:
#     def __init__(self, initial=None):
#         self.data = dict(initial) if initial else {}
#         self.history = deque(maxlen=5)
#
#     def set_value(self, key, value):
#         self.data[key] = value
#
#         # If key already exists in history, remove it first
#         if key in self.history:
#             self.history.remove(key)
#
#         self.history.append(key)
#
#     def get_history(self):
#         return list(self.history)
#
# if __name__ == "__main__":
#     d = HistoryDict({"foo": 42})
#     d.set_value("bar", 43)
#     d.set_value("bar1", 44)
#     d.set_value("bar", 44)
#
#     print(d.get_history())