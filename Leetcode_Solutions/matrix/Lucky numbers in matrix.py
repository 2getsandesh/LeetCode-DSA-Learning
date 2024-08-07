'''Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        rowmin = [min(r) for r in matrix]
        colmax = [max(c) for c in zip(*matrix)]

        return list(set(rowmin) & set(colmax))
            
        
