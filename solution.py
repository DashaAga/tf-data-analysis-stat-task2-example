import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return x.mean() + 35 * norm.ppf(alpha / 2) / np.sqrt(len(x)), \
           x.mean() + 35 * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))
