import numpy as np
from sklearn.metrics import mean_absolute_error

def bootstrap_metric(y_true, y_pred, metric=mean_absolute_error, n=500, random_seed=42):
    np.random.seed(random_seed)
    scores = []
    idx = np.arange(len(y_true))
    for _ in range(n):
        sample = np.random.choice(idx, size=len(y_true), replace=True)
        scores.append(metric(y_true[sample], y_pred[sample]))
    ci_low, ci_high = np.percentile(scores, [2.5, 97.5])
    return scores, ci_low, ci_high
