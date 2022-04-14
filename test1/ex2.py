# Python3 program to find duplicate
# parenthesis in a balanced expression

# Function to find duplicate parenthesis
# in a balanced expression
def findDuplicateparenthesis(string):
    # create a stack of characters
    Stack = []

    # Iterate through the given expression
    for ch in string:

        # if current character is
        # close parenthesis ')'
        if ch == ')':

            # pop character from the stack
            top = Stack.pop()

            # stores the number of characters between
            # a closing and opening parenthesis
            # if this count is less than or equal to 1
            # then the brackets are redundant else not
            elementsInside = 0
            while top != '(':
                elementsInside += 1
                top = Stack.pop()

            if elementsInside < 1:
                return True

        # push open parenthesis '(', operators
        # and operands to stack
        else:
            Stack.append(ch)

    # No duplicates found
    return False


# Driver Code
if __name__ == "__main__":

    # input balanced expression
    string = "(((1+2))+ 3)"

    if findDuplicateparenthesis(string) == True:
        print("Duplicate Found")
    else:
        print("No Duplicates Found")

# This code is contributed by Rituraj Jain
