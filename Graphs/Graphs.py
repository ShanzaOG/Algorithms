# array = [[0, 1, 0, 0],
#          [1, 1, 1, 0],
#          [0, 1, 0, 0],
#          [0, 1, 0, 0]]


def island_perimeter(array):
    perimeter = 0
    for row in range(len(array)):
        for cell in range(len(array[row])):
            if array[row][cell] == 1:
                perimeter += 4  # Assume each cell has a perimeter of 4
                # Check neighboring cells
                if row > 0 and array[row - 1][cell] == 1:  # Check top neighbor
                    perimeter -= 1
                if row < len(array) - 1 and array[row + 1][cell] == 1:  # Check bottom neighbor
                    perimeter -= 1
                if cell > 0 and array[row][cell - 1] == 1:  # Check left neighbor
                    perimeter -= 1
                if cell < len(array[row]) - 1 and array[row][cell + 1] == 1:  # Check right neighbor
                    perimeter -= 1
    return perimeter


if __name__ == '__main__':
    # grid = [
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0],
    #     [0, 1, 1, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 0]
    # ]
    array = [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]]
    result = island_perimeter(array)

    print(result)