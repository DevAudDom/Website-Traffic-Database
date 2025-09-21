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

# Helper function to generate random visitor data
def generate_visitor_data(visitor_data):
    return random.choice(visitor_data)

# Helper function to pick a random device (Mobile or Desktop) Mobile: 61.6% Desktop: 38.4%
def generate_device():
    return 'Mobile' if random.random() < 0.616 else 'Desktop'

# Keyword data extracted from Top 5 countries utilizing onlineseranking
paid_keywords = [
    "hotel in las vegas", "hilton", "jamaican all inclusive resorts", "tru hotel", 
    "hampton inn philadelphia convention center", "hotels in greenville south Carolina",
    "hotels winter haven florida", "hotel wichita falls Texas", "cheap hotel san juan puerto rico", 
    "doubletree hilton excel", "hampton by hilton York", "hotels on the palm", 
    "hilton bristol airport hotel", "doubletree hilton newcastle airport", "hotel heathrow terminal 3", 
    "hilton Wembley", "doubletree by hilton newcastle airport", "hotel at niagara falls Canada", 
    "niagara falls hotel", "hotel downtown Toronto", "downtown toronto hotels near rogers centre", 
    "hotels near the rogers center in Toronto", "grand oasis cancun Mexico", 
    "metrotown hilton Burnaby", "hotel burlington Vermont", "huntsville hotels",
    "hilton rewards", "hilton careers", "hilton conference center",
    "hilton wedding", "hilton meeting", "hilton business"
]

organic_keywords = [
    "hilton embassy", "hotel", "home Hilton", "hilton hotels near me", 
    "hilton hotel near me", "hilton near me", "home2 suites by Hilton", "home2 suites hotel",
    "hotels", "hilton hotel", "Hilton", "hilton hotel Glasgow", "hilton tower of London", 
    "hilton Newcastle", "hilton garden inn heathrow", "hilton London", "hilton london hotels", 
    "hilton hotels in London", "hilton Toronto", "hilton doubletree Toronto",
    "hilton mississauga meadowvale", "hilton garden inn", "hilton fallsview", "hilton cancun",
    "hilton montreal", "hilton niagara falls hotels", "hilton international", "hilton loyalty",
    "hilton points", "hilton vacation", "hilton conference"
]

# utilized ahrefs.com
backlink_pairs = [
('https://www.usafencing.org/', 'https://www.hilton.com/en/preferred-rates/usafencing/'),
('https://vibrantdbhcon.org/', 'https://www.hilton.com/en/attend-my-event/bnadudt-91g-f2d7d4ef-752d-4c6c-9646-37a18b77df77/'),
('https://www.newsweek.com/rankings/americas-greatest-workplaces-2023-diversity', 'https://www.hilton.com/'),
('https://www.fia.org/fia/events/international-futures-industry-conference', 'https://www.hilton.com/en/hotels/derdtdt-doubletree-deerfield-beach-boca-raton/'),
('https://www.usfigureskating.org/event/2025-eastern-sectional-singles-and-us-pairs-final', 'https://www.hilton.com/en/book/reservation/deeplink/?arrivaldate=2024-11-11&cid=OM%2CWW%2CHILTONLINK%2CEN%2CDirectLink&ctyhocn=BOSCTGI&departuredate=2024-11-17&fromId=HILTONLINKDIRECT&groupCode=902'),
('https://www.editions.dev/', 'https://www.hilton.com/en/attend-my-event/yyzhihh-shopi-62382cfd-6971-46bd-a873-6e3e97ff8188/'),
('https://winterparty.com/', 'http://www3.hilton.com/en/index.html'),
('https://www.region7usagym.com/meets', 'https://www.hilton.com/en/book/reservation/deeplink/?arrivaldate=2024-04-18&cid=OM%2CWW%2CHILTONLINK%2CEN%2CDirectLink&ctyhocn=PHLHWHW&departuredate=2024-04-21&fromId=HILTONLINKDIRECT&groupCode=CHW900'),
('https://www.capereindeerrun.com/', 'https://www.hilton.com/en/hotels/fmycchx-hampton-suites-cape-coral-fort-myers-area-fl/'),
('https://visionforum.weebly.com/', 'https://www.hilton.com/en/hotels/dfwrhru-tru-the-colony/'),
('https://www.twelvetransfers.co.uk/destinations/london-airport-taxi-transfers/london-gatwick-taxi-transfers/', 'http://www3.hilton.com/en/hotels/united-kingdom/hilton-london-gatwick-airport-GATHITW/index.html'),
('https://onlocationexp.com/ncaa/womens-college-world-series-tickets?travel-packages', 'https://www.hilton.com/en/hotels/dcawhhh-washington-hilton/'),
('https://www.beddingconference.com/', 'https://www.hilton.com/en/book/reservation/deeplink/?arrivaldate=2024-05-10&cid=OM%2CWW%2CHILTONLINK%2CEN%2CDirectLink&ctyhocn=HHHRSHH&departuredate=2024-05-19&fromId=HILTONLINKDIRECT&groupCode=FTB'),
('https://coastguardmarathon.com/', 'https://www.hilton.com/en/hotels/ecgnchx-hampton-elizabeth-city/'),
('https://www.flughafenregion.ch/en', 'https://www.hilton.com/en/hotels/zrhhitw-hilton-zurich-airport/'),
('https://clashendurance.com/pages/miami', 'https://www.hilton.com/en/book/reservation/rooms/?arrivalDate=2025-03-24&cid=OM%2CWW%2CHILTONLINK%2Cen%2CDirectLink&ctyhocn=HSTFLHX&departureDate=2025-03-31&groupCode=CHHCET&room1NumAdults=1'),
('https://additivemanufacturingstrategies.com/', 'https://www.hilton.com/en/hotels/nyccshx-hampton-manhattan-chelsea/'),
('https://www.asta.org/', 'https://www.hilton.com/en/'),
('https://www.houseofblues.com/', 'https://www.hilton.com/en/'),
('https://l33t.agency/', 'https://www.hilton.com/en/')
]

