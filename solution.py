import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    sqrt = 0
    for i in np.nditer(x):
      sqrt = sqrt + (i - x.mean())**2
    alpha = 1 - p
    return x.mean() + scipy.stats.t.ppf(alpha/2, len(x)-1)*(sqrt/len(x))**0.5/(len(x))**0.5, \
           x.mean() - scipy.stats.t.ppf(alpha/2, len(x)-1)*(sqrt/len(x))**0.5/(len(x))**0.5
