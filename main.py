def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        words = list_of_words(file_contents)
        word_count = count_words(words)
        #print(count_words(words))
        letter_count = count_characters(file_contents)
        print(letter_count)
        print(str(word_count) +" words found in the document")

        for letter in letter_count:
            print("The " + letter + " character was found " + str(letter_count.get(letter)) + " times")

    print("--- End report ---")


def list_of_words(text):
    word_list = text.split()
    return word_list

def count_words(text):
    count = len(text)
    return count

def count_characters(book_text):
    lowered_book_text = book_text.lower()
    characters = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
    for letter in lowered_book_text:
        if letter.isalpha():
            characters[letter] += 1
    
    return characters




main()