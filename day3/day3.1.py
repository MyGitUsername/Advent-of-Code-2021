f = open('input.txt', 'r')

num_lines = sum(1 for line in open('input.txt'))

bitPositionCounter = list()
# Record the number of 1s at each position
for line in f:
    for i in range(len(line)):
        c = line[i]
        if c == '\n':
            continue
        if len(bitPositionCounter) == i:
            bitPositionCounter.insert(i, 0)
        if len(bitPositionCounter) > i and c == '1':
            bitPositionCounter[i] += 1 

gamma_rate_binary = '0b';
mask = '0b111111111111'
for numOf1s in bitPositionCounter:
    if numOf1s > int(num_lines / 2):
        gamma_rate_binary += '1'
    else:
        gamma_rate_binary += '0'
gamma_rate_decimal = int(gamma_rate_binary, 2)
epsilon_rate = int(mask, 2) ^ gamma_rate_decimal
power_consumption = epsilon_rate * gamma_rate_decimal

print('gamma_rate_binary' + gamma_rate_binary);
print('epsilon_rate_binary' + bin(epsilon_rate));
print (bitPositionCounter);
print(power_consumption)
