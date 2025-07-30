
import pandas as pd

def csv_reader(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        return df
    except UnicodeDecodeError as e:
        try:
            df = pd.read_csv(file_path, encoding='latin-1')
            return df
        except UnicodeDecodeError as e:
            try:
                df = pd.read_csv(file_path, encoding='utf-16')
                return df
            except UnicodeDecodeError as e:
                try:
                    df = pd.read_csv(file_path, encoding='utf-32')
                    return df
                except UnicodeDecodeError as e:
                    print(e)
                    return None

def csv_saver(df, file_path):
    try:
        df.to_csv(file_path, index=False, encoding='utf-8')
        return True
    except UnicodeEncodeError as e:
        try:
            df.to_csv(file_path, index=False, encoding='latin-1')
            return True
        except UnicodeEncodeError as e:
            try:
                df.to_csv(file_path, index=False, encoding='utf-16')
                return True
            except UnicodeEncodeError as e:
                try:
                    df.to_csv(file_path, index=False, encoding='utf-32')
                    return True
                except Exception as e:
                    print(e)
                    return False