genders = ['Male', 'Female'] # Male: 44.75% Female: 55.25%
countries = ['United States', 'United Kingdom', 'Canada', 'Japan', 'India', 'Other'] # United States: 75.42% United Kingdom: 3.69% Canada: 3.55% Japan: 2.81% India: 1.38% Other: 13.15%
age_groups = [
    (18, 24), (25, 34), (35, 44), (45, 54), (55, 64), (65, 120) # 18-24: 8.81% 25-34: 23.0% 35-44: 20.92% 45-54: 21.27% 55-64: 16.67% 65+: 9.34%
]

# Generating 1,000 visitors (with gender, age, country distribution)
visitor_data = []
for i in range(1000):
    gender = random.choices(genders, [44.75, 55.25])[0]
    country = random.choices(countries, [75.42, 3.69, 3.55, 2.81, 1.38, 13.15])[0]
    age_range = random.choices(age_groups, [8.81, 23.0, 20.92, 21.27, 16.67, 9.34])[0]
    age = random.randint(age_range[0], age_range[1])
    visitor_data.append((i + 1, gender, country, age))

# Generating SQL Insert Statements for 1,000 Visitors
visitor_inserts = []
for vid, gender, country, age in visitor_data:
    visitor_inserts.append(
        f"INSERT INTO hilton_visitor (visitor_id, gender, country, age) VALUES ({vid}, '{gender}', '{country}', {age});")

# SQL Insertion for Keywords
keyword_inserts = []
for keyword in paid_keywords:
    safe_keyword = keyword.replace("'", "''")
    keyword_inserts.append(
        f"INSERT INTO hilton_keyword (traffic_type, keyword) VALUES ('Paid', '{safe_keyword}');")
for keyword in organic_keywords:
    safe_keyword = keyword.replace("'", "''")
    keyword_inserts.append(
        f"INSERT INTO hilton_keyword (traffic_type, keyword) VALUES ('Organic', '{safe_keyword}');")
backlink_inserts = []
for backlink, source in backlink_pairs:
    backlink_inserts.append(f"INSERT INTO hilton_backlink (backlink_url, source_url) VALUES ('{backlink}', '{source}');")

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
    backlink_id = random.randint(1, len(backlink_pairs))
    visit_date = generate_random_date()  # Random date for each access record
    access_inserts.append(
        f"INSERT INTO hilton_access (visitor_id, pages_visited, session_duration, device, backlink_id, keyword_id, access_date) "
        f"VALUES ({visitor_id}, {pages_visited}, '{session_duration}', '{device}', {backlink_id}, {keyword_id}, '{visit_date}');")


# Writing to a SQL file
with open('hilton_data.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(keyword_inserts + backlink_inserts + visitor_inserts + access_inserts))

print("SQL script 'hilton_data.sql' generated successfully.")
