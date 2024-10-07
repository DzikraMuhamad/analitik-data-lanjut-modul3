import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Streamlit Simple App')

page = st.sidebar.radio('Pilih halaman', ['Dataset', 'Visualisasi'])

# Baca data sekali untuk menghindari membaca ulang pada setiap halaman

data = pd.read_csv('pddikti_example.csv')

if page == "Dataset" :
    st.header('Halaman Dataset')

    if 'data' in locals():
        st.write(data)
    else:
        st.warning("Data tidak tersedia")

elif page == "Visualisasi" :
    st.header('Halaman Visualisasi')

    if 'data' in locals():
        # st.set_option('deprecation.showPyplotGlobalUse', False)

        selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
        filtered_data = data[data['universitas'] == selected_university]

        if filtered_data.empty:
            st.warning("Tidak ada data untuk universitas yang dipilih.")
        else:
            plt.figure(figsize=(12,6))

            for prog_studi in filtered_data['program_studi'].unique():
                subset = filtered_data[filtered_data['program_studi'] == prog_studi]
                subset = subset.sort_values(by='id', ascending=False)

                plt.plot(subset['semester'], subset['jumlah'], label = prog_studi)

            plt.title(f'Visualisasi Data untuk {selected_university}')
            plt.xlabel('Semester')
            plt.xticks(rotation=90)
            plt.ylabel('Jumlah')
            plt.legend()

            st.pyplot()
    else:
        st.warning("Data tidak tersedia untuk divisualisasikan.")
