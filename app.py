import pandas as pd
import os
current_directory = os.getcwd()
relative_path_to_csv = "desktop\dataforstreamlit.csv"
full_path_to_csv = os.path.join(current_directory, relative_path_to_csv)
df = pd.read_csv(full_path_to_csv)

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Visualisasi Peminjaman Sepeda", layout="wide")
convert_dict = {'year': 'string',
                'month': 'string',
                  }
df = df.astype(convert_dict)

st.sidebar.header("Pemilihan Kategori:")
tahun = st.sidebar.selectbox(
    'Tahun Data',
    ('2011', '2012'))

bulan = st.sidebar.selectbox(
    'Bulan Data',
    ('January', 'February', 'March', 'April', 'Mei', 'June', 'July', 'August', 'September', 'October', 'November', 'Desember'))

selected_data = df.loc[(df['year'] == tahun) & (df['month'] == bulan)]
sum_pinjam = selected_data['cnt'].sum()
avg_pinjam = round(selected_data["cnt"].mean(), 2)

y_casual = selected_data['casual']
x_casual = selected_data['casual'].reset_index()
x_casual = x_casual['index']

fig_casual, ax = plt.subplots()
ax.bar(x_casual, y_casual, color='blue')
ax.set_xlabel('Hari')
ax.set_ylabel('Jumlah Sepeda')
ax.set_title('Jumlah Sepeda yang Dipinjam Oleh Konsumen Tipe Casual')

y_regis = selected_data['registered']
x_regis = selected_data['registered'].reset_index()
x_regis = x_regis['index']

fig_regis, ax = plt.subplots()
ax.bar(x_regis, y_regis, color='blue')
ax.set_xlabel('Hari')
ax.set_ylabel('Jumlah Sepeda')
ax.set_title('Jumlah Sepeda yang Dipinjam Oleh Konsumen Tipe Registered')

column1, column2 = st.columns(2)
column3, column4 = st.columns(2)
with column1:
    st.write('Total Peminjaman', bulan, tahun, ': ', sum_pinjam)
with column2:
    st.write('Rata-Rata Peminjaman', bulan, tahun, ': ', avg_pinjam)
with column3:
    st.pyplot(fig_casual, use_container_width=True)
with column4:
    st.pyplot(fig_regis, use_container_width=True)

