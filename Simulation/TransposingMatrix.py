from typing import List


class TransposeMatrix:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed_matrix = [list(row) for row in zip(*matrix)]
        return transposed_matrix


if __name__ == '__main__':
    obj = TransposeMatrix()
    matrix = [[1, 2],
              [3, 4]]
    print(obj.transpose(matrix))
    # X=[[1,2,3],[4,5,6]]
    # print(list(zip(*X)))
