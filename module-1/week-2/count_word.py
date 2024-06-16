def count_word(file_path):
    counter = {}
    # Your code is here
    with open(file_path, 'r') as file:
        text = file.read()

    words = text.split()

    for word in words:
        word = word.lower()
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

# Test the function
file_path = "Module2/count_word_test.txt"
result = count_word(file_path)
assert result["who"] == 3
print(result["man"])
