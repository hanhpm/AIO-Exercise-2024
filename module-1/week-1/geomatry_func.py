def approx_sin(x, n):
    sin_x = 0
    factorial = 1
    power_of_x = x
    for i in range(n):
        term = power_of_x / factorial
        sin_x += (-1) ** i * term
        power_of_x *= x ** 2
        factorial *= (2 * i + 2) * (2 * i + 3)
    return sin_x

def approx_cos(x, n):
    cos_x = 0
    factorial = 1
    power_of_x = 1
    for i in range(n):
        term = power_of_x / factorial
        cos_x += (-1) ** i * term
        power_of_x *= x ** 2
        factorial *= (2 * i + 1) * (2 * i + 2)
    return cos_x

def approx_sinh(x, n):
    sinh_x = 0
    factorial = 1
    power_of_x = x
    for i in range(n):
        term = power_of_x / factorial
        sinh_x += term
        power_of_x *= x ** 2
        factorial *= (2 * i + 2) * (2 * i + 3)
    return sinh_x

def approx_cosh(x, n):
    cosh_x = 0
    factorial = 1
    power_of_x = 1
    for i in range(n):
        term = power_of_x / factorial
        cosh_x += term
        power_of_x *= x ** 2
        factorial *= (2 * i + 1) * (2 * i + 2)
    return cosh_x

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    
result_sin = approx_sin(x=3.14, n=10)
result_cos = approx_cos(x=3.14, n=10)
result_sinh = approx_sinh(x=3.14, n=10)
result_cosh = approx_cosh(x=3.14, n=10)

print(f"approx_sin(3.14, 10) = {result_sin}")
print(f"approx_cos(3.14, 10) = {result_cos}")
print(f"approx_sinh(3.14, 10) = {result_sinh}")
print(f"approx_cosh(3.14, 10) = {result_cosh}")
