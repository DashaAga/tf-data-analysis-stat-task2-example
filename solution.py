import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    std = 0
    alpha = 1-p
    for i in x:
      std = std+(i - x.mean())**2
    std = (std / len(x))**0.5
    SE = std/(len(x)**0.5)
    s = (x.mean()-t.ppf(1-alpha/2, len(x)-1)*SE, x.mean()+t.ppf(1-alpha/2, len(x)-1)*SE)
    return s
