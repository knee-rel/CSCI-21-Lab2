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

while True:
    rows = int(input())
    if rows != -1:
        columns = 2 * rows - 1
        iter_a = 0
        while iter_a < rows:
            iter_b = 0
            s = ''
            while iter_b < columns:
                if((columns//2)-iter_a <= iter_b <= (columns//2)+iter_a):
                    s+='*'
                else:
                    s+= ' '
                iter_b+=1
            print(s)
            iter_a += 1
        iter_a = 1
        while iter_a < rows:
            iter_b = 0
            s=''
            while iter_b < columns:
                if (iter_a <= iter_b <= columns-1 -iter_a):
                    s+='*'
                else:
                    s+= ' '
                iter_b += 1
            print(s)
            iter_a+=1
    else:
        break





        
