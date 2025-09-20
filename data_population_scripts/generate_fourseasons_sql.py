import random
import datetime

# Helper function to generate random session durations around the average of 00:02:00 (120 seconds)
def generate_session_duration():
    base_duration = 120  # 00:02:00 in seconds
    variance = random.randint(-30, 30)  # Slight variation to simulate realistic session times
    total_seconds = base_duration + variance
    return str(datetime.timedelta(seconds=total_seconds))

# Helper function to generate random pages visited (with 37.67%of visits being only 1 page)
def generate_pages_visited():
    if random.random() < 0.3767:  # 37.67% chance to have 1 page (bounce)
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

# Helper function to pick a random device (Mobile or Desktop) Desktop: 30.56% Mobile: 69.44% 
def generate_device():
    return 'Mobile' if random.random() < .6944 else 'Desktop'

# Helper function to generate a random visitor ID
def generate_visitor_id(visitor_ids):
    return random.choice(visitor_ids)

# Keyword data extracted from Top 5 countries utilizing onlineseranking
paid_keywords = [
    "four seasons las vegas", "four seasons resort nevis west indies", "four seasons napa", 
    "four seasons jet", "four season milano", "four seasons cairo at the first residence", 
    "four seasons milan italy", "resorts on sea of cortez", "oceans club bahamas", "four ses", 
    "four seasons orlando", "four seasons orlando florida", "four seasons sharm", 
    "langkawi malaysia hotel", "four seasons prague", "four seasons jimbaran bali", 
    "four season geneva", "fourseason hotel hong kong", "fourseason langkawi", "koh samui resort", 
    "paris four seasons hotel", "four seasons seattle", "four season surfside", "four season disney", 
    "disney four seasons orlando", "four seasons los angeles", "four seasons vegas", "4 seasons las vegas", 
    "paris hotels george v", "four seasons los angeles hotel", "four seasons taormina", "hotel milano lusso", 
    "four seasons kuda huraa", "four season in istanbul", "mauritius four seasons", 
    "luxurious resorts in maldives", "four seasons sultanahmet istanbul", "4 seasons hotel chicago", 
    "four seasons downtown new york", "four seasons landaa maldives", "four season megeve", 
    "four seasons marrakech", "grand hotel du cap ferrat", "four season london", "four season costa rica", 
    "four seasons bali hotel", "four seasons hotel london at ten trinity square", 
    "four seasons london trinity square", "four seasons trinity square"
]


organic_keywords = [ 
    "four seasons", "hotels", "bora bora", "four seasons orlando hotel", "spa", "four seasons chicago", "four seasons boston", 
    "four seasons maui", "georges v", 
    "four seasons at park lane london", "four seasons hampshire", "four seasons london", 
    "four seasons hotel london", "four season hotel",
    "four seasons toronto", "four seasons hotel toronto", 
    "hotel montreal", "four seasons montreal", "four seasons whistler", 
    "four season", "four seasons florence", "four seasons hotel firenze", 
    "four season firenze",
    "hotel four season milano",
    "four seasons hotel paris george v", "four seasons george v", "paris four seasons george v", 
    "four season paris george v", "four seasons georges v", 
    "hotel george v paris", "hotel four seasons paris", "four seasons paris"
]

