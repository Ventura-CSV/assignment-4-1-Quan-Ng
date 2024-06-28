def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')

    """
    ########################################
    Code Your Program here
    ########################################
    """
def main():
    def find_consecutive_letters(start, end):
        result = []
        
        # Check if start and end are alphabets
        if not (start.isalpha() and end.isalpha()):
            print("Input Error")
            return result
        
        # Convert start and end to lowercase (assuming case insensitivity)
        start = start.lower()
        end = end.lower()
        
        # Check if start and end are within 'a' to 'z'
        if not ('a' <= start <= 'z' and 'a' <= end <= 'z'):
            print("Input Error")
            return result
        
        # Generate consecutive letters from start to end
        for char_code in range(ord(start), ord(end) + 1):
            result.append(chr(char_code))
        
        return result

    while True:
        start = input("Enter the start letter (a-z): ")
        end = input("Enter the end letter (a-z): ")
        
        # Ensure start is less than end
        if start >= end:
            print("Input Error")
            continue
        
        # Validate and find consecutive letters
        result = find_consecutive_letters(start, end)
        
        if result:
            break  # If result is non-empty, break the loop and proceed to print
    
    # Print the result
    print(" ".join(result))



    ########################################
    # Do not delete the return statement
    ########################################



    return result

if __name__ == '__main__':
    main()

