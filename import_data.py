# -*- coding: utf-8 -*-
import pandas as pd
import pymongo

# Load the dataset
file_path = "data.csv"  # Adjust the path if necessary
df = pd.read_csv(file_path)

# Connect to MongoDB
client = pymongo.MongoClient("your_mongodb_connection_string")
db = client["pharmrevise"]
collection = db["your_collection_name"]

# Insert data into MongoDB
data = df.to_dict(orient="records")  # Convert dataframe to dictionary
collection.insert_many(data)

#  Add this success message
print(f" Successfully inserted {len(df)} records into MongoDB!")

# Verify inserted records
print(f" Total records in database: {collection.count_documents({})}")
