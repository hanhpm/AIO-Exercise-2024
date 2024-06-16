def character_count(word):
    character_statistic = {}
    # Your code is here
    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1

    return character_statistic

# Test the function
# assert character_count("Baby") == {"’B’": 1, "a": 1, "b": 1, "y": 1}
print(character_count("smiles"))
print(character_count("antidisestablishmentarianism"))
