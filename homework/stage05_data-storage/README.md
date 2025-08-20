# Data Storage

## Folder Structure

- `data/raw/`: Contains raw, unprocessed data files. These are the original data files as received or generated, and should not be modified manually.
- `data/processed/`: Contains processed data files, such as cleaned or transformed datasets ready for analysis or modeling.

## Formats Used and Why

- **CSV (Comma-Separated Values):**
  - Used for raw data storage due to its simplicity, human-readability, and wide compatibility with tools and platforms.
- **Parquet:**
  - Used for processed data because it is a columnar storage format that is efficient for both storage and analytical queries. Parquet supports fast reading/writing and preserves data types better than CSV.

## Reading and Writing Data

- The code uses environment variables (`DATA_DIR_RAW` and `DATA_DIR_PROCESSED`) defined in a `.env` file to determine the locations for raw and processed data.
- Utility functions `write_df` and `read_df` automatically select the correct file format (CSV or Parquet) based on the file extension:
  - `write_df(df, path)`: Writes a DataFrame to the specified path, creating directories as needed. Handles both `.csv` and `.parquet` formats. If the Parquet engine is missing, a clear message is shown.
  - `read_df(path)`: Reads a DataFrame from the specified path, supporting both `.csv` and `.parquet` formats. If the Parquet engine is missing, a clear message is shown.

## Example Usage

```python
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
DATA_DIR_RAW = os.getenv("DATA_DIR_RAW", "data/raw")
DATA_DIR_PROCESSED = os.getenv("DATA_DIR_PROCESSED", "data/processed")

# Example DataFrame
df = pd.DataFrame({"id": [1, 2, 3], "value": [10.5, 20.3, 30.7]})

# Write to both formats
write_df(df, f"{DATA_DIR_RAW}/sample.csv")
write_df(df, f"{DATA_DIR_PROCESSED}/sample.parquet")

# Read back
df_csv = read_df(f"{DATA_DIR_RAW}/sample.csv")
df_parquet = read_df(f"{DATA_DIR_PROCESSED}/sample.parquet")
```

## Validation

A small validation function checks that the shapes and dtypes of critical columns match between the two formats, ensuring data integrity after round-trip conversion.
