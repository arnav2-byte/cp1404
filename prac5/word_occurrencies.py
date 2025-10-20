"""
CP1404/CP5632 Practical
Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2
"""
def counting_word_occurrencies():
    text = input("Enter any text : ")
    text = text.lower()
    words = text.split()

    word_counting = {}

    for word in words:
        if word in word_counting:
            word_counting[word] += 1
        else:
            word_counting[word] = 1

    sorted_word_counting = dict(sorted(word_counting.items()))

    max_word_length = max(len(word) for word in sorted_word_counting)

    for word, count in sorted_word_counting.items():
        print(f"{word:{max_word_length}} : {count}")

if __name__ == "__main__":
    counting_word_occurrencies()