
import pandas as pd
import chardet

def read_csv(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except UnicodeDecodeError as e:
        print(e)
        return None

def save_csv(df, file_path):
    try:
        df.to_csv(file_path, index=False, encoding='utf-8')
        return True
    except UnicodeEncodeError as e:
        print(e)
        return False