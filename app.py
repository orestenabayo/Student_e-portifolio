import streamlit as st
import time

# Set page configuration at the very top
st.set_page_config(page_title="OREST'S E-PORTIFOLIO", page_icon="💩", layout="wide")

# Apply custom styling
st.markdown("""
    <style>
        .main {background-color: #f5f7fa;}
        .stSidebar {background-color: #2E4053; color: blue;}
        .stTitle {color: #1F618D;}
        .stSubheader {color: #283747;}
        .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
        .stProgress {background-color: #D5D8DC;}
        .stExpander {transition: all 0.3s ease-in-out;}
        
        /* Fade-in effect */
        .fade-in {opacity: 0; transition: opacity 1s ease-in-out;}
        .fade-in.visible {opacity: 1;}
        
        /* Hover effect for project cards */
        .hover-effect:hover {transform: scale(1.05); transition: 0.3s;}
        
        /* Scroll animations */
        .scroll-animate {opacity: 0; transform: translateY(50px); transition: opacity 0.6s ease-out, transform 0.6s ease-out;}
        .scroll-animate.visible {opacity: 1; transform: translateY(0);}
    </style>
""", unsafe_allow_html=True)

# Streamlit app title
st.title("🎓 Welcome to the Student Portfolio App")
st.write("Explore student achievements and projects.")

# Sidebar navigation
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Settings", "Contact", "Testimonials"])

# Initialize session state variables if they don't exist
if 'name' not in st.session_state:
    st.session_state.name = "Oreste NABAYO ISHIMWE"
if 'location' not in st.session_state:
    st.session_state.location = "Musanze, Rwanda" 
if 'bio' not in st.session_state:
    st.session_state.bio = "I am a passionate AI engineer, Data Analytics and Business Enterprenuer!"

# Theme Customization (White/Dark Mode)
theme = st.selectbox("Choose Theme", ["White", "Dark"], key="theme_selectbox")
if theme == "White":
    st.markdown("""
        <style>
            .main {background-color: #ffffff; color: black;}
            .stSidebar {background-color: #f0f0f0; color: black;}
            .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
            .stExpander {background-color: #ffffff; color: black;}
            .stProgress {background-color: #D5D8DC;}
            .stSidebar .css-1d391kg, .stSidebar .css-1v3fvcr, .stSidebar .css-1v3fvcr a {color: black;} /* Navigation bar text color */
            .stSidebar .css-1v3fvcr {color: black;} /* Navigation bar text color */
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .main {background-color: #2E2E2E; color: white;}
            .stSidebar {background-color: #1E1E1E; color: white;}
            .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
            .stExpander {background-color: #2E2E2E; color: white;}
            .stProgress {background-color: #D5D8DC;}
            .stSidebar .css-1d391kg, .stSidebar .css-1v3fvcr, .stSidebar .css-1v3fvcr a {color: white;} /* Navigation bar text color */
            .stSidebar .css-1v3fvcr {color: white;} /* Navigation bar text color */
        </style>
    """, unsafe_allow_html=True)

# Home section
if page == "Home":
    st.title("🧑‍🎓 Student Profile")
    st.image("5.png", width=150, caption="Default image")

    # Display profile details
    st.subheader("📌 Personal Details")
    st.markdown(f"*📍 Location:* {st.session_state.location}")
    
    # About Me (Short introduction)
    st.subheader("🔹 About Me")
    st.write(st.session_state.bio)

    # If "Customize Profile" is clicked, allow editing
    if st.session_state.get('editing_profile', False):
        st.session_state.name = st.text_input("Name:", st.session_state.name)
        st.session_state.location = st.text_input("Location:", st.session_state.location)
        st.session_state.bio = st.text_area("Short introduction about myself:", st.session_state.bio)

        # Save and update profile
        if st.button("Save Profile Changes"):
            st.success("✅ Profile updated successfully!")
    
    # Show 'Customize Profile' button
    if st.button("Customize Profile"):
        st.session_state.editing_profile = True
    else:
        st.session_state.editing_profile = False

    # Resume download button
    with open("resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")
    
    st.markdown("---")


