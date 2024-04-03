import streamlit as st
import pandas as pd

def main():
    st.title("Excel to CSV Converter")


    st.write("Upload your Excel file (.xlsx or .xls)")
    uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "xls"])

    if uploaded_file is not None:

        df = pd.read_excel(uploaded_file)

        st.write("Original Excel data:")
        st.write(df.head())


        if st.button("Convert to CSV"):

            csv_file = df.to_csv(index=False)

            st.download_button(
                label="Download CSV File",
                data=csv_file,
                file_name="converted_file.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()
