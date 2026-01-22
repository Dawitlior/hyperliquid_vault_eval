import requests
import pandas as pd
from pathlib import Path

PROTOCOL_SLUG = "hyperliquid"
OUTPUT_PATH = Path("data/raw/hyperliquid_tvl.csv")

url = f"https://api.llama.fi/protocol/{PROTOCOL_SLUG}"
response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code}")

data = response.json()

tvl_data = data.get("tvl", [])
if not tvl_data:
    raise Exception("No TVL data found")

df = pd.DataFrame(tvl_data)
df["date"] = pd.to_datetime(df["date"], unit="s")
df = df.rename(columns={"totalLiquidityUSD": "tvl_usd"})
df = df[["date", "tvl_usd"]].sort_values("date")

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print(f"TVL data saved to {OUTPUT_PATH}")
print(df.tail())
