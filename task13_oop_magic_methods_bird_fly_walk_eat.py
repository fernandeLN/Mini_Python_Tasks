"""
Create a hierarchy out of birds.
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have a default value.
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add the same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.

Example:
```python
>> b = Bird("Any")
>> b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
>> p.fly()
AttributeError: 'Penguin' object has no attribute 'fly'
>> p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
>> str(c)
"Canary bird can walk and fly"
>> c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
>> str(s)
"Gull bird can walk, swim and fly"
>> s.eat()
"It eats mostly fish"
```
"""
class Bird:
    def __init__(self, name: str):
        self.name = name

    def fly(self):
        return f"{self.name} bird can fly"

    def walk(self):
        return f"{self.name} bird can walk"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class FlyingBird(Bird):
    def __init__(self, name: str, ration: str = "grains") :
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"

class NonFlyingBird:
    def __init__(self, name: str, ration: str = "fish") :
        self.name = name
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can swim and fly"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name: str) :
        super().__init__(name)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"



if __name__ == "__main__":
    # Bird class testing
    # b = Bird("Any")
    # print(b.walk())
    # print(b.fly())
    # print(str(b))

    # NonFlyingBird testing
    p = NonFlyingBird("Penguin", "grains")
    # print(p.swim())
    print(p.eat())
    # print(str(p))
    # print(p.fly())

    # FlyingBird testing
    # c = FlyingBird("Canary")
    # print(c.eat())
    # print(str(c))
    # print(c.fly())
    # print(c.walk())

    # SuperBird testing
    s = SuperBird("Gull")
    print(str(s))
    print(s.eat())
    print(s.swim())
    print(s.fly())
    print(s.walk())
