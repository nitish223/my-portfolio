import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Nitish Kumar Singh | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# COLOR THEME
# ============================================================

PRIMARY = "#2563EB"
SECONDARY = "#38BDF8"
BACKGROUND = "#0B1120"
SIDEBAR = "#111827"
CARD = "#1E293B"
TEXT = "#F8FAFC"
MUTED = "#94A3B8"
BORDER = "#334155"

# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background: {BACKGROUND};
        color: {TEXT};
    }}

    .main .block-container {{
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    /* SIDEBAR */

    section[data-testid="stSidebar"] {{
        background: {SIDEBAR};
        border-right: 1px solid {BORDER};
    }}

    section[data-testid="stSidebar"] h1 {{
        color: {SECONDARY} !important;
        text-align: center;
    }}

    section[data-testid="stSidebar"] p {{
        color: {MUTED};
    }}

    /* HEADINGS */

    h1 {{
        color: {TEXT} !important;
        font-weight: 800 !important;
    }}

    h2 {{
        color: {SECONDARY} !important;
    }}

    h3 {{
        color: #60A5FA !important;
    }}

    p {{
        color: {MUTED};
        line-height: 1.7;
    }}

    /* CARDS */

    .card {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 25px;
        margin: 10px 0;
        transition: 0.3s;
    }}

    .card:hover {{
        border-color: {SECONDARY};
        transform: translateY(-4px);
        box-shadow:
            0 10px 30px rgba(56,189,248,0.15);
    }}

    /* BUTTON */

    .stButton > button {{
        background: {PRIMARY};
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
    }}

    .stButton > button:hover {{
        background: {SECONDARY};
        color: {BACKGROUND};
    }}

    /* METRICS */

    div[data-testid="stMetric"] {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 15px;
        padding: 20px;
    }}

    div[data-testid="stMetricValue"] {{
        color: {SECONDARY} !important;
    }}

    /* MOBILE */

    @media (max-width: 768px) {{
        .main .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        padding:10px;
    ">
        <div style="
            width:90px;
            height:90px;
            margin:auto;
            border-radius:50%;
            background:#2563EB;
            display:flex;
            align-items:center;
            justify-content:center;
            color:white;
            font-size:28px;
            font-weight:800;
            border:3px solid #38BDF8;
            box-shadow:0 0 25px rgba(56,189,248,0.35);
        ">
            NKS
        </div>

            Nitish Kumar Singh
            fresher Data Analyst

    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

# ============================================================
# NAVIGATION
# ============================================================

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "👤 About",
        "🛠️ Skills",
        "💼 Projects",
        "🛒 E-Commerce Analysis",
        "🤖 Machine Learning",
        "📊 Power BI Dashboard",
        "🔬 EDA",
        "🐍 Python",
        "🗄️ SQL",
        "🎓 Education",
        "🏆 Certifications",
        "📄 Resume",
        "📬 Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        font-size:13px;
        color:#64748B;
    ">
        Python • SQL • ML • Power BI
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HOME
# ============================================================

def home():

    st.title("👋 Hi, I'm Nitish kumar singh")

    st.subheader("Fresher Data Analyst")

    st.write(
        "Turning data into insights, predictions, "
        "and business decisions."
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Projects", "3+")

    with col2:
        st.metric("Experience", "Practical +")

    with col3:
        st.metric("Technologies", "15+")

    with col4:
        st.metric("Focus", "Data Science")

    st.markdown("---")

    st.header("🚀 What I Do")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="card">

            <h3>📊 Data Analysis</h3>

            <p>
            Analyze, clean and transform data
            to discover useful business insights.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">

            <h3>🤖 Machine Learning</h3>

            <p>
            Build predictive models and evaluate
            machine learning performance.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="card">

            <h3>📈 Business Intelligence</h3>

            <p>
            Create dashboards and visualizations
            for data-driven decisions.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# ABOUT
# ============================================================

def about():

    st.title("👤 About Me")

    st.write(
        """
        I am an fresher Data Analyst passionate about
        using data to solve real-world business problems.

        My technical learning includes Python, SQL, Pandas,
        NumPy, Statistics, Machine Learning, Power BI and
        Data Visualization.
        """
    )

    st.markdown("---")

    st.header("🎯 Career Objective")

    st.info(
        "To build a career in Data Analyst where I can combine "
        "analytical thinking, programming and business understanding "
        "to create data-driven solutions."
    )


# ============================================================
# SKILLS
# ============================================================

def skills():

    st.title("🛠️ Skills")

    skills_data = {
        "🐍 Programming": [
            "Python",
            "SQL"
        ],

        "📊 Data Analysis": [
            "Pandas",
            "NumPy",
            "Excel"
        ],

        "📈 Visualization": [
            "Power BI",
            "Matplotlib",
            "Seaborn",
            "Plotly"
        ],

        "🤖 Machine Learning": [
            "Scikit-learn",
            "Regression",
            "Classification",
            "Clustering"
        ],

        "🔧 Tools": [
            "Jupyter",
            "Git",
            "GitHub",
            "Streamlit"
        ]
    }

    for category, skill_list in skills_data.items():

        st.subheader(category)

        cols = st.columns(4)

        for i, skill in enumerate(skill_list):

            with cols[i % 4]:

                st.markdown(
                    f"""
                    <div class="card"
                         style="text-align:center;">
                        <h4 style="color:#38BDF8;">
                            {skill}
                        </h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ============================================================
# PROJECTS
# ============================================================

def projects():

    st.title("💼 Projects")

    search = st.text_input(
        "🔍 Search Project"
    )

    project_list = [

        {
            "name":
            "🛒 E-Commerce Sales & Customer Analysis",

            "type":
            "Data Analysis",

            "tools":
            "Python • SQL • Power BI • Excel"
        },

        {
            "name":
            "🤖 Machine Learning Prediction",

            "type":
            "Machine Learning",

            "tools":
            "Python • Pandas • Scikit-learn"
        },

        {
            "name":
            "📊 Sales Performance Dashboard",

            "type":
            "Business Intelligence",

            "tools":
            "Power BI • Excel • SQL"
        }
    ]

    for project in project_list:

        if (
            search.lower()
            in project["name"].lower()
        ):

            st.markdown(
                f"""
                <div class="card">

                    <h3>
                        {project["name"]}
                    </h3>

                    <p>
                        <b>Type:</b>
                        {project["type"]}
                    </p>

                    <p>
                        <b>Technologies:</b>
                        {project["tools"]}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# E-COMMERCE
# ============================================================

def ecommerce():

    st.title(
        "🛒 E-Commerce Sales & Customer Analysis"
    )

    st.subheader("🎯 Project Objective")

    st.write(
        """
        Analyze sales, customers, products, revenue,
        profit and regional performance to identify
        actionable business insights.
        """
    )

    st.subheader("🧰 Technologies")

    st.write(
        "Python • Pandas • NumPy • SQL • Power BI • Excel"
    )

    st.markdown("---")

    st.subheader("📌 Business Questions")

    questions = [

        "What are total sales and total profit?",

        "Which products generate the highest revenue?",

        "Which categories perform best?",

        "Which regions generate the most profit?",

        "Who are the highest-value customers?",

        "Which payment methods are most common?"
    ]

    for question in questions:

        st.write(
            f"• {question}"
        )

    st.markdown("---")

    st.subheader("📊 Dataset Columns")

    st.code(
        """
Order_ID
Order_Date
Customer_ID
Customer_Name
Product
Category
Quantity
Price
Cost
Revenue
Profit
Discount
Region
City
Payment_Method
        """
    )

    st.subheader("🔄 Data Analyst Workflow")

    st.write(
        """
        Data Collection
        ↓
        Data Cleaning
        ↓
        Exploratory Data Analysis
        ↓
        SQL Analysis
        ↓
        Visualization
        ↓
        Business Insights
        ↓
        Recommendations
        """
    )


# ============================================================
# MACHINE LEARNING
# ============================================================

def machine_learning():

    st.title("🤖 Machine Learning")

    st.subheader(
        "Customer Prediction / Classification"
    )

    st.write(
        """
        End-to-end machine learning project covering
        data preprocessing, feature engineering,
        model training and evaluation.
        """
    )

    st.markdown("---")

    st.subheader("🔄 ML Workflow")

    workflow = [
        "Data Collection",
        "Data Cleaning",
        "EDA",
        "Feature Engineering",
        "Train-Test Split",
        "Model Training",
        "Model Evaluation",
        "Prediction"
    ]

    for i, step in enumerate(
        workflow,
        1
    ):

        st.write(
            f"**{i}.** {step}"
        )

    st.markdown("---")

    st.subheader("🤖 Models")

    models = [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting"
    ]

    for model in models:

        st.write(
            f"• {model}"
        )


# ============================================================
# POWER BI
# ============================================================

def powerbi():

    st.title("📊 Power BI Dashboard")

    st.subheader(
        "Sales Performance Dashboard"
    )

    st.write(
        """
        Interactive dashboard designed to monitor
        sales, revenue, profit, customers and
        regional performance.
        """
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Revenue", "₹ —")

    with col2:
        st.metric("Profit", "₹ —")

    with col3:
        st.metric("Orders", "—")

    with col4:
        st.metric("Customers", "—")

    st.markdown("---")

    st.info(
        "Add your Power BI dashboard screenshot "
        "or public embed URL here."
    )


# ============================================================
# EDA
# ============================================================

def eda():

    st.title(
        "🔬 Exploratory Data Analysis"
    )

    st.subheader(
        "EDA Process"
    )

    eda_steps = [

        "Dataset Overview",

        "Missing Value Analysis",

        "Duplicate Analysis",

        "Statistical Summary",

        "Univariate Analysis",

        "Bivariate Analysis",

        "Correlation Analysis",

        "Outlier Detection",

        "Business Insights"
    ]

    for step in eda_steps:

        st.success(
            f"✓ {step}"
        )


# ============================================================
# PYTHON
# ============================================================

def python_page():

    st.title("🐍 Python")

    topics = [

        "Variables & Data Types",

        "Operators",

        "Conditions",

        "Loops",

        "Lists, Tuples, Sets, Dictionaries",

        "Functions",

        "List & Dictionary Comprehensions",

        "Exception Handling",

        "Modules",

        "File Handling",

        "OOP Basics",

        "NumPy",

        "Pandas",

        "Data Visualization"
    ]

    for topic in topics:

        st.write(
            f"• {topic}"
        )

    st.markdown("---")

    st.subheader(
        "💻 Python Example"
    )

    st.code(
        """
import pandas as pd

df = pd.read_csv("sales.csv")

summary = (
    df.groupby("Category")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(summary)
        """,
        language="python"
    )


# ============================================================
# SQL
# ============================================================

def sql():

    st.title("🗄️ SQL")

    st.subheader(
        "SQL Skills"
    )

    topics = [

        "SELECT",

        "FROM",

        "WHERE",

        "ORDER BY",

        "LIMIT",

        "GROUP BY",

        "HAVING",

        "Aggregate Functions",

        "CASE WHEN",

        "NULL Handling",

        "JOIN",

        "Subqueries",

        "CTE",

        "Window Functions"
    ]

    for topic in topics:

        st.write(
            f"• {topic}"
        )

    st.markdown("---")

    st.subheader(
        "📌 SQL Order of Execution"
    )

    st.code(
        """
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
↓
LIMIT
        """
    )

    st.subheader(
        "💻 Example Query"
    )

    st.code(
        """
SELECT
    Category,
    SUM(Revenue) AS total_revenue,
    SUM(Profit) AS total_profit
FROM ecommerce_sales
GROUP BY Category
ORDER BY total_revenue DESC;
        """,
        language="sql"
    )


# ============================================================
# EDUCATION
# ============================================================

def education():

    st.title("🎓 Education")

    st.subheader(
        "Academic Background"
    )

    st.markdown(
        """
        <div class="card">

        <h3>🎓 B.Tech in Computer Science and Engineering</h3>

        <p>
        Vivekananda Global University Jaipur,
        CGPA 7.00/10.0 and 2022 - 2026 
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader(
        "📚 Relevant Coursework"
    )

    courses = [

        "Statistics",

        "Database Management",

        "Python Programming",

        "Machine Learning",

        "Data Analysis",

        "Data Visualization"
    ]

    for course in courses:

        st.write(
            f"• {course}"
        )


# ============================================================
# CERTIFICATIONS
# ============================================================

def certifications():

    st.title("🏆 Certifications")

    certifications_list = [

        "Data Science Certification",

        "Python Certification",

        "SQL Certification",

        "Power BI Certification",

        "Machine Learning Certification"
    ]

    for certificate in certifications_list:

        st.markdown(
            f"""
            <div class="card">

                <h3>
                    🏆 {certificate}
                </h3>

                <p>
                    Add platform, date and certificate
                    verification link.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# RESUME
# ============================================================

def resume():

    st.title("📄 Resume")

    st.write(
        "Download my latest Data Analyst resume."
    )

    st.info(
        "Place your resume inside:"
    )

    st.code(
        "assets/resume.pdf"
    )

    try:

        with open(
            "assets/resume.pdf",
            "rb"
        ) as file:

            st.download_button(
                label="⬇️ Download Resume",
                data=file,
                file_name=
                "Nitish_Kumar_Singh_Data_Analyst_Resume.pdf",
                mime="application/pdf"
            )

    except FileNotFoundError:

        st.warning(
            "Resume file not found."
        )


# ============================================================
# CONTACT
# ============================================================

def contact():

    st.title("📬 Contact")

    st.write(
        """
        Interested in working together?
        Feel free to connect with me.
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Your Name"
        )

        email = st.text_input(
            "Your Email"
        )

    with col2:

        subject = st.text_input(
            "Subject"
        )

    message = st.text_area(
        "Message",
        height=150
    )

    if st.button(
        "📨 Send Message"
    ):

        if (
            name
            and email
            and message
        ):

            st.success(
                "Thank you! Your message has been prepared."
            )

        else:

            st.error(
                "Please complete all required fields."
            )

    st.markdown("---")

    st.subheader(
        "🔗 Professional Links"
    )

    st.write(
        "💻 GitHub: https://github.com/nitish223"
    )

    st.write(
        "💼 LinkedIn: https://www.linkedin.com/in/nitish-kumar-singh-756b7b281/"
    )

    st.write(
        "📧 Email: nitishpiprahi2@gmail.com"
    )


# ============================================================
# PAGE ROUTER
# ============================================================

if page == "🏠 Home":

    home()

elif page == "👤 About":

    about()

elif page == "🛠️ Skills":

    skills()

elif page == "💼 Projects":

    projects()

elif page == "🛒 E-Commerce Analysis":

    ecommerce()

elif page == "🤖 Machine Learning":

    machine_learning()

elif page == "📊 Power BI Dashboard":

    powerbi()

elif page == "🔬 EDA":

    eda()

elif page == "🐍 Python":

    python_page()

elif page == "🗄️ SQL":

    sql()

elif page == "🎓 Education":

    education()

elif page == "🏆 Certifications":

    certifications()

elif page == "📄 Resume":

    resume()

elif page == "📬 Contact":

    contact()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div style="
        text-align:center;
        padding:30px;
        margin-top:50px;
        border-top:1px solid #334155;
        color:#64748B;
    ">

            Nitish kumar singh | Data Analyst

            Python • SQL • Statistics • Machine Learning
            • Power BI • Data Analytics

            Built with Streamlit

    </div>
    """,
    unsafe_allow_html=True
)