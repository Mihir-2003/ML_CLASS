import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_gradient_logistic(X, y, w, b): 
    m, n = X.shape
    dj_dw = np.zeros(n)      
    dj_db = 0.0

    for i in range(m):
        f_wb_i = sigmoid(np.dot(X[i], w) + b)         
        err_i = f_wb_i - y[i]             
        for j in range(n):
            dj_dw[j] += err_i * X[i, j] 
        dj_db += err_i

    dj_dw = dj_dw / m                     
    dj_db = dj_db / m
    return dj_db, dj_dw  

def predict_prob(X, w, b):
    z = np.dot(X, w) + b
    return sigmoid(z)

def predict_class(X, w, b, threshold=0.5):
    if predict_prob(X,w,b)>=0.5:
        return 1
    else : 
        return 0

def train_logistic_regression(X, y, alpha=0.1, iterations=1000):
    m, n = X.shape
    w = np.zeros(n)
    b = 0.0

    for i in range(iterations):
        dj_db, dj_dw = compute_gradient_logistic(X, y, w, b)

        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        if i % 100 == 0:
            cost = -np.mean(y*np.log(predict_prob(X,w,b)+1e-15) + 
                            (1-y)*np.log(1-predict_prob(X,w,b)+1e-15))
            print(f"Iteration {i}: Cost {cost:.4f}")

    return w, b

def main():
    X = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
    y = np.array([0, 0, 0, 1, 1, 1])

    # Train model
    w, b = train_logistic_regression(X, y, alpha=0.1, iterations=1000)

    print("\nTrained parameters:")
    print("w =", w)
    print("b =", b)

    X_new = np.array([1.5, 2])
    prob = predict_prob(X_new, w, b)
    cls = predict_class(X_new, w, b)

    print("\nPrediction for X_new:", X_new)
    print("Probability:", prob)
    print("Class:", cls)

main()
