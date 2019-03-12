#practice

import pandas as pd

#downloaded all_contracts_prime_transactions_1.csv from Dropbox supplied by Tamr
#import as dataframe
practice = pd.read_csv(r"all_contracts_prime_transactions_1.csv")
practice_df = pd.DataFrame(practice, columns = ["recipient_name", "recipient_parent_name"])

#assuming all columns are same (file too large to open on my machine and check), concatenate with:
#single_df = pd.concat(practice_df)

print(practice_df[0:2])
