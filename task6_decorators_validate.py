"""
Create decorator`validate`, which validates arguments in the`set_pixel function.
All function parameters should be between 0(int) and 256(int) inclusive.
If all parameters are valid, the set_pixel function should return a *"Pixel created!"* message.
Otherwise, it should return the *"Function call is not valid!"* message.
Use`functools.wraps` where necessary.
Don't forget about doc strings.

**Examples**
>> set_pixel(0, 127, 300)
Function call is not valid!
>> set_pixel(0,127,250)
Pixel created!
"""
from functools import wraps

def validate(fn):
    """
    Add corresponded arguments and implementation here. 
    """
    @wraps(fn) # preserve original function metadata; without this, name and docstring would be lost
    def wrapper(*args, **kwargs):
        """
        All arguments must be integers between 0 and 256 inclusive
        if any of iterable returns False
        Then invalidate the set_pixel function.
        """
        if not all( isinstance(arg, int) and 0<=arg<= 256 for arg in args):
                return "Function call is not valid!"
        return fn(*args, **kwargs)
    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"
if __name__ == "__main__":
    assert set_pixel(0, 127, 300) == "Function call is not valid!"
    print(set_pixel(0, 127, 300))
    assert set_pixel(0,127,250) == "Pixel created!"
    print(set_pixel(0,127,250))