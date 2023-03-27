import pandas as pd

# create a sample dataframe
df = pd.DataFrame({
    'Name': ['John', 'Mike', 'Sara', 'Amy'],
    'Age': [22, 25, 19, 31],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# display the dataframe as a table
print(df.to_string(index=False))