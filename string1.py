inputString = 'aabccddd' #row_input()
print(len(inputString))

i=0
while len(inputString) >= 1:

        if (inputString[i] == inputString[i+1]):
            inputString_ = inputString[:i] + inputString[i+1:]
            inputString_ = inputString_[:i] + inputString_[i+1:]
            inputString = inputString_
            print(inputString_ , inputString, i, len(inputString))
        else:
            print(inputString)
            i = i+1
