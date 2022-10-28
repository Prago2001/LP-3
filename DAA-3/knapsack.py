def knapsack(values,weights,capacity):
    dp = [[0 for i in range(capacity+1)] for j in range(len(values)+1)]

    for item in range(1,len(values) + 1):
        for weight in range(1,capacity + 1):
            if weights[item - 1] <= weight:
                dp[item][weight] = max(dp[item-1][weight-weights[item-1]]+values[item-1],dp[item-1][weight])
            else:
                dp[item][weight] = dp[item-1][weight]
    return dp[-1][-1]


while True:
    print("Press Ctrl+C to terminate...")
    n = int(input('Enter number of items: '))
    values = [int(i) for i in input("Enter values of items:").split(" ")]
    weights = [int(i) for i in input("Enter weights of items:").split(" ")]
    capacity = int(input("Enter maximum weight: "))
    maximum_value = knapsack(values,weights,capacity)
    print('The maximum value of items that can be carried:', maximum_value)
