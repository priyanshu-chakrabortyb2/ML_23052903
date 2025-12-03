import pandas as pd

url = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_year/1950.csv.gz"

# pandas can read gzip directly from a URL
# the GHCN files do not have a CSV header, so we'll read with header=None
df = pd.read_csv(url, compression='gzip', header=None)

print("Rows:", len(df))
print(df.head())
