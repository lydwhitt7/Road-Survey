import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.gridspec as gridspec

#import raw data file
Data_Raw = pd.read_excel('Survey_responses2.xlsx')

#transform data
columns_to_check = ['Image_A', 'Image_B', 'Image_C', 'Image_D', 'Image_E', 'Image_F', 'Image_G', 'Image_H']  # replace with your actual column names

counts = {
    col: {
        'yes_count': (Data_Raw[col] == 'Yes').sum(),
        'no_count': (Data_Raw[col] == 'No').sum(),
        'unsure_count': (Data_Raw[col] == 'Unsure').sum()
    }
    for col in columns_to_check
}

Summary_Data = pd.DataFrame.from_dict(counts, orient='index').reset_index().rename(columns={'index': 'column'})

# Dictionary mapping column names to categories
Private_dict = {
    'Image_A': 'No',
    'Image_B': 'Yes',
    'Image_C': 'Yes',
    'Image_D': 'Yes',
    'Image_E': 'No',
    'Image_F': 'Yes',
    'Image_G': 'Yes',
    'Image_H': 'No',
}

Surface_dict = {
    'Image_A': 'Tarmac',
    'Image_B': 'Off-Road',
    'Image_C': 'Off-Road',
    'Image_D': 'Off-Road',
    'Image_E': 'Tarmac',
    'Image_F': 'Off-Road',
    'Image_G': 'Tarmac',
    'Image_H': 'Off-Road',
}

# Add the new column by mapping the dictionary
Summary_Data['Private'] = Summary_Data['column'].map(Private_dict)
Summary_Data['Surface'] = Summary_Data['column'].map(Surface_dict)