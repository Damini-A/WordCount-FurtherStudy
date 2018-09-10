# put your code here.
test_file = open("test.txt")



word_count = {}

for line in test_file:
    words = line.split()

    for word in words:
        word = word.lower().rstrip(",:.?")

        word_count[word] = word_count.get(word, 0) + 1



for word in word_count.items():
    print(f"{word[0]} {word[1]}")

