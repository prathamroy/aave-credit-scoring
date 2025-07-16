import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wallet_scores.csv")
df['score_bin'] = pd.cut(df['credit_score'], bins=range(0, 1100, 100))

# Plot
score_dist = df['score_bin'].value_counts().sort_index()
score_dist.plot(kind='bar', rot=45)
plt.title("Credit Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Wallets")
plt.tight_layout()
plt.show()