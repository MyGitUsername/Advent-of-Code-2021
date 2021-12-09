def count_bits(li, i):
    counter_1s = 0
    counter_0s = 0
    for bin in li:
        if bin[i] == '1':
            counter_1s += 1
        else:
            counter_0s += 1
    return counter_1s, counter_0s

# if 1 and 0s are equally common return 1
def bit_criteria_oxygen(li, i):
    num_of_1s, num_of_0s = count_bits(li, i)

    if num_of_1s  >= num_of_0s:
        return '1'
    else:
        return '0'

def bit_criteria_carbon(li, i):
    num_of_1s, num_of_0s = count_bits(li, i)

    if num_of_1s >= num_of_0s:
        return '0'
    else:
        return '1'



f = open('input.txt', 'r')
inputArr = list()
for line in f:
    new_line_char = len(line) - 1
    inputArr.append(line[:new_line_char])

filter_for_oxygen = list(inputArr)
filter_for_carbon = list(inputArr)
for i in range(12):
    x = bit_criteria_oxygen(filter_for_oxygen, i)
    y = bit_criteria_carbon(filter_for_carbon, i)
    if len(filter_for_oxygen) != 1:
        filter_for_oxygen = list(filter(lambda line: line[i] == x, filter_for_oxygen))
    if len(filter_for_carbon) != 1:
        filter_for_carbon = list(filter(lambda line: line[i] == y, filter_for_carbon))

oxygen_gen_rating = int(filter_for_oxygen[0], 2)
carbon_gen_rating = int(filter_for_carbon[0], 2)

print(f'filter_for_oxygen: {filter_for_oxygen}')
print(f'oxygen_gen_rating: {oxygen_gen_rating}\n')

print(f'filter_for_carbon: {filter_for_carbon}')
print(f'carbon_gen_rating: {carbon_gen_rating}\n')

print(f'result: {oxygen_gen_rating * carbon_gen_rating}')