# Projects section
elif page == "Projects":
    st.title("💻 My Projects")
    
    # Project Filtering System
    category = st.selectbox("Filter projects by category:", ["All", "Year 1 Project", "Group Projects", "Dissertation"], key="project_filter")
    
    project_data = {
        "Year 1 Project": {
            "📊 Data Analysis Project": {
                "type": "Individual",
                "description": ".",
                "link": "https://github.com/orestenabayo/CathServ.git"
            }
        },
        "Year 2 Project": {
            "🤖 AI Chatbot": {
                "type": "Group",
                "description": "Together with my  collegues we developed a site where you can view our profile & what we have developed together.",
            }
        },
        "Year 3 Project": {
            "🌐 Student attendance system": {
                "type": "Group",
                "description": "Designed and developed a website for ONLINE STUDENT ATTENDANCE.",
            }
        },
        "Dissertation": {
            "🌍 Football System Management": {
                "type": "Individual",
                "description": "Designed and developed a website for football management system.",
            }
        }
    }
    
    # Display the projects based on the category filter
    if category == "All":
        filtered_projects = {k: v for cat in project_data.values() for k, v in cat.items()}
    else:
        filtered_projects = project_data.get(category, {})
    
    for project, details in filtered_projects.items():
        with st.expander(project, expanded=False):
            time.sleep(0.1)  # Smooth transition
            st.write(f"*Type:* {details['type']}")
            st.write(f"*Description:* {details['description']}")
            if details.get("link"):
                st.markdown(f"[Link to Code]({details['link']})")
    
    st.markdown("---")
    
    # Student Testimonials
    st.subheader("🗣️ Student Testimonials")
    testimonials = [
        "Oreste is a brilliant problem solver! His final year project was truly innovative. – Dr. Theodore",
        "Oreste's dedication to Data Analystics is inspiring. He never stops learning! – Lecture. SHIMIRWA Aline Valerie",
        "A great team mentor and developer. Oreste delivers high-quality projects. – Teammate Prince"
    ]
    for testimonial in testimonials:
        st.write(f"🗨️ {testimonial}")
    
    st.markdown("---")
    
    # Timeline of Academic & Project Milestones
    st.subheader("⏳ Timeline of Academic & Project Milestones")
    milestones = [
        "✅ Year 2023: Web Design project completed",
        "🏆 Year 2024: Backend Specialization in ALX",
        "💼 08/07/2025: AI Learning",
        "📖 Year 2025: Dissertation submission"
    ]
    for milestone in milestones:
        st.write(f"- {milestone}")

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")
    
    st.subheader("Programming Skills")
    st.write("Python: 90%")
    st.progress(90)
    
    st.write("JavaScript: 75%")
    st.progress(75)
    
    st.write("Artificial Intelligence: 65%")
    st.progress(65)

    st.write("Machine Learning: 75%")
    st.progress(75)

    st.write("React Js: 75%")
    st.progress(75)
    
    st.subheader("🏆 Certifications & Achievements")
    st.write("✔ Completed AI & ML in Business Certification")
    st.write("✔ Certified Backend Developer")

# Contact section
elif page == "Contact":
    st.title("📬 Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your message")
        
        submitted = st.form_submit_button("Send message")
        if submitted:
            if name and email and message:
                st.success("✅ message sent successfully!")
                # Displaying the message after submission
                st.write(f"*Name:* {name}")
                st.write(f"*Email:* {email}")
                st.write(f"*message:* {message}")
            else:
                st.error("⚠️ Please fill in all fields before submitting.")

    # Contact Information Links
    st.markdown("*📧 Email:* orestenabayo@gmail.com")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/)")
    st.markdown("[📂 GitHub](https://github.com/orestenabayo/)")
    st.markdown("[📂 Instagram](https://www.instagram.com/)")

# Settings section
elif page == "Settings":
    st.title("⚙️ Settings")

    # Theme Customization (White/Dark Mode)
    theme = st.selectbox("Choose Theme", ["White", "Dark"], key="settings_theme_selectbox")
    if theme == "White":
        st.markdown("""
            <style>
                .main {background-color: #ffffff; color: black;}
                .stSidebar {background-color: #f0f0f0; color: black;}
                .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
                .stExpander {background-color: #ffffff; color: black;}
                .stProgress {background-color: #D5D8DC;}
                .stSidebar .css-1d391kg, .stSidebar .css-1v3fvcr, .stSidebar .css-1v3fvcr a {color: black;} /* Navigation bar text color */
                .stSidebar .css-1v3fvcr {color: black;} /* Navigation bar text color */
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .main {background-color: #2E2E2E; color: white;}
                .stSidebar {background-color: #1E1E1E; color: white;}
                .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
                .stExpander {background-color: #2E2E2E; color: white;}
                .stProgress {background-color: #D5D8DC;}
                .stSidebar .css-1d391kg, .stSidebar .css-1v3fvcr, .stSidebar .css-1v3fvcr a {color: white;} /* Navigation bar text color */
                .stSidebar .css-1v3fvcr {color: white;} /* Navigation bar text color */
            </style>
        """, unsafe_allow_html=True)

# Student Testimonials Section
if page == "Testimonials":
    st.title("🗣️ Student Testimonials")
    
    # Display example testimonial
    st.subheader("💬Testimonial:")
    st.write("*Oreste is a brilliant problem solver! His final year project is truly innovative. – Mclement*")
    
    st.markdown("---")
    
    # Allow classmates or mentors to leave testimonials
    st.subheader("✍️ Leave a Testimonial")
    
    with st.form("testimonial_form"):
        name = st.text_input("Your Name")
        relationship = st.selectbox("Your Relationship", ["Classmate", "Mentor", "Teammate", "Other"], key="relationship_selectbox")
        testimonial_message = st.text_area("Your Testimonial")
        
        submitted = st.form_submit_button("Submit Testimonial")
        if submitted:
            if name and testimonial_message:
                st.success(f"✅ Thank you, {name}! Your testimonial has been submitted.")
                # Display the testimonial after submission
                st.write(f"🗨️ {testimonial_message} — {name} ({relationship})")
            else:
                st.error("⚠️ Please fill in all fields before submitting.")   