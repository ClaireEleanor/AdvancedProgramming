

def ispalindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return ispalindrome(word[1:-1])

def ispalindrome1(word):
    return word == word[::-1]
