import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
DB_NAME = "phishing_campaign"
SOURCE_COLLECTION = "validated_templates"
TARGET_COLLECTION = "validated_templates_reviewed"
REJECTED_COLLECTION = "rejected_templates"


def template_correction():
    st.title("Template Correction")

    templates = list(client[DB_NAME][SOURCE_COLLECTION].find())

    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    if st.session_state.current_index < len(templates):
        template = templates[st.session_state.current_index]
        template_title = client[DB_NAME].dereference(template["title"])

        col1, col2 = st.columns(2)
        with col1:
            st.write("Original Template")
            st.write(f"**Title:** {template_title['title']}")
            st.write(f"**Body:** {template['body']}")
        with col2:
            st.write("Revised Template")
            st.write(f"**Title:** {template_title['title']}")
            body_length = len(template["body"])
            calculated_height = max(200, body_length)
            # Adjust formula as needed
            revised_body = st.text_area(
                "Body", value=template["body"], height=calculated_height
            )

        if st.button("Save Revision"):
            template["original_body"] = template["body"]
            template["body"] = revised_body
            client[DB_NAME][TARGET_COLLECTION].insert_one(template)
            st.session_state.current_index += 1

        if st.button("No Revision Needed"):
            client[DB_NAME][TARGET_COLLECTION].insert_one(template)
            st.session_state.current_index += 1

        if st.button("Reject"):
            client[DB_NAME][REJECTED_COLLECTION].insert_one(template)
            st.session_state.current_index += 1

    else:
        st.write("No more templates to display.")
