# Website Traffic Database

## 📌 Project Overview

This project was for our Intro to Data Engineering course in Spring 25'. This solution designs and implements relational databases to analyze and manage website traffic for four hotel websites: **Four Seasons, Hilton, Marriott, and Shangri-La**.
The goal is to provide international partners with structured data for traffic analysis, enabling insights into visitor demographics, engagement trends, and traffic sources.

## 🎯 Objectives

- Create relational schemas for website traffic analytics
- Support data retrieval, updating, and reporting
- Enable efficient storage and access of visitor and access information
- Provide Python-powered dashboards for visualization

## 📂 Project Scope

- **Captured Data:**
  - Visitor demographics (gender, country, age, age group)
  - Access data (date, session duration, device, pages visited)
  - Backlink information (URLs and sources)
  - Keyword traffic types
    - Note that the few keywords which appear as both 'paid' and 'organic' were omitted for semantic clarity and data normalization
- **Excluded Data:**
  - Clicked buttons, page content, and user interactions

## 🗂️ Database Schema

**Final Schemas:**

- **Access** (session_id, visitor_id, access_date, pages_visited, session_duration, device, backlink_id, keyword_id)
- **Visitor** (visitor_id, gender, country, age, age_group)
- **Keyword** (keyword_id, traffic_type, keyword)
- **Backlink** (backlink_id, backlink_url, source_url)

> ER diagrams and schema diagrams are available in the `/docs` folder.

## ⚙️ Data Population

- **Real data** for keywords and backlinks sourced from web analytics platforms
- **Synthetic data** generated with Python scripts for confidential visitor and access data
- **Data Generation Scripts**: Located in `/data_population_scripts/` directory
  - Uses only Python standard library (`random`, `datetime`)
  - Generates realistic data distributions based on actual analytics
  - Outputs SQL INSERT statements for database population

## ❓ Query Examples

SQL queries developed for international partners include:

- Percentage of traffic per keyword
- Bounce rate analysis per month
- Average session duration (HH:MM:SS)
- Visitor demographics by gender, age group, and country
- Device usage breakdown
- Monthly traffic and engagement trends

## 📊 Data Visualization

A Python-based dashboard was built using:

- **Libraries**: Pandas, Matplotlib, Seaborn, Psycopg2
- **Features**: Hotel selection filter, interactive charts, comprehensive analytics
- **Insights**: Visitor demographics, device usage, country-wise distribution, keyword traffic, backlink sources, engagement trends
- **Notebooks**:
  - `notebooks/Visualizations.ipynb` - Main visualization dashboard
  - `Team-3-Project-Files/Team3.ipynb` - Alternative implementation

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7+
- PostgreSQL database
- Jupyter Notebook (optional, for running visualization notebooks)

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Website-Traffic-Database
   ```
2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Set up PostgreSQL database:**

   - Create a database named `class_project`
   - Run the schema from `sql/schema.sql`
   - Populate with data from `sql/data_inserts.sql`
4. **Configure database connection:**

   - Update database settings in the Jupyter notebooks:

   ```python
   DB_SETTINGS = {
       'dbname': 'class_project',
       'user': 'your_username',
       'password': 'your_password',
       'host': 'localhost',
       'port': '5432'
   }
   ```

### Running the Project

1. **Generate new data (optional):**

   ```bash
   cd data_population_scripts
   python generate_fourseasons_sql.py
   python generate_hilton_sql.py
   python generate_marriott_sql.py
   python shangri_generate_data.py
   ```
2. **Run visualizations:**

   ```bash
   jupyter notebook notebooks/Visualizations.ipynb
   ```

## 🗂️ Project Structure

```
Website-Traffic-Database/
├── data_population_scripts/          # Python scripts for generating synthetic data
│   ├── generate_fourseasons_sql.py   # Four Seasons data generation
│   ├── generate_hilton_sql.py        # Hilton data generation
│   ├── generate_marriott_sql.py      # Marriott data generation
│   └── shangri_generate_data.py      # Shangri-La data generation
├── sql/                              # Database schema and data
│   ├── schema.sql                    # Database schema definitions
│   ├── data_inserts.sql             # Combined data insert statements
│   ├── queries.sql                  # Sample queries
│   └── uncombined_generated_inserts/ # Individual hotel data files
├── notebooks/                        # Jupyter notebooks for visualization
│   └── Visualizations.ipynb         # Main visualization dashboard
├── docs/                            # Project documentation
│   └── Project Report.pdf           # Detailed project report
├── Team-3-Project-Files/           # Alternative project files
│   ├── Team3.ipynb                 # Alternative visualization notebook
│   ├── Team-3-DDL.sql              # Alternative schema
│   └── Data Population Scripts/    # Alternative data generation scripts
├── requirements.txt                 # Python dependencies
└── README.md                       # This file
```

## 🛠️ Tools & Technologies

- **Database**: PostgreSQL
- **Languages**: SQL, Python
- **Data Generation**: Python Standard Library (random, datetime)
- **Visualization**: Pandas, Matplotlib, Seaborn, Jupyter Notebook
- **Database Connectivity**: Psycopg2, SQLAlchemy (optional)

## 📈 Key Features

### Data Generation Scripts

- **Realistic Distributions**: Based on actual web analytics data
- **Configurable Parameters**: Session durations, bounce rates, device preferences
- **SQL Injection Prevention**: Proper string escaping in generated SQL
- **No External Dependencies**: Uses only Python standard library

### Visualization Dashboard

- **Multi-Hotel Analysis**: Compare metrics across all four hotels
- **Comprehensive Metrics**: 13 different analytical views
- **Interactive Charts**: Bar charts and line plots for trend analysis
- **Real-time Database Connection**: Live data from PostgreSQL

## 🤝 Team & Collaboration

- Worked with international partners from SQU
- Overcame challenges with data confidentiality by simulating realistic datasets
- Coordinated across time zones to align project goals

## 📝 Key Insights

This project strengthened skills in:

- Database design & normalization
- SQL queries for analytics
- Data generation & visualization with Python
- Collaborative teamwork with international partners
- Real-world web analytics data modeling

## 🔧 Troubleshooting

### Common Issues

1. **Database Connection Errors:**

   - Verify PostgreSQL is running
   - Check database credentials in notebook settings
   - Ensure database `class_project` exists
2. **Missing Dependencies:**

   - Run `pip install -r requirements.txt`
   - For psycopg2 issues, try `pip install psycopg2-binary`
3. **Jupyter Notebook Issues:**

   - Ensure Jupyter is installed: `pip install jupyter`
   - Start notebook server: `jupyter notebook`

---

## 📊 Sample Analytics

The visualization dashboard provides insights into:

1. **Keyword Traffic Distribution** - Organic vs Paid traffic percentages
2. **Monthly Bounce Rates** - Seasonal trends in user engagement
3. **Session Duration Analysis** - Average time spent per visit
4. **Pages Per Visit** - Content engagement metrics
5. **Visitor Demographics** - Gender, age group, and country distributions
6. **Device Usage Patterns** - Mobile vs Desktop preferences
7. **Monthly Traffic Trends** - Seasonal patterns and growth
8. **Engagement Metrics** - Pages visited and session duration trends

Each metric is analyzed across all four hotel websites for comprehensive comparative insights.
