import random

def find_influencers(matrix):
    unsure, lions = set([]), set([])
    for index, person in enumerate(matrix[0]):
        # Initial pass to build sets
        lions.add(index)
        unsure.add(index)

    while len(unsure) > 0:
        # Loop until all have been explored
        current = random.sample(unsure, 1)[0]
        to_visit = filter(lambda x: x in lions, range(len((matrix[current]))))
        to_visit_values = [matrix[current][i] for i in to_visit]
        for index, value in zip(to_visit, to_visit_values):
            if value == True:
                lions.remove(index)
        unsure.remove(current)
    return lions if len(lions) > 0 else False

def find_influencer_brute(matrix):
    """
    Find if there is any sole influencer in a matrix.

    Time Complexity: O(n*m)
    """
    for row in matrix:
        index = 0
        sheep = False
        while not sheep and index < len(row):
            if row[index] == True:
                sheep = True
            index += 1
        if sheep == False:
            return True
    return False

if __name__ == "__main__":
    matrix = [[0, 0, 0, 0, True],
              [True, 0, 0, 0, 0],
              [0, True, 0, 0, 0],
              [True, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    print find_influencers(matrix)
