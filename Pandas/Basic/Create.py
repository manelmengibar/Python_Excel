import pandas as pd

# dataframe Name and Age columns
df = pd.DataFrame({'Empresa': ['Draexlmaier', 'Seat', 'Fujikura', 'Synergie'],
                   'Anys': [5, 20, 30, 10]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='LListat', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
