import streamlit as st
from template_filter import template_filter
from title_filter import title_filter
from template_correction import template_correction


def main():
    st.title("Phishing Campaign Tool")

    selection = st.sidebar.radio(
        "Go to", ["Home", "Title Filter", "Template Filter", "Template Correction"]
    )
    if selection == "Title Filter":
        title_filter()
    elif selection == "Template Filter":
        template_filter()
    elif selection == "Template Correction":
        template_correction()

    else:
        st.write("Select a tool from the sidebar to begin.")


main()
