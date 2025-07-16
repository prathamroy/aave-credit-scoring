import pandas as pd

def generate_features(df):
    df['wallet'] = df['userWallet']
    df['action_type'] = df['action']
    df['amount'] = df['actionData'].apply(lambda x: float(x.get('amount', 0)))
    df['price_usd'] = df['actionData'].apply(lambda x: float(x.get('assetPriceUSD', 1)))
    df['amount_usd'] = df['amount'] * df['price_usd']

    # Drop NaNs
    df = df.dropna(subset=['wallet', 'amount_usd', 'action_type'])

    agg_df = df.groupby('wallet').agg(
        total_txns=('action_type', 'count'),
        total_amount_usd=('amount_usd', 'sum'),
        unique_actions=('action_type', pd.Series.nunique),
        avg_amount_usd=('amount_usd', 'mean'),
        max_amount_usd=('amount_usd', 'max')
    ).reset_index()

    return agg_df