def text_alignment(number):
    c = 'H'

    #TOP
    for i in range(number):
        print((c*i).rjust(number - 1) + c + (c*i).ljust(number - 1))

    #First Pillar
    for i in range(number+1):
        print((c * number).center(number * 2) + (c * number).center(number * 6))

    #Middel Line
    for i in range((number + 1) // 2):
        print((c * number * 5).center(number * 6))

    #second Pillar
    for i in range(number+1):
        print((c * number).center(number * 2) + (c * number).center(number * 6))

    #Bottom
    for i in range(number):
        print(((c * (number - i - 1)).rjust(number) + c + (c * (number - i - 1)).ljust(number)).rjust(number * 6))