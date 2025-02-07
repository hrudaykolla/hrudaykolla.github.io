import streamlit as st

def home():
    # Set the title of the page
    st.title("Welcome to My Profile")

    # Add a photo and about me section side by side
    col1, col2 = st.columns([1.5, 3])
    
    with col1:
        st.image("assets/profile_photo.png", caption="", width=200)
    
    with col2:
        st.header("About Me")
        st.write("""
        Hello! I am Hruday Kumar, a motivated engineer with 4 years of expertise in software development, AI, machine learning, LLMs, and multimodal models.\n
        Interested in Cloud | Networking | follows AI news and articles | technology updates | learn everyday | adapt to new technologies.
        """)

    # What I do section
    st.header("What I Do")
    st.write("""
    I specialize in AI, machine learning, and large language models (LLMs). I have a strong focus on developing and deploying AI solutions that address real-world problems.
    Currently, I am learning agentic frameworks like AutoGen, LangGraph, and Crew AI.
    """)

    # Key skills section
    st.header("My Key Skills")

    skills = {
        "Programming Languages & Tools": [
            "Python", "VSCode", "Jupyter Notebook", "GitHub", "Docker", 
            "Azure", "SQL", "MS Office", "Linux", "WSL", "SLURM", 
            "Neptune", "TensorBoard"
        ],
        "Data Science & Machine Learning": [
            "Machine Learning", "Deep Learning", "Computer Vision", 
            "NLP", "LLMs", "Data Processing", "Data Cleaning", 
            "Feature Engineering", "Time-Series Analysis", "Classification Models", 
            "Clustering", "Pretrained Models", "Open AI"
        ],
        "Libraries & Frameworks": [
            "Numpy", "Pandas", "Matplotlib", "Seaborn", "Open CV", "Hugging Face", 
            "Langchain", "LlamaIndex", "Langgraph", "Chroma DB", "Anomalib"
        ],
    }

    for category, items in skills.items():
        st.subheader(category)
        cols = st.columns(4)
        for i, item in enumerate(items):
            cols[i % 4].write(f"- {item}")

    # Interests and Languages section side by side
    col1, col2 = st.columns(2)

    with col1:
        st.header("My Interests")
        st.write("""
        - 🏐 Volleyball
        - 🏸 Badminton
        - 🏋️ Workout
        - 💹 Investment
        - 💻 Technology Enthusiast
        """)

    with col2:
        st.header("I Speak")
        languages = {
            "English": "Fluent",
            "German": "Basic Conversational, Learning",
            "Telugu": "Native"
        }
        for language, proficiency in languages.items():
            st.write(f"- **{language}**: {proficiency}")

    # Contact section
    st.header("Contact Me")
    st.write("""
    Feel free to reach out to me via email or connect with me on LinkedIn and GitHub.
    """)

    # Add contact information
    st.write("""
        - 📧 Email: [hrudaykumar16@gmail.com](mailto:your.email@example.com)
        - 📱 Mobile: +4915758285757
        - 💼 LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/hrudaykolla/)
        - 💻 GitHub: [My GitHub Profile](https://github.com/hrudaykolla/)
    """)

    # Footer
    st.markdown("""
    <style>
    footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    home()