# utilized ahrefs.com
backlink_pairs = [
    ("https://www.wsop.com/", "https://www.fourseasons.com/stlouis"),
    ("https://escortalligator.com.listcrawler.eu/brief/escorts/usa/california/losangeles/1", "https://fourseasons.com/losangeles"),
    ("https://en.wikipedia.org/wiki/Milan", "https://www.fourseasons.com/magazine/"),
    ("http://magazine.fourseasons.com/travel-food-style/things-to-do/personalities-perspectives/best-shopping-and-dining-around-the-world", "https://www.fourseasons.com/losangeles"),
    ("https://mandalaybay.mgmresorts.com/en.html", "https://www.fourseasons.com/lasvegas/"),
    ("https://www.mitsuifudosan.co.jp/", "https://www.fourseasons.com/jp/otemachi/"),
    ("https://www.travelandleisure.com/best-places-to-go-2025-8739580", "https://www.fourseasons.com/budapest/"),
    ("https://www.dezeen.com/2025/03/18/the-white-lotus-hotels/", "https://www.fourseasons.com/kohsamui/"),
    ("https://www.nassauparadiseisland.com/", "https://www.fourseasons.com/oceanclub/"),
    ("https://www.glamour.com/story/sarah-catherine-hook-interview", "https://www.fourseasons.com/kohsamui/"),
    ("https://www.cntraveler.com/gallery/best-hotels-in-new-orleans", "https://www.fourseasons.com/neworleans/"),
    ("https://www.newtownplaza.com.hk/zh-hant/", "https://www.fourseasons.com/hongkong/"),
    ("https://www.skyhighphiladelphia.com/", "https://www.fourseasons.com/legal/accessibility-policy/"),
    ("https://www.redroosterharlem.com/", "https://www.fourseasons.com/montreal/dining"),
    ("https://www.cntraveller.com/gallery/definitive-guide-maldives-best-hotels", "https://www.fourseasons.com/maldivesvoavah/"),
    ("https://colombia.travel/en/bogota", "https://www.fourseasons.com/es/casamedina/"),
    ("https://allthingsfrench.com/eze-french-riviera/", "https://www.fourseasons.com/capferrat/"),
    ("https://www.popsugar.com/fitness/life-time-fitness-membership-cost-49354078", "https://www.fourseasons.com/jacksonhole/"),
    ("https://isuworlds2025.com/", "https://www.fourseasons.com/onedalton/"),
    ("https://www.theknot.com/content/bachelorette-party-city-guide", "https://www.fourseasons.com/philadelphia/dining/lounges/jg-skyhigh/"),
    ("https://www.talaatmoustafa.com/ar/home-page-ar/", "https://www.fourseasons.com/alexandria/")
]

visitor_distribution = {"Male": 44.52, "Female": 55.48}

age_distribution = {
    "18-24": 11.21,
    "25-34": 25.54,
    "35-44": 19.55,
    "45-54": 17.90,
    "55-64": 16.17,
    "65+": 9.63
}

top_countries = {
    "United States": 47.90,
    "Brazil": 5.26,
    "Canada": 4.98,
    "United Kingdom": 4.27,
    "Mexico": 3.73,
    "Other": 14.04
}

device_distribution = {
    "Desktop": 30.56,
    "Mobile": 69.44
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
        sql_statements.append(f"INSERT INTO fourseasons_keyword (traffic_type, keyword) VALUES ('Paid', '{keyword}');")
    for keyword in organic_keywords:
        sql_statements.append(f"INSERT INTO fourseasons_keyword (traffic_type, keyword) VALUES ('Organic', '{keyword}');")
    for backlink, source in backlink_pairs:
        sql_statements.append(f"INSERT INTO fourseasons_backlink (backlink_url, source_url) VALUES ('{backlink}', '{source}');")
    for vid, gender, country, age in visitor_ids:
        sql_statements.append(f"INSERT INTO fourseasons_visitor (visitor_id, gender, country, age) VALUES ({vid}, '{gender}', '{country}', {age});")
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
            f"INSERT INTO fourseasons_access (visitor_id, pages_visited, session_duration, device, backlink_id, keyword_id, access_date)"
            f"VALUES ({visitor_id}, {pages_visited}, '{session_duration}', '{device}', {backlink_id}, {keyword_id}, '{visit_date}');")
    
    return "\n".join(sql_statements)

sql_script = generate_sql()
with open("fourseasons_data.sql", "w", encoding="utf-8") as file:
    file.write(sql_script)

print("SQL script 'fourseasons_data.sql' generated successfully.")
