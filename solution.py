import pandas as pd
import numpy as np


chat_id = 475225606 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.08
    p_val = stats.anderson_ksamp([x, y])[2]
    return p_val <= alpha
