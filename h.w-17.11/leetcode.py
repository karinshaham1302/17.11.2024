# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


def length_of_last_word(s: str) -> int:
    s = s.strip()
    words = s.split(' ')
    return len(words[-1]) if words else 0


s = 'Hello World'
print(length_of_last_word(s))

s = 'fly me to the moon'
print(length_of_last_word(s))

s = 'luffy is still joyboy'
print(length_of_last_word(s))
