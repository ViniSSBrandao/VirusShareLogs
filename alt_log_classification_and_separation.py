import os
import pandas as pd

# Specify the directory where you want to save the files
block = "483"
print(f"Generating catalog for VirusShare_{block}")
count_directory_path = "./Logs_By_VirusShare"
mime_directory_path = "./TypeCounts"
origem = "registro_destino.csv"

try:
    # Check if input file exists
    if not os.path.exists(origem):
        raise FileNotFoundError(f"Input file '{origem}' not found. Please ensure the file exists in the current directory.")

    # Create directories if they don't exist
    for directory in [count_directory_path, mime_directory_path]:
        try:
            os.makedirs(directory, exist_ok=True)
        except PermissionError:
            raise PermissionError(f"Cannot create directory '{directory}'. Please check if you have write permissions.")

    # Load data
    try:
        data = pd.read_csv(origem)
    except Exception as e:
        raise Exception(f"Failed to read '{origem}'. Error: {str(e)}")

    # Count occurrences of each MIME type and convert to DataFrame
    mime_counts = data["MIME_type"].value_counts().reset_index()
    mime_counts.columns = ["MIME_type", "Count"]
    mime_counts["Virus_Share_Package"] = origem

    # Save the MIME counts to a CSV file
    try:
        mime_counts.to_csv(
            os.path.join(mime_directory_path, f"mime_counts{block}.csv"), index=False
        )
    except PermissionError:
        raise PermissionError(f"Cannot write to '{mime_directory_path}'. Please check if you have write permissions.")
    except Exception as e:
        raise Exception(f"Failed to save MIME counts. Error: {str(e)}")

    # Group data by 'MIME_type' and save to the specified directory
    for mime_type, group in data.groupby("MIME_type"):
        filename = f"{mime_type.replace('/', '_')}.csv"
        full_path = os.path.join(count_directory_path, filename)
        try:
            group.to_csv(full_path, index=False)
        except PermissionError:
            raise PermissionError(f"Cannot write to '{full_path}'. Please check if you have write permissions.")
        except Exception as e:
            raise Exception(f"Failed to save file '{full_path}'. Error: {str(e)}")

    # Print MIME counts DataFrame
    print("\nMIME Type Counts:")
    print(mime_counts)

except FileNotFoundError as e:
    print(f"Error: {str(e)}")
except PermissionError as e:
    print(f"Error: {str(e)}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")