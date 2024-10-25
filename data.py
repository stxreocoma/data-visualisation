import pandas as pd

def Open(filepath):
    try:
        return pd.read_excel(filepath)
    except FileNotFoundError:
        print(f"Error: file '{filepath}' not found")
    except pd.errors.ParserError:
        print(f"Error: failed to parse file '{filepath}'")
    except pd.errors.EmptyDataError:
        print(f"Error: file '{filepath}' is empty")
    except Exception as e:
        print(f"Error while opening file: {e}")
        return None