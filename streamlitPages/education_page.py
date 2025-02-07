import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os

def education():
    st.title("🎓 Education")

    # Navigation links
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("[Masters](#masters)")

    with col2:
        st.markdown("[Bachelors](#bachelors)")

    with col3:
        st.markdown("[Intermediate](#intermediate)")

    with col4:
        st.markdown("[High School](#school)")

    # Initialize session state keys
    if 'view_masters' not in st.session_state:
        st.session_state['view_masters'] = False
    if 'view_esn_Siegen' not in st.session_state:
        st.session_state['view_esn_Siegen'] = False
    if 'view_examboard' not in st.session_state:
        st.session_state['view_examboard'] = False
    if 'view_bachelors' not in st.session_state:
        st.session_state['view_bachelors'] = False
    if 'view_bachelors_transcript' not in st.session_state:
        st.session_state['view_bachelors_transcript'] = False 
    if 'view_intermediate' not in st.session_state:
        st.session_state['view_intermediate'] = False
    if 'view_school' not in st.session_state:
        st.session_state['view_school'] = False

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
                st.download_button(label=f"⬇️ {download_label}", data=PDFbyte, file_name=os.path.basename(file_path), mime='application/pdf')
        else:
            st.error(f"File not found: {file_path}")

    # Masters
    st.markdown('<a id="masters"></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding-top: 80px;"></div>', unsafe_allow_html=True)
    st.header("[Masters of Science in Mechatronics](https://www.mechatronics.eti.uni-siegen.de/)")
    st.write("[🏫 University of Siegen](https://www.uni-siegen.de/start/)")
    col1, col2, col3 = st.columns(3)
    col1.write("📅 Start Date: 2021-October")
    col2.write("📅 End Date: 2024-September")
    col3.write("📍 Location: Siegen, Germany")
    st.write("🏆 Achievements:")
    st.write("  - 🏅 Grade: 1.4 / 4 (1 being best)")
    st.write("  - 📚 Subjects: Focus on Deep Learning, Computer Vision, Machine Learning, Unsupervised Deep Learning, C++, Embedded Systems, Industrial Communication, Control Systems")
    st.write("  - 🤝 Volunteered with ESN Siegen and Examination Board")
    col1, col2 = st.columns(2)
    with col1:
        view_pdf("./assets/masters_list_of_Achievements.pdf", "View Master List of Achievements", "Unview Master List of Achievements", "view_masters")
        view_pdf("./assets/ESN_Siegen.pdf", "View ESN Siegen Certificate", "Unview ESN Siegen Certificate", "view_esn_Siegen")
        view_pdf("./assets/Examination_Board_acknowledgement.pdf", "View Examination Board Certificate", "Unview Examination Board Certificate", "view_examboard")
    with col2:
        download_pdf("./assets/masters_list_of_Achievements.pdf", "Download Master List of Achievements")
        download_pdf("./assets/ESN_Siegen.pdf", "Download ESN Siegen Certificate")
        download_pdf("./assets/Examination_Board_acknowledgement.pdf", "Download Examination Board Certificate")
        

    # Bachelors
    st.markdown('<a id="bachelors"></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding-top: 80px;"></div>', unsafe_allow_html=True)
    st.header("[Bachelors of Technology in Mechanical Engineering](https://nitc.ac.in/department/mechanical-engineering)")
    st.write("[🏫 National Institute of Technology Calicut](https://nitc.ac.in/)")
    col1, col2, col3 = st.columns(3)
    col1.write("📅 Start Date: 2014-August")
    col2.write("📅 End Date: 2018-May")
    col3.write("📍 Location: Calicut, India")
    st.write("🏆 Achievements:")
    st.write("  - 🏅 CGPA: 7.77 / 10")
    st.write("  - 🤝 Attended Inter-NIT Volleyball Competitions")
    col1, col2 = st.columns(2)
    with col1:
        view_pdf("./assets/Btech_certificate.pdf", "View Btech certificate", "Unview Btech certificate", "view_bachelors")
        view_pdf("./assets/Btech_Transcript.pdf", "View Btech Transcript", "Unview Btech Transcript", "view_bachelors_transcript")
    with col2:
        download_pdf("./assets/Btech_certificate.pdf", "Download Btech certificate")
        download_pdf("./assets/Btech_Transcript.pdf", "Download Btech Transcript")

    # Intermediate
    st.markdown('<a id="intermediate"></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding-top: 80px;"></div>', unsafe_allow_html=True)
    st.header("Intermediate")
    st.write("🏫 Narayana Junior Colege")
    col1, col2, col3 = st.columns(3)
    col1.write("📅 Start Date: 2012-July")
    col2.write("📅 End Date: 2014-April")
    col3.write("📍 Location: Vijayawada, India")
    st.write("🏆 Achievements:")
    st.write("  - 🏅 Marks: 970 / 1000")
    st.write("  - 🏅 Achieved a All Inida Rank of 4553 out 1.3 Million Students for the Joint Entrance Exam(JEE mains) in 2014.")
    st.write("  - 📚 Subjects: Focus on Maths, Physics, Chemistry")
    col1, col2 = st.columns(2)
    with col1:
        view_pdf("./assets/Intermediate_certificate.pdf", "View Intermediate Certificate", "Unview Intermediate Certificate", "view_intermediate")
    with col2:
        download_pdf("./assets/Intermediate_certificate.pdf", "Download Intermediate Certificate")

    # School
    st.markdown('<a id="school"></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding-top: 80px;"></div>', unsafe_allow_html=True)
    st.header("High School Diploma")
    st.write("🏫 SFS High School")
    col1, col2, col3 = st.columns(3)
    col1.write("📅 Start Date: 2011-June")
    col2.write("📅 End Date: 2012-April")
    col3.write("📍 Location: Nagulaplem India")
    st.write("🏆 Achievements:")
    st.write("  - 🏅 Grade of 9.8/10")
    st.write("  - 🏆 Sports Captain")
    st.write("  - 🏃 Active in sports (kabaddi, volleyball)")
    st.write("  - 🎭 Participated in stage drama and debates")
    col1, col2 = st.columns(2)
    with col1:
        view_pdf("./assets/School_certificate.pdf", "View High School Certificate", "Unview High School Certificate", "view_school")
    with col2:
        download_pdf("./assets/School_certificate.pdf", "Download High School Certificate")

if __name__ == "__main__":
    education()