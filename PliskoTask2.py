R = float(input('Input rating score of student '))
if R <0 or R >100:
    print('Error: invalid rating score')
elif R <= 59:
    print('Your rate is "Unsatisfactory"')
elif R <= 64:
    print('Your rate is "Marginal"')
elif R <= 74:
    print('Your rate is "Satisfactory"')
elif R <= 84:
    print('Your rate is "Good"')
elif R <= 94:
    print('Your rate is "Very good"')
else:
    print('Your rate is "Excellent"')