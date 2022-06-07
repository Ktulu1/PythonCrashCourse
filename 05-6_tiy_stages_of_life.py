age = 101
stage_of_life = ['baby', 'toddler', 'kid', 'teenager', 'adult', 'elder']

if age < 2:
    stage = stage_of_life[0]
elif 2 == age < 4:
    stage = stage_of_life[1]
elif 4 == age < 13:
    stage = stage_of_life[2]
elif 13 == age < 20:
    stage = stage_of_life[3]
elif 20 == age < 65:
    stage = stage_of_life[4]
else:
    stage = stage_of_life[5]

print(f"\nYou are in the {stage} stage of life.\n")