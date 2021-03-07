# Nirel Marie M. Ibarra
# 192468
# March 8, 2021

# I have not discussed the Python language code in my program
# with anyone other than my instructor or the teaching assistants
# assigned to this course

# I have not used Python language code obatained from another student
# or any other unauthorized source, either modified or unmodified

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website,
# that has clearly noted with a proper ciration in the comments
# of my program



for num in range(0, 100):
    grade = int(input())
    if 92 <= grade <= 100:
        print('A')

    elif 87 <= grade <= 91:
        print('B+')

    elif 83 <= grade <= 86:
        print('B')

    elif 79 <= grade <= 82:
        print('C+')

    elif 75 <= grade <= 78:
        print('C')

    elif 70 <= grade <= 74:
        print('D')
    
    elif grade == -1:
        break

    else:
        print('F')


