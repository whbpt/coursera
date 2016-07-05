# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    price=list()
    for (a,b) in zip(values,weights):
        price.append(float(a)/float(b))
    for (a,b) in sorted(zip(price,weights),reverse=True):
        if capacity>b:
            value=value+b*a
            capacity=capacity-b
        else:
            value=value+capacity*a 
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
