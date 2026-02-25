"""
Write a program which makes a pretty print of a part of the multiplication table.
Example:

Input:
row_start = 2
row_end = 4
column_start = 3
column_end = 7

Output: [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
that is equal to the following multiplication table:

    3   4   5   6   7
2   6   8   10  12  14
3   9   12  15  18  21
4   12  16  20  24  28"""
from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """
    products_list = []
    for i in range(row_start, row_end+1):
        product_by_row = []
        for j in range(column_start, column_end+1):
            product_by_row.append(i*j)
        products_list.append(product_by_row)
    return products_list

if __name__ == "__main__":
    row_start1 = 2
    row_end1 = 4
    column_start1 = 3
    column_end1 = 7
    assert check(row_start1, row_end1, column_start1, column_end1) == [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
    print(check(row_start1, row_end1, column_start1, column_end1))
