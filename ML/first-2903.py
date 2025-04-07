import numpy as np
import matplotlib.pyplot as plt

plt.ioff()

N = 1000
x = np.linspace(0, 1, N)
z = 20 * np.sin(2 * np.pi * 3 * x) + 100 * np.exp(x)
error = 10 * np.random.randn(N)
t = z + error


def create_matrix(x, M):
    X = np.ones((len(x), M + 1))
    for i in range(1, M + 1):
        X[:, i] = x ** i
    return X


def polynomial_regression(t, X):
    XTX = X.T @ X
    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv @ X.T @ t
    return w


def error(t, Y):
    return (t - Y) ** 2


def predict(w, X):
    return X @ w


M_values = [1, 8, 100]
plt.figure(figsize=(20, 5))

for i, M in enumerate(M_values):
    X = create_matrix(x, M)
    w = polynomial_regression(t, X)
    y = predict(w, X)

    plt.subplot(1, 3, i + 1)
    plt.plot(x, z, color=(0, 1, 0, 1), label='Функция z(x)')
    plt.scatter(x, t, s=1, label='Данные + шум t(x)')
    plt.plot(x, y, color=(1, 0, 0, 1), label=f'Регрессия (M={M})')
    plt.title(f'Полиномиальная регрессия (M={M})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

plt.show()


errors = []
for i in range(1, 101):
    X = create_matrix(x, i)
    w = polynomial_regression(t, X)
    y = predict(w, X)
    errors.append(sum(error(t, y)))

plt.plot([i for i in range(1, 101)], errors)
plt.show()