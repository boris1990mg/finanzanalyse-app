import pandas as pd

def parse_bwa_file(file, filename):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        df = pd.read_excel(file, header=None)
    elif filename.endswith('.csv'):
        df = pd.read_csv(file, header=None)
    else:
        raise ValueError('Unsupported file format')

    df = df.dropna()
    return df