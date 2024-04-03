import streamlit as st

def main():

    st.set_page_config(page_title="About", layout='wide')

    st.title("About")


    st.markdown("This website allows users to upload CSV files, chat with a generative AI model, and generate various types of graphs based on the data. It is built using Python with Streamlit as the web framework.")
    st.image("chatcsv.png", use_column_width=True)
    st.markdown("This page enables users to upload a CSV file and generate various types of graphs based on the data and allows users to convert an Excel file (.xlsx or .xls) to a CSV format")

    st.image("GenerateGraphs.png", use_column_width=True)
    
    st.image("fileocnversion.png", use_column_width=True)


if __name__ == "__main__":
    main()

