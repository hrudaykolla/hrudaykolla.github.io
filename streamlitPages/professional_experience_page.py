import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os


def professional_experience():
    st.title("Professional Experience 💼")
    # Navigation links
    # Create a 2x2 grid using Streamlit columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("[Mercedes Benz AG](#mercedes)")
        st.markdown("[University of Siegen](#siegen)")

    with col2:
        st.markdown("[Robert Bosch GmbH](#bosch)")
        st.markdown("[Larsen and Toubro (L&T) Ltd](#lt)")

    # Initialize session state keys
    if 'view_mercedes' not in st.session_state:
        st.session_state['view_mercedes'] = False
    if 'view_bosch' not in st.session_state:
        st.session_state['view_bosch'] = False
    if 'view_mercedes' not in st.session_state:
        st.session_state['view_mercedes'] = False
    if 'view_siegen' not in st.session_state:
        st.session_state['view_siegen'] = False
    if 'view_lt' not in st.session_state:
        st.session_state['view_lt'] = False

    def view_pdf(file_path, view_label="View Certificate", unview_label="Unview Certificate", key="pdf_view_key"):
        """
        Displays or hides a PDF based on user interaction.

        Args:
        - file_path (str): Path to the PDF file.
        - view_label (str): Label for the "View" button.
        - unview_label (str): Label for the "Unview" button.
        - key (str): Key for session state management.
        """
        # Check if the file exists
        if not os.path.exists(file_path):
            st.error(f"File not found: {file_path}")
            return

        # Determine current view state and set button text
        is_viewing = st.session_state.get(key, False)
        button_label = f"{'🙈 ' + unview_label if is_viewing else '👁️ ' + view_label}"

        # Toggle state based on button click
        if st.button(button_label, key=f"{key}_button"):
            st.session_state[key] = not is_viewing

        # Display PDF if in viewing state
        if st.session_state[key]:
            with open(file_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
                pdf_viewer(PDFbyte)

    # Function to provide a download link for a PDF
    def download_pdf(file_path, download_label):
        if os.path.exists(file_path):
            with open(file_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
                st.download_button(label=f"⬇️ {download_label}", data=PDFbyte, file_name=os.path.basename(
                    file_path), mime='application/pdf')
        else:
            st.error(f"File not found: {file_path}")

    st.markdown('<a id="mercedes"></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding-top: 80px;"></div>',
                unsafe_allow_html=True)
    st.header(
        "Generative AI Developer in the Drive Software Development Team at Mercedes Benz AG, Sindelfingen")
    st.write("📅 June 2024 - Present")
    st.write("📍 Location: Sindelfingen, Germany")
    st.write("""
    Designed & Deployed Scalable AI Solutions on Microsoft Azure: Developed containerized, production-grade web applications using Python and Docker, ensuring secure on-premises to cloud connections via OpenID authentication. Delivered comprehensive proof-of-concepts, engaging presentations, and hands-on workshops to demonstrate technical strategies and gather actionable feedback.

    **Software Requirements Analysis Platform:**  
        - Engineered an innovative platform that leverages advanced NLP and LLM techniques including RAG, OpenAI ADA, and GPT-4O to analyze software requirements against industry standards (e.g., INCOSE, VDA), identify grammatical errors, uncover requirement inconsistencies, and cross-reference legislative documents.  
        - Developed an agentic workflow enabling Automation featuring ReAct agents, powered by LlamaIndex, LangGraph, and Autogen Agentic frameworks. Created a FastAPI interface that connects seamlessly to an Open Web UI via Open Web Pipelines, empowering users to interact with endpoints naturally through intuitive, natural language commands.

    **Developer Query Resolution Tool:**  
        - Answers developer questions by extracting insights from JIRA and Confluence via REST APIs, utilizing RAG, OpenAI Ada, and GPT-4O models for intelligent responses.

    **Skills / Tools:** Python, Docker, FastAPI, Microsoft Azure, SQL, OpenAI (ADA, GPT-4O), LlamaIndex, LangGraph, Autogen, Open Web UI, Open Web Pipelines, Chroma DB, Streamlit, GitHub, Hugging Face, WSL, and advanced NLP techniques.
    """)

    col1, col2 = st.columns(2)
    with col1:
        view_pdf("./assets/mercedes_reference.pdf", "View Mercedes Reference",
                 "Unview Bosch Reference", "view_mercedes")
    with col2:
        download_pdf("./assets/mercedes_reference.pdf",
                     "Download Mercedes Reference")

    st.markdown('<a id="bosch"></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding-top: 80px;"></div>',
                unsafe_allow_html=True)
    st.header("Computer Vision Engineer - Master Thesis at Robert Bosch GmbH")
    st.write("📅 Mar 2024 - September 2024")
    st.write("📍 Location: Reutlingen, Germany")
    st.write("""
    Developed and implemented a novel AI-based unsupervised defect recognition algorithm for analyzing image data in automotive manufacturing processes.

    - Designed and executed an iterative hierarchical clustering approach using foundational models such as DinoV2 for advanced feature extraction.
    - Integrated multiple neural network architectures for feature extraction, followed by dimensionality reduction and custom clustering adaptation.
    - Achieved a 5% improvement in recognition accuracy compared to existing clustering methods through efficient benchmarking on four industrial datasets.
    - Collaborated closely with cross-functional teams for data alignment, ensuring seamless integration and reusability of well-documented code by internal teams.
    - Delivered results ahead of schedule while maintaining quality and efficiency in problem-solving approaches.

    **Skills/Tools**: Vscode, Python, Anomalib, Computer Vision, Pretrained Models, Clustering, Data Processing, GitHub, Numpy, Pandas, Linux, Object Oriented Programming, Open CV, Matplotlib, Seaborn, Gimp, Fiji, Jupyter Notebook
    """)

    col1, col2 = st.columns(2)
    with col1:
        view_pdf("./assets/bosch_reference.pdf", "View Bosch Reference",
                 "Unview Bosch Reference", "view_bosch")
    with col2:
        download_pdf("./assets/bosch_reference.pdf",
                     "Download Bosch Reference")

    st.markdown('<a id="siegen"></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding-top: 80px;"></div>',
                unsafe_allow_html=True)
    st.header("Deep Learning Research Assistant at University of Siegen")
    st.write("📅 July 2023 - February 2024")
    st.write("📍 Location: Siegen, Germany")
    st.write("""
    - Developed a Deep Convolutional LSTM network architecture that improves temporal context without increasing network parameters, with 6% enhancements in accuracy, F1 score, and average MAP across Human Activity Recognition (HAR) datasets.
    - Optimized existing activity detection methods by extracting LSTM features and training them on vision networks, resulting in a 5% improvement in F1 and average MAP scores.
    - Designed a novel outlier removal and dataset normalization method to improve dataset quality and activity recognition accuracy.
    - Developed a theoretical Compensation Matrix with the method of least squares for 3D Imaging to remove harmonic distortions in time-of-flight signals caused by highly scattering medium.

    **Skills/Tools**: Vscode, Jupyter Notebook, Python, SLURM, Linux, Neptune, TensorBoard, GitHub, Numpy, Pandas, Deep Learning, Computer Vision.
    """)

    col1, col2 = st.columns(2)
    with col1:
        view_pdf("./assets/university_siegen_reference.pdf", "View University of Siegen Reference",
                 "Unview University of Siegen Reference", "view_siegen")
    with col2:
        download_pdf("./assets/university_siegen_reference.pdf",
                     "Download University of Siegen Reference")

    st.markdown('<a id="lt"></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding-top: 80px;"></div>',
                unsafe_allow_html=True)
    st.header("Jr. Data Scientist at Larsen and Toubro (L&T) Ltd")
    st.write("📅 July 2018 - June 2021")
    st.write("📍 Location: India")
    st.write("""
    Predictive Maintenance for Industrial Equipment: Collaborated with the Construction equipment division to develop a predictive maintenance system. By analyzing real-time sensor data, we could forecast equipment failures, enabling proactive maintenance scheduling. This approach reduced unplanned downtime by 30% and maintenance costs by 20%.

    **Skills/Tools**: Pycharm, Python, Sensors, Numpy, Pandas, Machine Learning, Matplotlib, Seaborn, SQL, Data Processing Pipelines, Data Cleaning, Time-Series Analysis, Classification Models, Feature Engineering, GridSearchCV.
    """)
