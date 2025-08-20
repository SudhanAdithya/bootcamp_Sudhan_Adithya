# Data Storage

## Folder Structure

- `data/raw/`  
  Contains raw data files as originally collected or downloaded.  
  Files here are kept in CSV format for easy access and portability.

- `data/processed/`  
  Stores cleaned or processed datasets ready for analysis or modeling.  
  Files are saved in Parquet format for efficient storage and fast reading.

## Data Formats

- **CSV (.csv)**  
  - Plain text, human-readable format.  
  - Ideal for raw data because it’s easy to inspect and share.

- **Parquet (.parquet)**  
  - Columnar storage format optimized for analytical queries.  
  - Used for processed data due to compression and faster I/O in pandas workflows.

## Environment Variables

Paths to data folders are configured via environment variables loaded from a `.env` file using the `python-dotenv` package:

```env
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
