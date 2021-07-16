

# @BEGIN LA_AirBnB
# @in listings.csv 
# @in neighbourhoods.csv
# @in regions.csv
# @in calendar.csv



# @begin open_refine
# @in listings.csv 
# @in neighbourhoods.csv
# @in regions.csv
# @in calendar.csv
# @out listings_cleaned.csv 
# @out neighbourhoods_cleaned.csv
# @out regions_cleaned.csv
# @out calendar_cleaned.csv
# @end open_refine



# file names
db_name = 'los_angeles_airbnb.db'
listings_path_name = 'C:/Users/slim_/OneDrive/Documents/listings.csv'
neighbourhoods_path_name = 'C:/Users/slim_/OneDrive/Documents/neighbourhoods.csv'
regions_path_name = 'C:/Users/slim_/OneDrive/Documents/LA.csv'
calendar_path_name = 'C:/Users/slim_/OneDrive/Documents/calendar.csv'


# to get the column names from csvs
#import csv

#listing_columns = []
#listing_columns_str = ''

#with open('C:/Users/slim_/OneDrive/Documents/LA.csv', 'r') as f:
#    csv_reader = csv.reader(f)#, delimiter = ',')#csv.reader(f, delimiter=' ', quotechar='|')
#    listing_columns = next(csv_reader)
#
#for each in listing_columns:
#    listing_columns_str += each + ", "
#listing_columns_str = listing_columns_str[:-2]
#
#print(listing_columns_str)


# listings columns
# id, listing_url, scrape_id, last_scraped, name, description, neighborhood_overview, picture_url, host_id, host_url, host_name, host_since, host_location, host_about, host_response_time, host_response_rate, host_acceptance_rate, host_is_superhost, host_thumbnail_url, host_picture_url, host_neighbourhood, host_listings_count, host_total_listings_count, host_verifications, host_has_profile_pic, host_identity_verified, neighbourhood, neighbourhood_cleansed, neighbourhood_group_cleansed, latitude, longitude, property_type, room_type, accommodates, bathrooms, bathrooms_text, bedrooms, beds, amenities, price, minimum_nights, maximum_nights, minimum_minimum_nights, maximum_minimum_nights, minimum_maximum_nights, maximum_maximum_nights, minimum_nights_avg_ntm, maximum_nights_avg_ntm, calendar_updated, has_availability, availability_30, availability_60, availability_90, availability_365, calendar_last_scraped, number_of_reviews, number_of_reviews_ltm, number_of_reviews_l30d, first_review, last_review, review_scores_rating, review_scores_accuracy, review_scores_cleanliness, review_scores_checkin, review_scores_communication, review_scores_location, review_scores_value, license, instant_bookable, calculated_host_listings_count, calculated_host_listings_count_entire_homes, calculated_host_listings_count_private_rooms, calculated_host_listings_count_shared_rooms, reviews_per_month

# calendar columns
# listing_id, date, available, price, adjusted_price, minimum_nights, maximum_nights

# neighbourhoods columns
# neighbourhood_group, neighbourhood

# LA_times columns
# City, Region

import sqlite3
import pandas as pd
from pathlib import Path


# @begin create_database @desc create SQL database for LA AirBnB data




Path(db_name).touch()

conn = sqlite3.connect(db_name)
c = conn.cursor()

# @in listings_cleaned.csv 
# create listings table
c.execute('''CREATE TABLE listings (id, listing_url, scrape_id, last_scraped, name, description, neighborhood_overview, picture_url, host_id, host_url, host_name, host_since, host_location, host_about, host_response_time, host_response_rate, host_acceptance_rate, host_is_superhost, host_thumbnail_url, host_picture_url, host_neighbourhood, host_listings_count, host_total_listings_count, host_verifications, host_has_profile_pic, host_identity_verified, neighbourhood, neighbourhood_cleansed, neighbourhood_group_cleansed, latitude, longitude, property_type, room_type, accommodates, bathrooms, bathrooms_text, bedrooms, beds, amenities, price, minimum_nights, maximum_nights, minimum_minimum_nights, maximum_minimum_nights, minimum_maximum_nights, maximum_maximum_nights, minimum_nights_avg_ntm, maximum_nights_avg_ntm, calendar_updated, has_availability, availability_30, availability_60, availability_90, availability_365, calendar_last_scraped, number_of_reviews, number_of_reviews_ltm, number_of_reviews_l30d, first_review, last_review, review_scores_rating, review_scores_accuracy, review_scores_cleanliness, review_scores_checkin, review_scores_communication, review_scores_location, review_scores_value, license, instant_bookable, calculated_host_listings_count, calculated_host_listings_count_entire_homes, calculated_host_listings_count_private_rooms, calculated_host_listings_count_shared_rooms, reviews_per_month)''')
listings = pd.read_csv(listings_path_name)
listings.to_sql('listings', conn, if_exists='append', index = False)

# @in neighbourhoods_cleaned.csv
#create neighbourhoods table
c.execute('''CREATE TABLE neighbourhoods (neighbourhood_group, neighbourhood)''')
neighbourhoods = pd.read_csv(neighbourhoods_path_name)
neighbourhoods.to_sql('neighbourhoods', conn, if_exists='append', index = False)

# @in regions_cleaned.csv
#create regions table
c.execute('''CREATE TABLE regions (City, Region)''')
regions = pd.read_csv(regions_path_name)
regions.to_sql('regions', conn, if_exists='append', index = False)

# @in calendar_cleaned.csv
#create calendar table
c.execute('''CREATE TABLE calendar (listing_id, date, available, price, adjusted_price, minimum_nights, maximum_nights)''')
regions = pd.read_csv(calendar_path_name)
regions.to_sql('calendar', conn, if_exists='append', index = False)

# @out LA_airbnb.db
# @end create_database





# @begin SQL_query
# @in LA_airbnb.db
# @out neighbourhood_average_price
# @out neighbourhood_average_rating
# @out region_average_price
# @out region_average_rating
# @out etc
# @end SQL_query




# @out neighbourhood_average_price
# @out neighbourhood_average_rating
# @out region_average_price
# @out region_average_rating
# @out etc
# @end LA_AirBnB

