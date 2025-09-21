import random
import datetime

# Helper function to generate random session durations around the average of 00:03:59 (239 seconds)
def generate_session_duration():
    base_duration = 239  # 00:03:59 in seconds
    variance = random.randint(-30, 30)  # Slight variation to simulate realistic session times
    total_seconds = base_duration + variance
    return str(datetime.timedelta(seconds=total_seconds))

# Helper function to generate random pages visited (with 43.01% of visits being only 1 page)
def generate_pages_visited():
    if random.random() < 0.4301:  # 43.01% chance to have 1 page (bounce)
        return 1
    else:
        return random.choices([2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[0.10, 0.12, 0.14, 0.15, 0.13, 0.10, 0.07, 0.05, 0.04])[0]

# Helper function to generate random dates between December 2024 and February 2025
def generate_random_date():
    start_date = datetime.date(2024, 12, 1)
    end_date = datetime.date(2025, 2, 28)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + datetime.timedelta(days=random_days)
    return random_date

# Helper function to pick a random device (Mobile or Desktop) Mobile: 56.38% Desktop: 43.62%
def generate_device():
    return 'Mobile' if random.random() < 0.5638 else 'Desktop'

# Helper function to generate a random visitor ID
def generate_visitor_id(visitor_ids):
    return random.choice(visitor_ids)

# Keyword data extracted from Top 5 countries utilizing onlineseranking
paid_keywords = [
    "marriott", "bonvoy marriott", "marriott frenchman's cove st thomas", "marriott bonvoy points",
    "gaylord national convention center maryland", "grand lake marriott orlando", "marriott own",
    "four points by sheraton riyadh", "fairfield inn & suites by marriott harrisburg international airport",
    "hoteles bonvoy", "marriott muskoka jw", "jw starr pass marriott", "sanya marriott yalong bay",
    "marriott brussels executive apartments", "marriott annapolis", "wedding at marriott hotel",
    "marriott residence inn oxnard hotel", "marriott coolidge corner", "spg marriott",
    "marriott hotel paso robles california", "courtyard by marriott los angeles sherman oaks",
    "marriott toronto bloor yorkville", "marriott book", "hotels sydney airport",
    "tampa marriott waterstreet", "marriott reser"
]

organic_keywords = [
    "hotel", "marriott hotels", "marriott bonvoy", "hotels", "marriott fairfield inn suite",
    "springhill suites", "fairfield inn and", "marriott near me", "marriott job openings",
    "marriotts", "fairfield inn by marriott", "fairfield inn and suites", "marriott marquis new",
    "new york marriott broadway", "marriott careers", "marriott bonvoy login",
    "marriott marquis new york city", "jobs at marriott", "new york hotels",
    "residence inn by", "residence inn", "courtyard by the marriott",
    "marriott marquis houston", "new york marriott marquis", "jw marriott",
    "united airline", "gaylord texan"
]

# utilized ahrefs.com
backlink_pairs = [
    ("https://www.newsweek.com/rankings/americas-greatest-workplaces-2023-diversity", "https://www.marriott.com/"),
    ("https://hottravel.mx/", "https://www.marriott.com/"),
    ("https://stripesessions.com/", "https://www.marriott.com/en-us/hotels/sfodt-san-francisco-marriott-marquis/overview/"),
    ("https://www.fia.org/fia/events/international-futures-industry-conference", "https://www.marriott.com/en-us/hotels/pbibr-boca-raton-marriott-at-boca-center/overview/"),
    ("https://go.marriott-promotions.com/yvoc-travelvision-banner", "https://www.marriott.com/ja/meeting-event-hotels/group-reservations/your-vision-our-commitment.mi"),
    ("https://www.jumia.ug/", "https://four-points.marriott.com/?EM=DNM_FOURPOINTSKAMPALA.COM"),
    ("https://www.usfigureskating.org/event/2025-eastern-sectional-singles-and-us-pairs-final", "https://www.marriott.com/event-reservations/reservation-link.mi?app=resvlink&id=1723655349979&key=GR"),
    ("https://www.westin.pl/", "https://www.marriott.com/reservation/availability.mi?cc=XPK&propertyCode=WAWWI"),
    ("https://www.tickettailor.com/events/weloveawards/1464879", "https://www.marriott.com/event-reservations/reservation-link.mi?guestreslink2=true&id=1731529063375&"),
    ("https://www.naepcconference.org/", "https://www.marriott.com/en-us/hotels/wasgn-gaylord-national-resort-and-convention-center/overview/"),
    ("https://geoignite.ca/", "https://www.marriott.com/event-reservations/reservation-link.mi?app=resvlink&guestreslink2=true&id=1"),
    ("https://www.ader-ep.com/en/home", "https://www.marriott.com/fr/hotels/parlc-prince-de-galles-a-luxury-collection-hotel-paris/overview/"),
    ("http://www.kaisahotel.com/", "https://www.marriott.com/en-us/hotels/huzcy-courtyard-boluo/overview/"),
    ("https://www.marriott.com.cn/default.mi", "https://www.marriott.com/it/default.mi"),
    ("http://moana-surfrider.com/?EM=EM_aa_YEXT__WI_374__NAD_FM&SWAQ=94Z197", "https://www.marriott.com/en-us/hotels/hnlwi-moana-surfrider-a-westin-resort-and-spa-waikiki-beach/overview/"),
    ("https://osakastation-hotel.jp/en/", "https://www.marriott.com/default.mi"),
    ("https://narrowscenter.showare.com/eventperformances.asp?evt=250", "https://www.marriott.com/event-reservations/reservation-link.mi?id"),
    ("https://www.messe.de/de/unternehmen/selected-hotels/", "https://www.marriott.com/de/hotels/travel/hajsi-sheraton-hannover-pelikan-hotel/"),
    ("https://www.shopmarriott.com/", "https://www.marriott.com/about/terms-of-use.mi"),
    ("https://moments.marriottbonvoy.com/en-us", "https://www.marriott.com/about/terms-of-use.mi")
]

visitor_distribution = {"Male": 45.36, "Female": 54.64}

age_distribution = {
    "18-24": 8.83,
    "25-34": 24.17,
    "35-44": 20.58,
    "45-54": 21.17,
    "55-64": 16.36,
    "65+": 8.90
}

top_countries = {
    "United States": 67.50,
    "Canada": 5.23,
    "Japan": 3.42,
    "India": 2.91,
    "United Kingdom": 2.28,
    "Other": 14.04
}


# Generate visitors
visitor_ids = []
for i in range(1000):
    visitor_id = i + 1
    gender = random.choices(list(visitor_distribution.keys()), weights=visitor_distribution.values())[0]
    country = random.choices(list(top_countries.keys()), weights=top_countries.values())[0]
    age_group = random.choices(list(age_distribution.keys()), weights=age_distribution.values())[0]
    age = random.randint(int(age_group.split('-')[0]), int(age_group.split('-')[-1])) if '-' in age_group else 65
    visitor_ids.append((visitor_id, gender, country, age))  

# Generate SQL statements
def generate_sql():
    sql_statements = []
    
    for keyword in paid_keywords:
        safe_keyword = keyword.replace("'", "''")
        sql_statements.append(f"INSERT INTO marriott_keyword (traffic_type, keyword) VALUES ('Paid', '{safe_keyword}');")
    for keyword in organic_keywords:
        safe_keyword = keyword.replace("'", "''")
        sql_statements.append(f"INSERT INTO marriott_keyword (traffic_type, keyword) VALUES ('Organic', '{safe_keyword}');")
    for backlink, source in backlink_pairs:
        sql_statements.append(f"INSERT INTO marriott_backlink (backlink_url, source_url) VALUES ('{backlink}', '{source}');")
    for vid, gender, country, age in visitor_ids:
        sql_statements.append(f"INSERT INTO marriott_visitor (visitor_id, gender, country, age) VALUES ({vid}, '{gender}', '{country}', {age});")
    for _ in range(2000):
        visitor_id = generate_visitor_id(visitor_ids)[0]
        pages_visited = generate_pages_visited()
        session_duration = generate_session_duration()
        device = generate_device()
        backlink_id = random.randint(1, len(backlink_pairs))
        # Use actual unique keyword count to avoid foreign key violations
        unique_organic_count = len(set(organic_keywords))
        total_unique_keywords = len(paid_keywords) + unique_organic_count
        keyword_id = random.randint(1, total_unique_keywords)
        visit_date = generate_random_date()
        sql_statements.append(
            f"INSERT INTO marriott_access (visitor_id, pages_visited, session_duration, device, backlink_id, keyword_id, access_date)"
            f"VALUES ({visitor_id}, {pages_visited}, '{session_duration}', '{device}', {backlink_id}, {keyword_id}, '{visit_date}');")
    
    return "\n".join(sql_statements)

sql_script = generate_sql()
with open("marriott_data.sql", "w", encoding="utf-8") as file:
    file.write(sql_script)

print("SQL script 'marriott_data.sql' generated successfully.")
