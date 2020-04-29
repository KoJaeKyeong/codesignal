def checkPalindrome(inputString):
    if inputString[:]==inputString[::-1]:
        return True
    elif inputString[:]!=inputString[::-1]:
        return False
