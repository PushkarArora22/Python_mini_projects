def main():
    a=input("Enter a sentence")
    print(f"Total Characters: {count_characters(a)}")
    print(f"Total Words: {count_words(a)}")
    print(f"Uppercase: {upper_case(a)}")
    print(f"Lowercase: {lower_case(a)}")
    print(f"Reversed: {reverse_txt(a)}")
    print(f"Vowel Count: {vowel_count(a)}")
    print(f"Space Count: {space_count(a)}")

def count_characters(sen):
    return len(sen)


def count_words(sen):
    return len(sen.split())


def upper_case(sen):
    return sen.upper()


def lower_case(sen):
    return sen.lower()


def reverse_txt(sen):
    return sen[::-1]


def vowel_count(sen):
    sen=sen.lower()
    b=sen.count("a")
    c=sen.count("e")
    d=sen.count("i")
    e=sen.count("o")
    f=sen.count("u")
    return b+c+d+e+f


def space_count(sen):
    return sen.count(" ")


main()