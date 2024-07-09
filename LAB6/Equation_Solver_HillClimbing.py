def value(equation, x):
    ans = 0
    for i in equation.keys():
        ans += equation[i] * (x ** i)
    return ans

def hill_climbing(equation, source, l_range, h_range, max_iterations=1000, tolerance=1e-6):
    iterations = 0
    while iterations < max_iterations:
        if l_range < source < h_range:
            adList = [source - 1, source + 1]
        elif l_range == source:
            adList = [source + 1]
        else:
            adList = [source - 1]
        flag = True
        for i in adList:
            if value(equation, i) > value(equation, source):
                source = i
                flag = False
                break
        if flag:
            print(f'Maximum value = {value(equation, source)} at x = {source}')
            return
        iterations += 1
    print("Maximum iterations reached without convergence.")

if __name__ == '__main__':
    deg = int(input('Enter degree of equation: '))
    eq = {i: 0 for i in range(deg + 1)}
    for i in range(deg + 1):
        coeff = float(input(f'Enter coefficient of x^{i}: '))
        eq[i] = coeff
    src = float(input('Enter source: '))
    l = float(input('Enter lower range: '))
    h = float(input('Enter higher range: '))
    hill_climbing(eq, src, l, h)
