import streamlit as st
from template_filter import template_filter
from title_filter import title_filter
from template_correction import template_correction
from pymongo import MongoClient
import pickle as pkl

with open("secrets.pkl", "rb") as f:
    secrets = pkl.load(f)


@st.cache_resource
def get_db_client():
    return MongoClient(
        secrets["db_connection"],
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
