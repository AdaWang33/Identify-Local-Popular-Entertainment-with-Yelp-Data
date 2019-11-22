import pandas as pd
df = pd.read_csv('yelp_business.csv')
df = df.drop(['business_id', 'postal_code', 'neighborhood', 'address'], axis=1)
df = df[df['is_open'] == 1]
grouped = df.groupby('state')
grouped.apply(lambda x:x.sort_values(['stars', 'review_count'], ascending=False).head(1)).to_csv('result.csv')