# Wallet Credit Scoring

This project assigns credit scores (0–1000) to wallets interacting with the Aave V2 protocol, using raw on-chain transaction data. It is designed to evaluate the reliability of DeFi users based on behavioral patterns.


## Project Structure

```
aave-credit-scoring/
├── data/
│   └── user-wallet-transactions.json     # Raw input data
├── utils/
│   ├── feature_engineering.py            # Feature extraction logic
│   └── scoring.py                        # Credit score logic
├── score_wallets.py                      # One-step pipeline script
├── wallet_scores.csv                     # Output: wallet + credit score
├── Figure_1.png                          # Score distribution chart
├── helper_analysis.py                    # Generates the distribution chart
├── analysis.md                           # Insights from score ranges
├── README.md                             # This file
└── requirements.txt                      # Dependencies
```

---

### Features Engineered:

Per wallet, the following metrics are calculated:

* `total_txns`: Number of transactions
* `total_amount_usd`: USD value of all actions
* `unique_actions`: Count of distinct action types
* `avg_amount_usd`: Mean transaction amount
* `max_amount_usd`: Largest single transaction

### Scoring Logic:

Each feature is ranked on a percentile basis across all wallets. A weighted score is computed as:

```
score_raw = 0.3 × total_txns_rank
          + 0.3 × total_amount_usd_rank
          + 0.2 × unique_actions_rank
          + 0.1 × avg_amount_usd_rank
          + 0.1 × max_amount_usd_rank
```

The final credit score is:

```python
credit_score = int(score_raw * 1000)
```

---

### Requirements

```
pip install -r requirements.txt
```

### Run the scoring script

```
python score_wallets.py
```

### Output

Generates:

* `wallet_scores.csv`: Contains each wallet address and its computed credit score

---

## Analysis

See [`analysis.md`](analysis.md)

## Future Possibilities

* Cluster wallets using unsupervised learning
* Add real-time scoring via API pipeline

---

Created by [Pratham Roy](https://github.com/prathamroy)
Inspired by risk modeling in DeFi

---