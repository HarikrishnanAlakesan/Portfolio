import streamlit as st

# Page setup
st.set_page_config(page_title="Harikrishnan | Autogen Dev Portfolio", layout="wide", page_icon="🤖")

# Custom CSS and JavaScript to handle light/dark theme detection and dynamic styling
st.markdown("""
    <style>
    /* Default styles for Dark Mode */
    body {
        background-color: #0f0f0f;
        color: white;
    }
    .title {
        font-size: 3em;
        color: #00FFE1;
    }
    .subtitle {
        font-size: 1.3em;
        color: #00e6ac;
    }
    .project-card {
        background-color: #1a1a1a;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 0 10px #00ffe180;
        margin-bottom: 1.5rem;
    }
    .btn {
        background-color: #00ffe1;
        color: #000;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: bold;
        text-decoration: none;
    }
    .btn:hover {
        background-color: #00e6ac;
        color: black;
    }
    a {
        color: #00FFE1;
        text-decoration: none;
    }

    /* Light Mode styles */
    .light-mode body {
        background-color: white;
        color: black;
    }
    .light-mode .title {
        color: #0066CC;
    }
    .light-mode .subtitle {
        color: #007ACC;
    }
    .light-mode .project-card {
        background-color: #f4f4f4;
        color: black;
        box-shadow: 0 0 10px #0066CC;
    }
    .light-mode .btn {
        background-color: #0066CC;
        color: white;
    }
    .light-mode .btn:hover {
        background-color: #0057A8;
        color: white;
    }

    /* JavaScript to toggle class based on system theme */
    </style>
    <script>
    function detectAndToggleTheme() {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const body = document.querySelector('body');
        
        if (prefersDark) {
            body.classList.remove('light-mode');
        } else {
            body.classList.add('light-mode');
        }
    }
    
    // Call function on load to set the initial theme
    detectAndToggleTheme();
    
    // Add event listener to listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', detectAndToggleTheme);
    </script>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔗 Navigate")
page = st.sidebar.radio("Pages", ["🏠 Home", "👨‍💻 About", "📂 Projects", "📜 Resume", "📬 Contact"])

# ---- HOME ----
if page == "🏠 Home":
    st.markdown('<h1 class="title">Hey, I\'m Harikrishnan 👋</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Developer of Autonomous Agents | Full-Stack Innovator | Futuristic Thinker</p>', unsafe_allow_html=True)

    st.write("""
    I build intelligent systems where **AI agents collaborate, solve problems, and take action**.  
    From AR classrooms to smart drones, I create **end-to-end solutions** combining AI, data, and design.  
    Check out my live projects, dev tools, and a future driven by autonomy.
    """)

    st.markdown("### 🔥 Featured Live Projects")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("📊 AutoDataML")
        st.write("An automated ML pipeline builder for tabular data with visualization and model comparison.")
        st.markdown("[🌐 Visit AutoDataML](https://autodataml.azurewebsites.net/)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("🧠 Mental Health Chatbot")
        st.write("AI-powered chatbot to support users with mental health queries and predictions.")
        st.markdown("[🌐 Visit Chatbot](https://mental-health-7ctl.onrender.com/)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---- ABOUT ----
elif page == "👨‍💻 About":
    st.header("👨‍💻 About Me")
    st.write("""
        I'm Harikrishnan, a B.Tech student with deep interest in AI automation, full-stack systems, and building digital tools that solve real problems.
        
        I love working with:
        - 🤖 Multi-Agent AI Systems using Autogen
        - 🌍 Scalable ML/AR Applications
        - 🔌 Cross-platform integrations with Firebase, Flask, GCP
    """)
    st.markdown("#### 🧰 Tech Stack")
    st.write("""
    - **Languages:** Python, JavaScript, C++
    - **Web:** Flask, Firebase, React, Bootstrap
    - **AI/ML:** Autogen, OpenCV, TensorFlow, Gemini API, NLP
    - **DevOps/Cloud:** Google Cloud, Netlify, AWS
    - **Tools:** Figma, Power BI, Git, Streamlit
    """)

# ---- PROJECTS ----
elif page == "📂 Projects":
    st.header("📂 Featured Projects")

    projects = [
        ["Heart Disease Prediction", "ML model w/ Tkinter UI (88% accuracy)"],
        ["Audio Emotion Detection", "Speech-to-text & emotion classifier"],
        ["Dynamic Form Generator", "AI-generated HTML forms via Gemini + Firebase"],
        ["Eye-Controlled Mouse", "CV-based eye tracking for input control"],
        ["AR Learning for Kids", "Gesture-controlled 3D model teaching platform"],
        ["AR Trial Room", "Body detection + clothing overlay using MediaPipe"],
        ["Autonomous Mine Safety Car", "Obstacle detection + gas sensing vehicle"],
        ["Mental Health Chatbot", "Gemini-powered chatbot with secure data handling"],
        ["AQ Drone", "AI drone with real-time pollution mapping & purification"]
    ]

    col1, col2 = st.columns(2)

    for i, (title, desc) in enumerate(projects):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.subheader(f"🚀 {title}")
            st.write(desc)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<a class="btn" href="https://github.com/HarikrishnanAlakesan" target="_blank">🌐 View All on GitHub</a>', unsafe_allow_html=True)

# ---- RESUME ----
elif page == "📜 Resume":
    st.header("📜 Resume Highlights")
    st.markdown("### 🎓 Education")
    st.write("**B.Tech - Computer and Communication Engineering**, SMVEC (2022–2026) | CGPA: 8.64")

    st.markdown("### 🏆 Achievements")
    st.write("- 🥈 Runner-Up: Future Tech AI Hackathon – ₹13,000")
    st.write("- 🥇 Winner: PTU Paper Presentation – ₹1,400")
    st.write("- 🌍 Top 15: Google Gen AI Hackathon")
    st.write("- 🚁 Top 25: Buzz on Earth Hackathon (IIT Kanpur)")

    st.markdown("### 💼 Internships")
    st.write("- AICTE x Google Internship")
    st.write("- ML Intern at InternPe")

    st.markdown("### 🧠 Soft Skills")
    st.write("Leadership • Problem Solving • Adaptability • Communication")

    st.markdown("### 🧩 Fun Extras")
    st.write("- 🏀 Basketball player (2011–2019)")
    st.write("- 📚 Author of 2 books on Kindle")
    st.write("- 📱 App published on Amazon Store")

# ---- CONTACT ----
elif page == "📬 Contact":
    st.header("📬 Contact Me")
    st.write("Interested in working together or just want to say hi?")
    st.markdown("- 📧 Email: `mailhkris@gmail.com`")
    st.markdown("- 📞 Phone: `+91-9344779755`")
    st.markdown("- 💼 [LinkedIn](https://linkedin.com/in/harikrishnanalakesan)")
    st.markdown("- 🐙 [GitHub](https://github.com/HarikrishnanAlakesan)")
