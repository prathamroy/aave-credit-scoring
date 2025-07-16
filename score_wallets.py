import json
import pandas as pd
from utils.feature_engineering import generate_features
from utils.scoring import assign_credit_scores

def main():
    input_path = 'data/user-wallet-transactions.json'
    output_path = 'wallet_scores.csv'
    with open(input_path, 'r') as f:
        raw_data = json.load(f)
    df = pd.DataFrame(raw_data)

    feature_df = generate_features(df)
    scored_df = assign_credit_scores(feature_df)
    scored_df.to_csv(output_path, index=False)
    print(f"Wallet scores have been saved to {output_path}")

if __name__ == "__main__":
    main()