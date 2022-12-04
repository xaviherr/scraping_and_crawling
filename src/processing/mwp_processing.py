import pandas as pd
import numpy as np

devices_df = pd.read_csv('devices_list.csv', sep=',')

devices_df['release_date_text'] = devices_df['raw_features']
devices_df['screen_size'] = devices_df['raw_features']

devices_df['release_date'] = pd.to_datetime(devices_df['release_date_text'], format='%Y-%M')
devices_df['phone_age_months'] = (pd.Timestamp().today() - devices_df['release_date'])/np.timedelta64(1, 'M')
devices_df['phone_age_months'] = devices_df['phone_age_months'].astype(int)
