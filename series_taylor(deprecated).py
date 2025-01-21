import math
import numpy as np
import matplotlib.pyplot as plt

# FUNCIONES SERIES DE TAYLOR
MIN_ERROR = 0.005
MAX_TERMS = 85

def taylor_approx(x, function, a):
    ''' funcion que aproxima el número de términos requeridos para construir un polinomio de Taylor, calculando el número de terminos requeridos para aproximarnos a un valor de e que menor que MIN_ERROR '''
    for i in range(1, MAX_TERMS + 1):

        if(function == 'exp'):
            approx = func_exp(x, i)
            actual = math.exp(x)

        elif(function == 'cos'):
            approx = func_cos(x, i)
            actual = np.cos(x)

        elif(function == 'binom'):
            approx = func_binom(x, a, i)
            actual = (1 + x) ** a

        elif(function == 'ln'):
            approx = func_ln(x, a, i)
            actual = np.log(x)

        error = abs(approx - actual)
        if error < MIN_ERROR or i == MAX_TERMS:
            terms = i
            break

    return terms, approx, actual, error

# Funciones aproximadas

def func_exp(x, n):
    ''' funciones exponenciales aproximadas en la forma e elevado a x '''
    exp_approx = 0;
    for i in range(n):
        num = x**i / math.factorial(i)
        exp_approx += num

    return exp_approx

def func_cos(x, n):
    ''' funcion cos() aproximada '''
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )
    
    return cos_approx

def func_binom(x, a, n):
    ''' funciones binomiales aproximadas en la forma (1 + x) elevado a "a" '''
    binom_approx = 0
    for i in range(n):
        coef = math.comb(a, i)
        num = x**i
        binom_approx += coef * num

    return binom_approx

def func_ln(x, a, n):
    ''' ln(x) aproximada para 0 < x < 2a '''
    ln_approx = np.log(x)
    for i in range(1, n):
        num = ((x - a)**n) / (n*(a**n))
        ln_approx += num

    return ln_approx

def main():
    function = 'ln'
    step = 0.5
    x_bounds = {
        'low': -10,
        'high': 100
    }
    y_bounds = {
        'low': -10,
        'high': 100
    }
    a = 10

    # se definen los parámetros de entrada / salida
    x = np.arange(x_bounds['low'], x_bounds['high'], step, dtype=np.float64)
    y = np.copy(x)
    y_hat = np.copy(x)

    i = 0
    for index in x:
        terms, approx, actual, error = taylor_approx(index, function, a)
        y[i] = actual
        y_hat[i] = approx
        i += 1
        print(f'{terms} terminos: Serie Taylor approx= {approx}, exp calc= {actual}, error = {error}')

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x, y_hat)
    ax.legend([str(function) + '() function','Serie Taylor - ' + str(terms) + ' terms'])
    plt.xlim([x_bounds['low'], x_bounds['high']])
    plt.ylim([y_bounds['low'], y_bounds['high']])

    plt.show()

if __name__ == "__main__":
    main()
