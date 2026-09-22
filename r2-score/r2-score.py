import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    sum, count, numerator, denominator = np.zeros(4)
    for i in y_true:
        sum += i 
        count += 1
    mean_target = sum/count 
    print(sum," ", count)
    for a,b in zip(y_pred, y_true):
         numerator += (a-b)**2
         denominator += (b-mean_target)**2

    
    if numerator == 0 and denominator == 0: 
        return float(1)
    elif denominator == 0:
        return float(0)
    else: 
        return float(1 - numerator/denominator)
    pass