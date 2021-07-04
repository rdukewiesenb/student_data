# Function to hash student names on each survey response CSV

def hash_names(df):
  df["What's your name?"] = [str(hash(x)) for x in df["What's your name?"]]
  return df