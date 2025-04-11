import streamlit as st

from streamlitPages.home_page import home as home_page
from streamlitPages.education_page import education as education_page
from streamlitPages.personal_projects_page import personal_projects as personal_projects_page
from streamlitPages.professional_experience_page import professional_experience as professional_experience_page

st.set_page_config(
    layout="wide"
)

# Define pages with unique URL pathnames
Home_page = st.Page(home_page, title="Profile", icon="👤",
                    default=True, url_path="profile")
education_page = st.Page(education_page, title="Education",
                         icon="🎓", url_path="education")
personal_projects_page = st.Page(
    personal_projects_page, title="Personal Projects", icon="💻", url_path="personal_projects")
professional_experience_page = st.Page(
    professional_experience_page, title="Professional Experience", icon="💼", url_path="professional_experience")

# Configure navigation with sections
pages = [
    Home_page,
    professional_experience_page,
    education_page,
    personal_projects_page,
]

# Initialize navigation
selected_page = st.navigation(pages, position="sidebar", expanded=True)

# Run the selected page
selected_page.run()
