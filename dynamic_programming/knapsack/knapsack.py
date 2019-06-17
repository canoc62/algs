import sys

def main():
    with open("text/" + sys.argv[1]) as f:
        capacity, num_items = f.readline().split(" ")
        capacity = int(capacity)
        num_items = int(num_items)
        values = [0]
        weights = [0]

        for line in f:
            data = line.split(" ")
            values.append(int(data[0]))
            weights.append(int(data[1]))
   
    optimal_values = knapsack(capacity, num_items, values, weights)
    print(reconstruct(optimal_values, capacity, values, weights))

def knapsack(capacity, num_items, values, weights):
    optimal_values = []
    for _ in range(num_items + 1):
        optimal_values.append([])

    for c in range(capacity+1):
        optimal_values[0].append(0)

    for i in range(1, len(values)):
        for cap in range(capacity+1):
            if weights[i] > cap:
                optimal_values[i].append(optimal_values[i-1][cap])
            else:
                greater_val = max(optimal_values[i-1][cap], optimal_values[i-1][cap-weights[i]] + values[i])
                optimal_values[i].append(greater_val)
    print("optimal_value: " + str(optimal_values[len(optimal_values)-1][-1]))
    return optimal_values

def reconstruct(optimal_values, capacity, values, weights):
    items = []
    c = capacity

    for i in range(len(values)-1, -1, -1):
        # print("i: " + str(i))
        # print("c: " + str(c))
        # print("weights[i]: " + str(weights[i]))
        # print("optimal_values[i-1][c-weights[i]] + values[i]: " + str(optimal_values[i-1][c-weights[i]] + values[i]))
        # print("optimal_values[i-1][c]: " + str(optimal_values[i-1][c]))
        if weights[i] <= c and (optimal_values[i-1][c-weights[i]] + values[i]) >= optimal_values[i-1][c]:
            items.append(i)
            c -= weights[i]

    items.reverse()
    return items

if __name__ == '__main__':
    main()