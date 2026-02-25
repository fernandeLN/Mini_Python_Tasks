"""
#### Description

Implement class `Currency` and inherited classes `Euro`, `Dollar`, `Pound`.
Course is `1 EUR == 2 USD == 100 GBP`

You need to implement the following methods:

- `course` - classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for}

        >> print(
            f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
            f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
            f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
        )
        Euro.course(Pound)   ==> 100.0 GBP for 1 EUR
        Dollar.course(Pound) ==> 50.0 GBP for 1 USD
        Pound.course(Euro)   ==> 0.01 EUR for 1 GBP

- `to_currency` - method transforms currency from one currency to another. Method should return
instance of a required currency.

        >> e = Euro(100)
        >> r = Pound(100)
        >> d = Dollar(200)

        >> print(
            f"e = {e}\n"
            f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
            f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
            f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
        )
        e = 100 EUR
        e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
        e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
        e.to_currency(Euro)   = 100.0 EUR  # Euro instance printed

        >> print(
            f"r = {r}\n"
            f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
            f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
            f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
        )
        r = 100 GBP
        r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
        r.to_currency(Euro)   = 1.0 EUR  # Euro instance printed
        r.to_currency(Pound) = 100.0 GBP  # Pound instance printed

- `+` - returns an instance of a new value

        >> e = Euro(100)
        >> r = Pound(100)
        >> d = Dollar(200)
        >> print(
            f"e + r  =>  {e + r}\n"
            f"r + d  =>  {r + d}\n"
            f"d + e  =>  {d + e}\n"
        )
        e + r  =>  101.0 EUR  # Euro instance printed
        r + d  =>  10100.0 GBP  # Pound instance printed
        d + e  =>  400.0 USD  # Dollar instance printed

- other comparison methods: `> < ==`

Please pay attention on examples. Your code should work exactly the same.
"""
from __future__ import annotations

from locale import currency
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP


    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    rate_to_eur: float
    currency_code: str

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        # 1 EUR = 2 USD = 100 GBP
        """
        we can use EUR as the based currency
        and define rate conversion to eur for all currencies
        meaning for conversion we do:
        1 cls to EUR = 1 x cls.rate_to_eur
        and that amount to other_cls = 1cls_to_eur/other_cls.rate_to_eur
        """
        rate = cls.rate_to_eur / other_cls.rate_to_eur
        return f"{rate} {other_cls.currency_code} for 1 {cls.currency_code}"


    def to_currency(self, other_cls: Type[Currency]):
        """
        first we convert the value to euro
        then to the targeted currency which will be converted_value
        """
        value_in_eur = self.value * self.rate_to_eur
        converted_value = value_in_eur / other_cls.rate_to_eur
        return other_cls(converted_value)

    def __add__(self, other: Currency):
        other_to_self = other.to_currency(self.__class__)
        result = self.value + other_to_self.value
        return self.__class__(result)

    """
    For comparison, the values should be converted
    to the same currency base, so to EUR
    """

    def __eq__(self, other: Currency):
        return self.value * self.rate_to_eur == other.value * other.rate_to_eur

    def __lt__(self, other: Currency):
        return self.value * self.rate_to_eur < other.value * other.rate_to_eur

    def __gt__(self, other: Currency):
        return self.value * self.rate_to_eur > other.value * other.rate_to_eur


class Euro(Currency):
    rate_to_eur = 1
    currency_code = "EUR"

    def __init__(self, value: float):
        super().__init__(value)

    def __str__(self):
        return f"{self.value} {Euro.currency_code}"


class Dollar(Currency):
    rate_to_eur = 0.5
    currency_code = "USD"

    def __init__(self, value: float):
        super().__init__(value)

    def __str__(self):
        return f"{self.value} {Dollar.currency_code}"

class Pound(Currency):
    rate_to_eur = 0.01
    currency_code = "GBP"

    def __init__(self, value: float):
        super().__init__(value)

    def __str__(self):
        return f"{self.value} {Pound.currency_code}"

if __name__ == "__main__":
    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)
    print(
        f"e = {e}\n"
        f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
        f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
        f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
    )

    print(
        f"r = {r}\n"
        f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
        f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
        f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
    )

    print(
        f"e + r  =>  {e + r}\n"
        f"r + d  =>  {r + d}\n"
        f"d + e  =>  {d + e}\n"
    )

    print(Euro(1) == Dollar(2))  # True
    print(Pound(100) == Euro(1))  # True

    print(Dollar(1) < Euro(1))  # True
    print(Euro(1) > Pound(50)) # True
