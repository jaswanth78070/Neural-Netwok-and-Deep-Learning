# Student ID: 7700757807
#       CRN :23476
#Question 1A

Strng = list(input("Enter the string 'Python': "))

if len(Strng) >= 2:
    # deleting the first two characters
    del Strng[:2]
    # Reverse the resultant string
    reversed_string = Strng[::-1]
    print("Reversed String:", ''.join(reversed_string))

    

