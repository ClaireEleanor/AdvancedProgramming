

def ispalindrome(word):
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        return ispalindrome(word[1:-1])
    else:
        return False

def ispalindrome1(word):
    return word == word[::-1]
