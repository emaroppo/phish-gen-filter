import streamlit as st
from template_filter import template_filter
from title_filter import title_filter
from template_correction import template_correction
from pymongo import MongoClient
import pickle as pkl

connection_string = f"mongodb+srv://{st.secrets['db_username']}:{st.secrets['db_pswd']}@{st.secrets['cluster_name']}.mongodb.net/?retryWrites=true&w=majority&appName=Feedback"


@st.cache_resource
def get_db_client():
    return MongoClient(
        connection_string,
    )


client = get_db_client()


def main():
    st.title("Phishing Campaign Tool")

    selection = st.sidebar.radio(
        "Go to", ["Home", "Title Filter", "Template Filter", "Template Correction"]
    )
    if selection == "Title Filter":
        title_filter(client)
    elif selection == "Template Filter":
        template_filter(client)
    elif selection == "Template Correction":
        template_correction(client)

    else:
        st.write("Select a tool from the sidebar to begin.")


main()
