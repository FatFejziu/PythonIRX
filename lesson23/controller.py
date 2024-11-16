import streamlit as st
import requests
import pandas as pd

st.title("Project Menagment App")

st.header("Add a Developer")
dev_name=st.text_input("Developer Name")
dev_experience=st.number_input("Experience (years)",min_value=0, max_value=50,value=0)

if st.button("create Developer"):
    dev_data={"name":dev_name,"experience":dev_experience}
    response=requests.post("http://lockalhost:800/developers/",json=dev_data)

st.header("Project dashboard")

if st.button("Get Projects"):
    response=requests.get("http://lockalhost:800/projects/")
    projects_data=response.json()["projects"]

    if projects_data:
        projects_df=pd.DataFrame(projects_data)

        st.subheader("Projects Overview")
        st.dataframe(projects_df)

        st.subheader("Project Details")
        for project in projects_data:
            st.markdown(f"### {project["title"]}")
            st.markdown(f"**Description:** {project["description"]}")
            st.markdown(f"**Languages Used:** {" , ".join(project["languages"])}")
            st.markdown(f"**Lead Developer:**{project["lead_developer"]["name"]} with{project["lead_developer"]["experience"]} years of experience")
    else:
        st.warning("No projects found!")