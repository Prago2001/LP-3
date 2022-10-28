from numpy import maximum


def fractional_knapsack(values,weights,capacity):
    value_weight_pairs = list(zip(values,weights,list(range(len(values)))))

    value_weight_pairs.sort(key=lambda x : x[0]/x[1],reverse=True)

    maximum_value = 0

    quantities = [0] * len(value_weight_pairs)

    for value,weight,index in value_weight_pairs:
        if weight <= capacity:
            maximum_value += value
            quantities[index] = 1
            capacity -= weight
        else:
            maximum_value += (value / weight) * capacity
            quantities[index] = capacity/weight
            break
    
    return maximum_value,quantities


while True:
    print("Press Ctrl+C to terminate...")
    n = int(input('Enter number of items: '))
    values = [int(i) for i in input("Enter values of items").split(" ")]
    weights = [int(i) for i in input("Enter weights of items").split(" ")]
    capacity = int(input("Enter maximum weight: "))
    maximum_value, quantities = fractional_knapsack(values,weights,capacity)
    print('The maximum value of items that can be carried:', maximum_value)
    print('The fractions in which the items should be taken:', quantities)

