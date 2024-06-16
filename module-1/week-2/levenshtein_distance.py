def levenshtein_distance(token1, token2):
    len1, len2 = len(token1), len(token2)
    distance_matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        distance_matrix[i][0] = i
    for j in range(len2 + 1):
        distance_matrix[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1
            distance_matrix[i][j] = min(
                distance_matrix[i - 1][j] + 1,       # Deletion
                distance_matrix[i][j - 1] + 1,       # Insertion
                distance_matrix[i - 1][j - 1] + cost  # Substitution
            )

            '''
            # Print the matrix after each update
            print(f"Updated matrix after setting distance_matrix[{i}][{j}] (token1[{i - 1}] vs token2[{j - 1}]):")
            for row in distance_matrix:
                print(row)
            print()
            '''

    distance = distance_matrix[len1][len2]
    return distance


# Test the function
# assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))
print(levenshtein_distance("favoritos", "favourite"))
print(levenshtein_distance("hi", "hello"))
