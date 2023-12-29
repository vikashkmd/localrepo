import pandas as pd 
url = 'https://raw.githubusercontent.com/vikashkmd/DSMLNotebooks/main/loansdata.csv'
data = pd.read_csv(url)
print(data.shape)
data.head()