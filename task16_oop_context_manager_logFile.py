"""
***
Create a context manager `LogFile` inherited from `ContextDecorator`
which adds text lines into a log file.
Every text line must contain the following information:
- date and time when started (`Start:`)
- execution time (`Run:`)
- error information (in the code wrapped by context manager) (`An error occured:`)
>The trace format example when no errors occurred:
```python
Start: 2021-03-22 12:38:24.757637 | Run: 0:00:00.000054 | An error occurred: None
```
> The example in case of `ZeroDivisionError` exception
```python
Start: 2021-03-22 12:38:24.758463 | Run: 0:00:00.000024 | An error occurred: division by zero
```

The log file name is passed as an argument to text manager constructor.
For example:
```python
@LogFile('my_trace.log')
def some_func():
    ...
```
The log file has to be open in `append` mode to allow reopening existing file and adding
new information into this file if the same name is pointed.

When an exception is happened the error message has to be put in `An error occured:` into the log and reraised upper.

Use `open` builtin function to open the log file.
"""

from contextlib import ContextDecorator
from datetime import datetime
import os

class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.now()
        duration = end_time - self.start_time

        # The error message should be in exc_val
        error_message = str(exc_val) if exc_val else None

        log_result = (
            f"Start: {self.start_time} | "
            f"Run: {duration} | "
            f"An error occurred: {error_message}\n"
        )

        with open(self.filename, "a") as f:
            f.write(log_result)

        return False


if __name__ == "__main__":
    log_file = "test_log.txt"

    if os.path.exists(log_file):
        os.remove(log_file)

    @LogFile(log_file)
    def log_function():
        return "Hello World!"
    result = log_function()
    print(result)


    @LogFile(log_file)
    def log_function():
        return 1/0
    result = log_function()
    print(result)