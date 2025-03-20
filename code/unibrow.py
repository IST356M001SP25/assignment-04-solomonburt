'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

def main():
    st.title("UniBrow - Data Explorer")
    st.markdown("Effortlessly browse and analyze your data files.")

    uploaded_file = st.file_uploader("Choose a file (CSV, Excel, JSON)", type=["csv", "xlsx", "json"])

    if uploaded_file is not None:
        file_extension = pl.get_file_extension(uploaded_file.name)
        data_frame = pl.load_file(uploaded_file, file_extension)
        available_columns = pl.get_column_names(data_frame)

        selected_columns = st.multiselect("Columns to display:", available_columns, default=available_columns)

        with st.expander("Data Filtering"):
            if st.checkbox("Enable filtering"):
                string_columns = pl.get_columns_of_type(data_frame, 'object')
                if string_columns:
                    filter_column = st.selectbox("Filter by column:", string_columns)
                    unique_values = pl.get_unique_values(data_frame, filter_column)
                    selected_value = st.selectbox("Filter by value:", unique_values)
                    filtered_data = data_frame[data_frame[filter_column] == selected_value][selected_columns]
                else:
                    st.warning("No string columns available for filtering.")
                    filtered_data = data_frame[selected_columns]
            else:
                filtered_data = data_frame[selected_columns]

        st.subheader("Data Preview")
        st.dataframe(filtered_data)

        st.subheader("Descriptive Statistics")
        st.dataframe(filtered_data.describe())

if __name__ == "__main__":
    main()
