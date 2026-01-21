def stochastic_gradient_descent(B0, B1, A, X, Y, n, epochs=5):
    print("\n--- STOCHASTIC GRADIENT DESCENT ---")
    print(f"Initial -> B0={B0}, B1={B1}")

    for epoch in range(epochs):
        for i in range(n):
            Y_pred = B0 + B1 * X[i]
            error = Y_pred - Y[i]

            dB0 = error
            dB1 = error * X[i]

            B0 -= A * dB0
            B1 -= A * dB1

    print(f"Final -> B0={B0:.4f}, B1={B1:.4f}")
    return B0, B1


def batch_gradient_descent(X, Y, n, B0, B1, A, iterations=10):
    print("\n--- BATCH GRADIENT DESCENT ---")
    print(f"Initial -> B0={B0}, B1={B1}")

    for _ in range(iterations):
        Y_pred = [B0 + B1 * X[i] for i in range(n)]

        dB0 = 0
        dB1 = 0
        for i in range(n):
            error = Y_pred[i] - Y[i]
            dB0 += error
            dB1 += error * X[i]

        dB0 /= n
        dB1 /= n

        B0 -= A * dB0
        B1 -= A * dB1

    print(f"Final -> B0={B0:.4f}, B1={B1:.4f}")
    return B0, B1


def least_square(X, Y, n):
    print("\n--- LEAST SQUARE METHOD ---")
    

    x_mean = sum(X) / n
    y_mean = sum(Y) / n

    num = 0
    den = 0
    for i in range(n):
        num += (X[i] - x_mean) * (Y[i] - y_mean)
        den += (X[i] - x_mean) ** 2

    m = num / den
    b = y_mean - m * x_mean

    print(f"Final -> B0={b:.4f}, B1={m:.4f}")
    return b, m


def main():
    X = [1, 3, 4, 2, 5]
    Y = [3, 4, 5, 2, 1]
    n = len(X)

    B0 = 0.5
    B1 = 0.5
    A = 0.01

    print("\nLINEAR REGRESSION COMPARISON :")

    b0_f, b1_f = stochastic_gradient_descent(B0, B1, A, X, Y, n)
    b0_f, b1_f = batch_gradient_descent(X, Y, n, B0, B1, A)
    b0_f, b1_f = least_square(X, Y, n)

    print("\n FINAL COMPARISON :")
    print(f"SGD        -> B0={b0_f:.4f}, B1={b1_f:.4f}")
    print(f"Batch GD   -> B0={b0_f:.4f}, B1={b1_f:.4f}")
    print(f"Least Sq   -> B0={b0_f:.4f}, B1={b1_f:.4f}")


main()
