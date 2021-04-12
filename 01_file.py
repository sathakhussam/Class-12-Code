# One Way

num = int(input('Enter A Number Between 0-999 ? '))
if num < 0 :
    print('The Number You Have Entered Is Less Than 0')
elif num > 0 and num < 10 :
    print('The Number You Have Entered Is One Digit Number')
elif num > 9 and num < 100 :
    print('The Number You Have Entered Is Two Digit Number')
elif num > 99 and num < 1000 :
    print('The Number You Have Entered Is Three Digit Number')


# Another Way

num = int(input('Enter A Number Between 0-999 ? '))
if num < 0 :
    print('The Number You Have Entered Is Less Than 0')
elif num < 10 :
    print('The Number You Have Entered Is One Digit Number')
elif num < 100 :
    print('The Number You Have Entered Is Two Digit Number')
elif num < 1000 :
    print('The Number You Have Entered Is Three Digit Number')
