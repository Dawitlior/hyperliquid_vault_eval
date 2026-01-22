import requests
import pandas as pd
from pathlib import Path

# -----------------------------
# Config
# -----------------------------
PROTOCOL_SLUG = "hyperliquid"
OUTPUT_PATH = Path("data/raw/hyperliquid_fees.csv")

# -----------------------------
# Fetch Fees from DeFiLlama
# -----------------------------
url = f"https://api.llama.fi/summary/fees/{PROTOCOL_SLUG}"
response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to fetch fees data: {response.status_code}")

data = response.json()

# -----------------------------
# Extract daily fees
# -----------------------------
daily_fees = data.get("dailyFees", [])

if not daily_fees:
    raise Exception("No daily fees data found")

df = pd.DataFrame(daily_fees)
df["date"] = pd.to_datetime(df["date"], unit="s")
df = df.rename(columns={"totalFees": "fees_usd"})
df = df[["date", "fees_usd"]].sort_values("date")

# -----------------------------
# Save to CSV
# -----------------------------
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print(f"Fees data saved to {OUTPUT_PATH}")
print(df.tail())
