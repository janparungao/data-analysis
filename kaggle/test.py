import pandas as pd

tmd_file_path = "kaggle/TMDb_updated.CSV"
movie_data = pd.read_csv(tmd_file_path)
print(movie_data.columns)
