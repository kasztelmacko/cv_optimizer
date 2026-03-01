from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PERSONAL_EXPERIENCE_PATH = PROJECT_ROOT / "context" / "personal_experience.json"

TEMPLATE_PATH = PROJECT_ROOT / "context" / "current_cv.tex"
OUTPUT_DIR = PROJECT_ROOT / "output_cv"
MODEL = "gemini/gemini-3-flash-preview"

#########################################################
ROLE_NAME = "Data Scientist"
COMPANY_NAME = "Tabby"
JOB_DESCRIPTION = """Department: Risk B2C

Employment Type: Full Time

Location: Remote

Reporting To: Mikhail Gritskikh

Description

Tabby creates financial freedom in the way people shop, earn and save by reshaping their relationship with money. Over 15 million users choose Tabby to stay in control of their spending and make the most out of their money.

The company’s flagship offering allows shoppers to split their payments online and in-store with no interest or fees. Over 40,000 global brands and small businesses, including Amazon, Noon, IKEA, and SHEIN use Tabby to accelerate growth and gain loyal customers by offering easy and flexible payments online and in stores.

Tabby generates over $10 billion in annual transaction volume for its partner brands and is the highest-rated, most-reviewed, largest, and fastest-growing FinTech in the GCC region.

Tabby launched in 2019 and has since raised +$1 billion in equity and debt funding from global and regional investors, and is now valued at $4.5 billion.

We are seeking a highly skilled and motivated Data Scientist to join our Data Science stream in the Risk Department. In this role, you will work on both operational model lifecycle tasks and next-generation ML initiatives, including hybrid modeling, behavioral modeling, and automation of our ML workflows. You’ll work in a dynamic and fast-paced environment, contributing to projects that directly impact our risk decisioning capabilities and future ML stack.

Key Responsibilities:

    Design, develop, and maintain risk models using advanced machine learning techniques, including hybrid and sequential approaches.
    Regularly retrain, monitor, and validate existing models to ensure timely adaptation to changing customer behavior.
    Build and manage scalable data marts in BigQuery to support model development and analytical needs.
    Contribute to development of internal automation tools (e.g., AutoML components, ML workflows).
    Provide data-driven insights through ad-hoc analyses to support product, credit, and operations teams.
    Participate in early research and prototyping of new architectures (Transformers, foundation-style embeddings, multimodal models).


What you’ll bring:

    At least 2 years of experience in roles such as Data Scientist, ML Engineer, or Risk Analyst, with a proven track record of impactful contributions in credit scoring.
    Proficiency in Python and experience with key data science and machine learning libraries (e.g., NumPy, Pandas, scikit-learn, CatBoost, XGBoost, LightGBM).
    Strong knowledge of PyTorch, with the ability to implement and fine-tune complex machine learning models.
    Advanced knowledge of SQL, with the ability to work effectively with large datasets.
    Experience in building and deploying end-to-end machine learning solutions that drive measurable business impact.
    Hands-on experience with tools like Airflow and Docker for deploying machine learning models into production.
    Fluency in English
    Familiarity with cloud platforms such as AWS, Google Cloud Platform (GCP), or Microsoft Azure for scalable data analysis and model deployment.
    Proficiency in visualization tools like Tableau or Power BI to effectively communicate insights and support decision-making.
    Prior experience working with financial datasets and a strong understanding of risk management principles.
"""
