import random
import datetime

# Helper function to generate random session durations around the average of 00:02:23 (143 seconds)
def generate_session_duration():
    base_duration = 143  # 00:02:23 in seconds
    variance = random.randint(-20, 20)  # Slight variation to simulate realistic session times
    total_seconds = base_duration + variance
    return str(datetime.timedelta(seconds=total_seconds))

# Helper function to generate random pages visited (average of 4.43 pages per visit)
def generate_pages_visited():
    if random.random() < 0.4033:  # 40.33% chance to have 1 page (bounce)
        return 1
    else:
        return random.choices([2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[0.08, 0.12, 0.15, 0.16, 0.14, 0.12, 0.08, 0.07, 0.06])[0]

# Helper function to generate random dates between December 2024 and February 2025
def generate_random_date():
    start_date = datetime.date(2024, 12, 1)
    end_date = datetime.date(2025, 2, 28)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + datetime.timedelta(days=random_days)
    return random_date

# Helper function to generate random visitor data
def generate_visitor_data(visitor_data):
    return random.choice(visitor_data)

# Helper function to pick a random device (Mobile or Desktop)
def generate_device():
    return 'Mobile' if random.random() < 0.6943 else 'Desktop'


# Keyword data extracted from Top 5 countries utilizing onlineseranking
organic_keywords = [
    'hong kong shangri la',
    'hk island hotel',
    'shangri la',
    'shangri la hong kong',
    'shangri la hotels and resorts',
    'the shard hotel',
    'shangri la london',
    'shangri la the shard',
    'shard hotel',
    'london hotel the shard',
    'shangrila sydney hotel'
]

paid_keywords = [
    'shangri la hotel toronto',
    'shangrila hotel toronto',
    'shangri la hotel',
    'toronto luxury hotel',
    'shangri la vancouver spa',
    'shangri la singapore',
    'toronto luxury hotel downtown',
    'shangri la hotel taipei taiwan',
    'shangri la cebu',
    'shangri la at the fort manila',
    'shangri la hotels',
    'shangrila sg',
    'shangri la sydney hotel',
    'island shangri la hong kong',
    'shangri la fiji',
    'rasa sayang penang',
    'shangri-la orchard singapore',
    'singapore shangri la',
    'shangri-la rasa sayang',
    'edsa shangri-la manila',
    'jen hotel penang',
    'shangri la sydney',
    'shangri la kl',
    'bangkok hotels 5 star',
    'family staycation singapore',
    'harbin hotel china',
    'shangrila surabaya',
    'shangrila the fort',
    'shangri la hotel hangzhou',
    'best hotel in hangzhou china',
    'shangri la boracay',
    'shangri-la boracay',
    'kowloon shangri-la hong kong',
    'shangri la kuala lumpur',
    'hotel on boracay',
    'shangri la boracay resort & spa boracay philippines',
    'shangri sydney',
    'hotel shangri la kuala lumpur'
]

backlinks = [
    ("https://www.businesssitedirectory.com/", "https://www.shangri-la.com/"),
    ("https://mangaloreblogs.com/places-of-interest-in-mangalore/", "https://www.shangri-la.com/en/kualalumpur/traders/"),
    ("https://front.factmagazines.com/", "https://www.shangri-la.com/dubai/shangrila/offer-detail/dining/chinese-new-year-at-shang-palace/"),
    ("https://www.businessmenupage.com/", "https://www.shangri-la.com/"),
    ("https://www.theasianbanker.com/", "https://www.shangri-la.com/manila/shangrilaatthefort/"),
    ("https://indodefence.com/", "http://www.shangri-la.com/reservations/booking/en/index.aspx"),
    ("https://www.businesssitebook.com/", "https://www.shangri-la.com/"),
    ("https://www.virginaustralia.com/au/en/", "https://www.shangri-la.com/"),
    ("http://cc.114chn.com/", "http://www.shangri-la.com/cn/property/changchun/shangrila"),
    ("https://www.businessmenubook.com/", "https://www.shangri-la.com/"),
    ("http://i7q.cn/69jUz3", "http://www.shangri-la.com/reservations/booking/sc/index.aspx"),
    ("http://www.kerryparkside.com/", "http://www.shangri-la.com/cn/shanghai/kerryhotelpudong/"),
    ("https://confinement24.org.au/", "https://www.shangri-la.com/en/cairns/shangrila/"),
    ("https://pmi2024.svell.cn/", "http://www.shangri-la.com/reservations/booking/sc/index.aspx"),
    ("https://aseangaming.com/", "https://www.shangri-la.com/manila/shangrilaatthefort/about/map-directions/"),
    ("https://www.businessmenudirectory.com/", "https://www.shangri-la.com/"),
    ("https://www.businessmenuguide.com/", "https://www.shangri-la.com/"),
    ("https://www.insurtechinsights.com/asia/register/", "http://www.shangri-la.com/reservations/booking/en/index.aspx"),
    ("https://www.spiceseries.com/ssa", "https://www.shangri-la.com/en/colombo/shangrila/"),
    ("https://en.wikivoyage.org/wiki/London", "http://www.shangri-la.com/london/shangrila/about/")
]

# Generating 1,000 visitors (with gender, age, country distribution)
visitor_data = []
genders = ['Male', 'Female']
countries = ['Philippines', 'Australia', 'Hong Kong', 'United States', 'Malaysia', 'Other']
age_groups = [
    (18, 24), (25, 34), (35, 44), (45, 54), (55, 64), (65, 120)
]

# Generate 1000 visitors with the specified distribution
for i in range(1000):
    gender = random.choices(genders, [45.44, 54.56])[0]
    country = random.choices(countries, [12.85, 8.93, 8.73, 8.69, 7.86, 52.94])[0]
    age_range = random.choices(age_groups, [11.00, 25.54, 20.11, 18.75, 15.22, 9.38])[0]
    age = random.randint(age_range[0], age_range[1])
    visitor_data.append((i + 1, gender, country, age))

# Generating SQL Insert Statements for 1,000 Visitors
visitor_inserts = []
for vid, gender, country, age in visitor_data:
    visitor_inserts.append(
        f"INSERT INTO shangri_visitor (visitor_id, gender, country, age) VALUES ({vid}, '{gender}', '{country}', {age});")

# Generating SQL Insert Statements for 2,000 Access Records with Random Dates
access_inserts = []
for i in range(2000):
    visitor_id = generate_visitor_data(visitor_data)[0]
    pages_visited = generate_pages_visited()
    session_duration = generate_session_duration()
    device = generate_device()
    # Use actual unique keyword count to avoid foreign key violations
    unique_organic_count = len(set(organic_keywords))
    total_unique_keywords = len(paid_keywords) + unique_organic_count
    keyword_id = random.randint(1, total_unique_keywords)
    backlink_id = random.randint(1, len(backlinks))
    visit_date = generate_random_date()
    access_inserts.append(
        f"INSERT INTO shangri_access (visitor_id, pages_visited, session_duration, device, backlink_id, keyword_id, access_date) "
        f"VALUES ({visitor_id}, {pages_visited}, '{session_duration}', '{device}', {backlink_id}, {keyword_id}, '{visit_date}');")

# SQL Insertion for Keywords
keyword_inserts = []
for keyword in paid_keywords:
    safe_keyword = keyword.replace("'", "''")
    keyword_inserts.append(
        f"INSERT INTO shangri_keyword (traffic_type, keyword) VALUES ('Paid', '{safe_keyword}');")
for keyword in organic_keywords:
    safe_keyword = keyword.replace("'", "''")
    keyword_inserts.append(
        f"INSERT INTO shangri_keyword (traffic_type, keyword) VALUES ('Organic', '{safe_keyword}');")

# SQL Insertion for Backlinks
backlink_inserts = []
for backlink, source in backlinks:
    backlink_inserts.append(
        f"INSERT INTO shangri_backlink (backlink_url, source_url) VALUES ('{backlink}', '{source}');")
    
# Writing to a SQL file
with open('shangri_data.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(keyword_inserts + backlink_inserts + visitor_inserts + access_inserts))

print("SQL script 'shangri_data.sql' generated successfully.")