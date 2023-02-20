#!/usr/bin/env python

import mysql.connector, sys

# Connect to the whitlist database SQL
conn = mysql.connector.connect(host="YOUR HOST",
                               user="YOUR USER", password="YOUR PASSWD", 
                               database="whitelist")

# Create a cursor
cur = conn.cursor()

# Create "whitelist" table
cur.execute("""
CREATE TABLE IF NOT EXISTS whitelist (
  name VARCHAR(255) NOT NULL,
  phone_number VARCHAR(255) NOT NULL
);
""")

# Inserting data into the "whitelist" table
cur.execute("""
INSERT INTO whitelist (name, phone_number)
VALUES 
  ('name', '+33600000000'),
  ('name1', '+33600000000'),
  ('name2', '+33600000000'),
  ('name3', '+33600000000'),
""")

# Save changes
conn.commit()