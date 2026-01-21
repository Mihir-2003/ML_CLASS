print("------------WHEN LINE PASS THROUGH ORIGIN -----------------")


def multi_linear_regression(X1,X2,Y,n):
    X1_mean = sum(X1)/n
    X2_mean = sum(X2)/n
    Y_mean = sum(Y)/n
    X1_sum = 0
    X2_sum = 0
    X1_X2 = 0

    X1_Y =0
    X2_Y =0
    for i in range(n):
        X1_sum = X1_sum+X1[i]**2
        X2_sum = X2_sum+X2[i]**2
        X1_X2 = X1_X2 + X1[i]*X2[i]
        X1_Y = X1_Y + X1[i]*Y[i]
        X2_Y = X2_Y + X2[i]*Y[i]
    

    print(X1_mean, X2_mean, Y_mean, X1_sum ,X2_sum ,X1_X2 ,X1_Y ,X2_Y)
    denominator = (X1_sum*X2_sum - (X1_X2)**2)
    B1 = (X2_sum*X1_Y - X1_X2*X2_Y)/denominator

    B2 = (X1_sum*X2_Y - X1_X2*X1_Y)/denominator

    B0 = Y_mean - B1*X1_mean- B2*X2_mean

    print(f"Gradient B1 : {B1}")
    print(f"Gradient B2 : {B2}")
    print(f"Bias B0 : {B0}")
    
    print(f"Final Regression Equation : y = {B0} + {B1}x1+{B2}x2")
    
    x1 = float(input("Enter the x1 : "))
    x2 = float(input("Enter the x2 : "))
    
    y = B0 + B1*x1+B2*x2

    print(f"Predicted Value of y at {x1} and {x2} is : {y:.4f}")

def main():
    n = int(input("Enter the no of terms : "))
    X1, X2, Y = [], [], []

    for i in range(n):
        X1.append(float(input(f"Enter X1{i+1}: ")))
        
        X2.append(float(input(f"Enter X2{i+1}: ")))
        
        Y.append(float(input(f"Enter Y{i+1}: ")))
        
    multi_linear_regression(X1,X2,Y,n)
main()