import numpy as np

def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))

def relu_func(x):
    return x * (x > 0)

def elu_func(x, alpha=1.0):
    return np.where(x >= 0, x, alpha * (np.exp(x) - 1))

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def main():
    x_input = input("Input x: ")
    
    if not is_number(x_input):
        print("x must be a number")
        return
    
    x = float(x_input)
    
    activation_func_input = input("Input activation function (sigmoid | relu | elu): ").lower()

    activation_functions = {
        'sigmoid': sigmoid_func,
        'relu': relu_func,
        'elu': elu_func
    }
    
    if activation_func_input in activation_functions:
        result = activation_functions[activation_func_input](x)
        print(f"{activation_func_input} : f({x}) = {result}")
    else:
        print(f"{activation_func_input} is not supported")

main()
