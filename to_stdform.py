import pandas as pd
import os


df = pd.read_csv('extracted_dataset/images_info.csv')
df.index = df['body_region']+'/'+df['age_month'].astype(str)+'_'+df['filename']
df['label'] = 'normal'
df.drop(columns=['image_urls', 'filename'], inplace=True)

df['is_valid_file'] = [os.path.isfile(f'extracted_dataset/images/{file_path}') for file_path in df.index]
df = df[df['is_valid_file']]
df.drop(columns='is_valid_file', inplace=True)
df = df.loc[~df.index.duplicated()]

df.to_csv('extracted_dataset/metainfo.csv')
