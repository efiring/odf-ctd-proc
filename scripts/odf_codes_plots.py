import matplotlib
matplotlib.use('ps')

import libODF_merge_codes as merge
import libODF_ctd_plots as ctd_plots

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

qual_codes_filepath = f'/Users/jgum/work_code/cruises/P06_2017/quality_codes/'
cruise_dir = f'/Users/jgum/work_code/cruises/P06_2017/'
log_dir = f'{cruise_dir}ctd_proc_rewrite/data/logs/quality_code/all/'

file_ssscc = f'{cruise_dir}ssscc.csv'
bottle_file= f'{qual_codes_filepath}320620170703_hy1.csv'

### compile bottle trips into one file, then merge with odf_db bottle file
df_bottle = merge.prelim_ctd_bottle_df(file_ssscc, bottle_file)
### compute residuals for plotting
merge.ctd_residuals_df(df_bottle)
df_bottle = merge.merge_ctd_codes(log_dir, df_bottle)
df_coded = merge.get_qc_all_from_df(df_bottle)

ctd_plots.all_plots(df_coded)
