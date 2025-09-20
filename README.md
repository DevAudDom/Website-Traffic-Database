# Website Traffic Database

## 📌 Project Overview
This project designs and implements relational databases to analyze and manage website traffic for four hotel websites: **Four Seasons, Hilton, Marriott, and Shangri-La**.  
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
- **Excluded Data:**
  - Clicked buttons, page content, and user interactions

## 🗂️ Database Schema
**Final Schemas:**
- **Access** (access_id, access_date, pages_visited, session_duration, device, visitor_id, keyword_id, backlink_id)  
- **Visitor** (visitor_id, gender, country, age, age_group)  
- **Keyword** (keyword_id, traffic_type, keyword)  
- **Backlink** (backlink_id, backlink_url, source_url)  

> ER diagrams and schema diagrams are available in the `/docs` folder.

## ⚙️ Data Population
- **Real data** for keywords and backlinks sourced from web analytics platforms  
- **Synthetic data** generated with Python scripts for confidential visitor and access data  

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
- **Libraries**: Pandas, Matplotlib, Seaborn, Tkinter  
- **Features**: Hotel selection filter, interactive charts, dark-themed UI  
- **Insights**: Visitor demographics, device usage, country-wise distribution, keyword traffic, backlink sources, engagement trends

## 🚀 Tools & Technologies
- **Database**: PostgreSQL  
- **Languages**: SQL, Python  
- **Libraries**: Pandas, Matplotlib, Seaborn, Tkinter  
- **Visualization**: Jupyter Notebook dashboard  

## 🤝 Team & Collaboration
- Worked with international partners from SQU
- Overcame challenges with data confidentiality by simulating realistic datasets
- Coordinated across time zones to align project goals

## 📝 Conclusion
This project strengthened skills in:
- Database design & normalization  
- SQL queries for analytics  
- Data generation & visualization with Python  
- Collaborative teamwork with international partners  

---
