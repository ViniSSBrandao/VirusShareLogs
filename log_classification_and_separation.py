import os
import pandas as pd

# Specify the directory where you want to save the files

block = '00485'
print(f'Generating catalog for VirusShare_{block}')
count_directory_path= f"./Logs_By_VirusShare/{block}"
mime_directory_path="./TypeCounts"


# Ensure the directory exists
os.makedirs(count_directory_path, exist_ok=True)

origem = f'Untreated_logs/registro_destino_{block}.csv'

# Load data
data = pd.read_csv(origem)

# Count occurrences of each MIME type and convert to DataFrame
mime_counts = data['Tipo MIME'].value_counts().reset_index()
mime_counts.columns = ['Tipo MIME', 'Count']


mime_counts['Virus_Share_Package'] = origem

# Save the MIME counts to a CSV file
mime_counts.to_csv(os.path.join(mime_directory_path, f'mime_counts{block}.csv'), index=False)

# Group data by 'Tipo MIME' and save to the specified directory
for mime_type, group in data.groupby('Tipo MIME'):
    filename = f"{mime_type.replace('/', '_')}.csv"
    full_path = os.path.join(count_directory_path, filename)
    group.to_csv(full_path, index=False)

# Print MIME counts DataFrame
print(mime_counts)
