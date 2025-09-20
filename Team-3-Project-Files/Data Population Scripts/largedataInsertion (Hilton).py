import random
import datetime

# Helper function to generate random session durations around the average of 00:04:21 (261 seconds)
def generate_session_duration():
    base_duration = 261  # 00:04:21 in seconds
    variance = random.randint(-30, 30)  # Slight variation to simulate realistic session times
    total_seconds = base_duration + variance
    return str(datetime.timedelta(seconds=total_seconds))


# Helper function to generate random pages visited (with 37.42% of visits being only 1 page)
def generate_pages_visited():
    # 37.42% of the sessions should have only 1 page visited (bounce rate)
    if random.random() < 0.3742:  # 37.42% chance to have 1 page (bounce)
        return 1
    else:
        # Remaining 62.58% of the sessions should have pages between 2 and 10, distributed as follows
        return random.choices([2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[0.10, 0.12, 0.14, 0.15, 0.13, 0.10, 0.07, 0.05, 0.04])[0]


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
    return 'Mobile' if random.random() < 0.616 else 'Desktop'


# Helper function to generate a random backlink ID (1 to 20 backlinks)
def generate_backlink_id():
    return random.randint(1, 20)


# Helper function to generate a random keyword ID (1 to 53 keywords)
def generate_keyword_id():
    return random.randint(1, 53)


# Generating 53 keywords (organic and paid)
keywords = [
    ('Organic', 'hilton embassy'), ('Organic', 'hilton honors'), ('Organic', 'hotel'),
    ('Organic', 'home Hilton'), ('Organic', 'hilton hotels near me'), ('Organic', 'hilton hotel near me'),
    ('Organic', 'hilton near me'), ('Organic', 'home2 suites by Hilton'), ('Organic', 'home2 suites hotel'),
    ('Organic', 'hotels'), ('Organic', 'hilton hotel'), ('Organic', 'Hilton'), ('Organic', 'hilton hotel Glasgow'),
    ('Organic', 'hilton tower of London'), ('Organic', 'hilton Newcastle'), ('Organic', 'hilton garden inn heathrow'),
    ('Organic', 'hilton London'), ('Organic', 'hilton london hotels'), ('Organic', 'hilton hotels in London'),
    ('Organic', 'hilton Toronto'), ('Organic', 'hilton doubletree Toronto'),
    ('Organic', 'hilton mississauga meadowvale'),
    ('Organic', 'hilton garden inn'), ('Organic', 'hilton fallsview'), ('Organic', 'hilton cancun'),
    ('Organic', 'hilton montreal'), ('Organic', 'hilton niagara falls hotels'),
    ('Paid', 'hotel in las vegas'), ('Paid', 'hilton'), ('Paid', 'jamaican all inclusive resorts'),
    ('Paid', 'tru hotel'), ('Paid', 'hampton inn philadelphia convention center'),
    ('Paid', 'hotels in greenville south Carolina'),
    ('Paid', 'hotels winter haven florida'),
    ('Paid', 'hotel wichita falls Texas'), ('Paid', 'cheap hotel san juan puerto rico'), ('Paid', 'doubletree hilton excel'),
    ('Paid', 'hampton by hilton York'),
    ('Paid', 'hotels on the palm'), ('Paid', 'hilton bristol airport hotel'),
    ('Paid', 'doubletree hilton newcastle airport'),
    ('Paid', 'hotel heathrow terminal 3'), ('Paid', 'hilton Wembley'),
    ('Paid', 'doubletree by hilton newcastle airport'),
    ('Paid', 'hotel at niagara falls Canada'), ('Paid', 'niagara falls hotel'), ('Paid', 'hotel downtown Toronto'),
    ('Paid', 'downtown toronto hotels near rogers centre'), ('Paid', 'hotels near the rogers center in Toronto'),
    ('Paid', 'grand oasis cancun Mexico'), ('Paid', 'metrotown hilton Burnaby'), ('Paid', 'hotel burlington Vermont'),
    ('Paid', 'huntsville hotels')
]

# Generating 1,000 visitors (with gender, age, country distribution)
visitor_ids = []
genders = ['Male', 'Female']
countries = ['United States', 'United Kingdom', 'Canada', 'Japan', 'India', 'Other']
age_groups = [
    (18, 24), (25, 34), (35, 44), (45, 54), (55, 64), (65, 120)
]

# Generate 1000 visitors with the specified distribution
for i in range(1000):
    gender = random.choices(genders, [44.75, 55.25])[0]
    country = random.choices(countries, [75.42, 3.69, 3.55, 2.81, 1.38, 13.15])[0]
    age_range = random.choices(age_groups, [8.81, 23.0, 20.92, 21.27, 16.67, 9.34])[0]
    age = random.randint(age_range[0], age_range[1])
    visitor_ids.append(i + 1)

# Generating SQL Insert Statements for 1,000 Visitors
visitor_inserts = []
for i in range(1000):
    gender = random.choices(genders, [44.75, 55.25])[0]
    country = random.choices(countries, [75.42, 3.69, 3.55, 2.81, 1.38, 13.15])[0]
    age_range = random.choices(age_groups, [8.81, 23.0, 20.92, 21.27, 16.67, 9.34])[0]
    age = random.randint(age_range[0], age_range[1])
    visitor_inserts.append(
        f"INSERT INTO hilton_visitor (gender, country, age) VALUES ('{gender}', '{country}', {age});")

# Generating SQL Insert Statements for 2,000 Access Records with Random Dates
access_inserts = []
for i in range(2000):
    visitor_id = generate_visitor_id(visitor_ids)
    pages_visited = generate_pages_visited()  # Now with bounce rate properly considered
    session_duration = generate_session_duration()
    device = generate_device()
    backlink_id = generate_backlink_id()
    keyword_id = generate_keyword_id()
    visit_date = generate_random_date()  # Random date for each access record
    access_inserts.append(
        f"INSERT INTO hilton_access (visitor_id, pages_visited, session_duration, device, backlink_id, keyword_id, access_date) "
        f"VALUES ({visitor_id}, {pages_visited}, '{session_duration}', '{device}', {backlink_id}, {keyword_id}, '{visit_date}');")

# SQL Insertion for Keywords
keyword_inserts = []
for keyword in keywords:
    keyword_inserts.append(
        f"INSERT INTO hilton_keyword (traffic_type, keyword) VALUES ('{keyword[0]}', '{keyword[1]}');")

# Writing to a SQL file
with open('data_insertion_with_dates.sql', 'w') as f:
    f.write('\n'.join(keyword_inserts + visitor_inserts + access_inserts))

print("SQL data insertion script with random dates generated successfully!")
