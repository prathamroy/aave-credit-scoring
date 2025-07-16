import pandas as pd
import numpy as np

def assign_credit_scores(df):
    df = df.copy()
    
    # Score formula: weighted normalized rank
    df['score_raw'] = (
        df['total_txns'].rank(pct=True) * 0.3 +
        df['total_amount_usd'].rank(pct=True) * 0.3 +
        df['unique_actions'].rank(pct=True) * 0.2 +
        df['avg_amount_usd'].rank(pct=True) * 0.1 +
        df['max_amount_usd'].rank(pct=True) * 0.1
    )

    df['credit_score'] = (df['score_raw'] * 1000).astype(int).clip(0, 1000)
    return df[['wallet', 'credit_score']]