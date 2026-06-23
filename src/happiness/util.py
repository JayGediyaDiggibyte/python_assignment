
def calculate_happiness(arr, liked, disliked):
    happiness = 0
    for num in arr:
        if num in liked:
            happiness += 1
        elif num in disliked:
            happiness -= 1
    return happiness