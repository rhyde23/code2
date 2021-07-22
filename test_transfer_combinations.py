import pickle


#Change these to include more later, just testing
rating_factors = list(reversed(list(range(50, 95))))
age_factors = list(reversed(list(range(16, 40))))
position_factors = [
    'GK', 
    'RWB', 
    'LWB', 
    'LB', 
    'RB', 
    'CB', 
    'CM', 
    'CDM', 
    'CAM',
    'CF', 
    'LM', 
    'LW',
    'RM', 
    'RW',
    'ST'
]

#transfer_combinations = {}

file_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\TransferCombinations.dat'
transfer_combinations = pickle.load(open(file_path, 'rb'))

def build_key(position_factor, rating_factor, age_factor) :
    return '|'.join([position_factor, str(rating_factor), str(age_factor)])

def find_middle_example(key) :
    position, rating, age = key.split('|')
    rating, age = int(rating), int(age)
    rating_higher, rating_same = build_key(position, rating+1, age), build_key(position, rating-1, age)
    age_higher, age_lower = build_key(position, rating, age+1), build_key(position, rating, age-1)
    if rating_higher in transfer_combinations and rating_lower in transfer_combinations :
        return rating_higher, rating_lower
    if age_higher in transfer_combinations and age_lower in transfer_combinations :
        return age_higher, age_lower

def get_middle_value(higher_value, lower_value) :
    return lower_value+int((higher_value-lower_value)/2)


succ = 0

for position_factor in position_factors :
    for rating_factor in rating_factors :
        for age_factor in age_factors :
            test = build_key(position_factor, rating_factor, age_factor)
            if test in transfer_combinations :
                print(test, 'IN', transfer_combinations[test])
            else :
                try :
                    higher, lower = find_middle_example(test)
                    transfer_combinations[test] = get_middle_value(transfer_combinations[higher], transfer_combinations[lower])
                    print(test, 'SUCCESSFUL', transfer_combinations[test], 'TOTAL SUCC: ', succ)
                    succ += 1
                except :
                    print('COULDNT FIND', test)

print(transfer_combinations)


"""
file_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\TransferCombinations.dat'
transfer_combinations = pickle.load(open(file_path, 'rb'))

for combo_key in transfer_combinations :
    print(combo_key, transfer_combinations[combo_key])
"""
