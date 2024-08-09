import pandas as pd

file_path = 'ventas.txt'
df = pd.read_csv(file_path, delimiter='\t')

# Remove extra columns and extra whitespaces 
df.columns = df.columns.str.strip()
df = df[['KUNNR', 'ERDAT', 'KWMENG']]

# NOTE: Como es un ejercicio, renombro el nombre de las columnas por simplificar
df = df.rename(columns={'KUNNR': 'client', 'ERDAT': 'date', 'KWMENG': 'sales'})

# Sort by date
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df = df.sort_values(by='date')

df.to_csv('client_date_sales_data.csv', index=False)


# I'm also interested in just the total sales per day, without the client info.
df = df.drop(columns="client")
total_sales_per_day = df.groupby('date')['sales'].sum().reset_index()

total_sales_per_day.to_csv('daily_sales.csv', index=False)