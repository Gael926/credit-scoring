from sklearn.metrics import roc_auc_score, recall_score, confusion_matrix, precision_score, f1_score, accuracy_score
import numpy as np

# fonction de calcul de l'auc
def calculate_auc(y_true, y_pred_proba):
    try:
        return roc_auc_score(y_true, y_pred_proba)
    except ValueError:
        return np.nan 

# focntion de calcul du rappel
def calculate_recall(y_true, y_pred):
    return recall_score(y_true, y_pred)

# focntion de calcul de la precision
def calculate_precision(y_true, y_pred):
    return precision_score(y_true, y_pred)

# focntion de calcul du F1
def calculate_f1(y_true, y_pred):
    return f1_score(y_true, y_pred)

# focntion de calcul de l'accuracy
def calculate_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

# focntion de calcul du cout métier 10 * FN + 1 * FP
def business_cost_metric(y_true, y_pred_proba, threshold=0.5):
    y_pred = (y_pred_proba > threshold).astype(int)
    
    if len(y_true) == 0:
        return np.nan
        
    try:
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    except ValueError:
        return np.nan

    cost = 10 * fn + 1 * fp
    return cost