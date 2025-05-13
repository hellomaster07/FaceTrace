import pandas as pd

def remove_duplicate_entries(input_file, output_file, sheet_name=0):
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    
    df_cleaned = df.drop_duplicates(subset=["Name", "Timestamp"])
    
    df_cleaned.to_excel(output_file, index=False)
    
    print(f"Duplicates removed. Cleaned data saved to {output_file}")

input_excel = "face_log.xlsx"  
output_excel = "output.xlsx"
remove_duplicate_entries(input_excel, output_excel)
