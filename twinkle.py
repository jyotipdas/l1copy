s1 = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"

count = 1

for d in s1:
    if d == '.':
        print d + "\n",
        count = 1
    elif d == '!':
        print d + "\n\t\t",
    elif d == ',':
        if count == 3 :
            print d + "\n\t",
            count += 1
        elif count == 4:
            print d + "\n\t\t\t",
            count = 1
        else:
            print d,
            count += 1
    else:
        print d,
