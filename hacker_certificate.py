def reverse_word_and_swap_case(sentence):
    new_sentence=""
    sentence=sentence.swapcase()
    sentence=sentence.split()
    sentence=sentence[::-1]
    print(sentence)
    for i in sentence:
        sentence+=i+" "
    return sentence
sentence="my name is ANDEBET TILAAHUN"
print(reverse_word_and_swap_case(sentence))