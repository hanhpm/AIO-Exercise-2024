import math
import random

def mae(predict, target):
    return abs(predict - target)

def mse(predict, target):
    return (predict - target) ** 2

def rmse(predict, target):
    return math.sqrt(mse(predict, target))

def main():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return

    num_samples = int(num_samples)
    loss_name = input("Input loss name: ")

    losses = []
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        
        if loss_name == "MAE":
            loss = mae(predict, target)
        elif loss_name == "MSE":
            loss = mse(predict, target)
        elif loss_name == "RMSE":
            loss = rmse(predict, target)
        else:
            print("Invalid loss name")
            return
        
        print(f"loss name : {loss_name}, sample : {i}, pred : {predict}, target : {target}, loss : {loss}")
        losses.append(loss)
    
    if loss_name == "RMSE":
        final_loss = math.sqrt(sum(losses) / num_samples)
    else:
        final_loss = sum(losses) / num_samples
    
    print(f"final {loss_name} : {final_loss}")

main()
