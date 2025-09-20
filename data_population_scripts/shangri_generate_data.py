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

# Helper function to pick a random visitor from the generated visitor IDs
def generate_visitor_id(visitor_ids):
    return random.choice(visitor_ids)

# Helper function to pick a random device (Mobile or Desktop)
def generate_device():
    return 'Mobile' if random.random() < 0.6943 else 'Desktop'

# Helper function to generate a random backlink ID (1 to 20 backlinks)
def generate_backlink_id():
    return random.randint(1, 20)

# Helper function to generate a random keyword ID (1 to 49 keywords)
def generate_keyword_id():
    return random.randint(1, 49)

# Generating 49 keywords (organic and paid)

keywords = [
    ('Organic', 'hong kong shangri la'),
    ('Organic', 'hk island hotel'),
    ('Organic', 'shangri la'),
    ('Organic', 'shangri la hong kong'),
    ('Organic', 'shangri la hotels and resorts'),
    ('Organic', 'the shard hotel'),
    ('Organic', 'shangri la london'),
    ('Organic', 'shangri la the shard'),
    ('Organic', 'shard hotel'),
    ('Organic', 'london hotel the shard'),
    ('Organic', 'shangrila sydney hotel'),
    ('Paid', 'shangri la hotel toronto'),
    ('Paid', 'shangrila hotel toronto'),
    ('Paid', 'shangri la hotel'),
    ('Paid', 'toronto luxury hotel'),
    ('Paid', 'shangri la vancouver spa'),
    ('Paid', 'shangri la singapore'),
    ('Paid', 'toronto luxury hotel downtown'),
    ('Paid', 'shangri la hotel taipei taiwan'),
    ('Paid', 'shangri la cebu'),
    ('Paid', 'shangri la at the fort manila'),
    ('Paid', 'shangri la hotels'),
    ('Paid', 'shangrila sg'),
    ('Paid', 'shangri la sydney hotel'),
    ('Paid', 'island shangri la hong kong'),
    ('Paid', 'shangri la fiji'),
    ('Paid', 'rasa sayang penang'),
    ('Paid', 'shangri-la orchard singapore'),
    ('Paid', 'singapore shangri la'),
    ('Paid', 'shangri-la rasa sayang'),
    ('Paid', 'edsa shangri-la manila'),
    ('Paid', 'jen hotel penang'),
    ('Paid', 'shangri la sydney'),
    ('Paid', 'shangri la kl'),
    ('Paid', 'bangkok hotels 5 star'),
    ('Paid', 'family staycation singapore'),
    ('Paid', 'harbin hotel china'),
    ('Paid', 'shangrila surabaya'),
    ('Paid', 'shangrila the fort'),
    ('Paid', 'shangri la hotel hangzhou'),
    ('Paid', 'best hotel in hangzhou china'),
    ('Paid', 'shangri la boracay'),
    ('Paid', 'shangri-la boracay'),
    ('Paid', 'kowloon shangri-la hong kong'),
    ('Paid', 'shangri la kuala lumpur'),
    ('Paid', 'hotel on boracay'),
    ('Paid', 'shangri la boracay resort & spa boracay philippines'),
    ('Paid', 'shangri sydney'),
    ('Paid', 'hotel shangri la kuala lumpur')
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
visitor_ids = []
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
    visitor_ids.append(i + 1)

# Generating SQL Insert Statements for 1,000 Visitors
visitor_inserts = []
for i in range(1000):
    gender = random.choices(genders, [45.44, 54.56])[0]
    country = random.choices(countries, [12.85, 8.93, 8.73, 8.69, 7.86, 52.94])[0]
    age_range = random.choices(age_groups, [11.00, 25.54, 20.11, 18.75, 15.22, 9.38])[0]
    age = random.randint(age_range[0], age_range[1])
    visitor_inserts.append(
        f"INSERT INTO shangri_visitor (gender, country, age) VALUES ('{gender}', '{country}', {age});")

# Generating SQL Insert Statements for 2,000 Access Records with Random Dates
access_inserts = []
for i in range(2000):
    visitor_id = generate_visitor_id(visitor_ids)
    pages_visited = generate_pages_visited()
    session_duration = generate_session_duration()
    device = generate_device()
    backlink_id = generate_backlink_id()
    keyword_id = generate_keyword_id()
    visit_date = generate_random_date()
    access_inserts.append(
        f"INSERT INTO shangri_access (visitor_id, pages_visited, session_duration, device, backlink_id, keyword_id, access_date) "
        f"VALUES ({visitor_id}, {pages_visited}, '{session_duration}', '{device}', {backlink_id}, {keyword_id}, '{visit_date}');")

# SQL Insertion for Keywords
keyword_inserts = []
for keyword in keywords:
    keyword_inserts.append(
        f"INSERT INTO shangri_keyword (traffic_type, keyword) VALUES ('{keyword[0]}', '{keyword[1]}');")
    
    # SQL Insertion for Keywords
backlink_inserts = []
for backlink in backlinks:
    backlink_inserts.append(
        f"INSERT INTO shangri_backlink (backlink_url, source_url) VALUES ('{backlink[0]}', '{backlink[1]}');")
    
# Writing to a SQL file
with open('shangri_data_insertion.sql', 'w') as f:
    f.write('\n'.join(backlink_inserts + keyword_inserts + visitor_inserts + access_inserts))

print("SQL data insertion script for Shangri generated successfully!")