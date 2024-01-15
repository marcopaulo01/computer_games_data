# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:55:55 2024

@author: Marco
"""

import pandas as pd


"""
Data Exploration
"""
data = pd.read_csv("https://raw.githubusercontent.com/marcopaulo01/computer_games_data/main/computer_games.csv")
print(data.columns.values)
print(data.shape)
print(data.describe())
print(data.dtypes) 
print(data.head(5))


"""
Data Cleaning
"""
print(data.isnull().sum())

genres = data['Genre'].str.split(', ')
individual_genre = []
for entry in genres:
    individual_genre.extend(entry)
for i in range(len(individual_genre)):
    if individual_genre[i].lower() == "rts":
        individual_genre[i] = "real-time strategy"
for i in range(len(individual_genre)):
    if individual_genre[i].lower() == "action-adventure":
        individual_genre[i] = "adventure"
for i in range(len(individual_genre)):
    if individual_genre[i].lower() == "rpg" or individual_genre[i].lower() == "action role-playing" or individual_genre[i].lower() == "action rpg":
        individual_genre[i] = "role-playing"
for i in range(len(individual_genre)):
    if individual_genre[i].lower() == "life simulation":
        individual_genre[i] = "simulation"
individual_genre = [genre.lower() for genre in individual_genre]
genre = pd.DataFrame({'Genre':individual_genre}).value_counts().reset_index(name='Count')

operating_system = data['Operating System'].str.split(', ')
individual_os = []
for entry in operating_system:
    individual_os.extend(entry)
individual_os = [os.lower() for os in individual_os]
os = pd.DataFrame({'OS':individual_os}).value_counts().reset_index(name='Count')


year_released  =  data['Date Released'].str[-4:]
release = pd.DataFrame({'Year Released':year_released}).value_counts().reset_index(name='Count')

producers = data['Producer'].str.split(', ')
individual_producer = []
for entry in producers:
    individual_producer.extend(entry)
producer = pd.DataFrame({'Producer':individual_producer}).value_counts().reset_index(name='Count')


"""
Data Visualization
"""
import matplotlib.pyplot as plt
top_genre = genre.head(20).sort_values(by='Count', ascending=True)
plt.figure()
top_genre.plot(kind='barh', color='skyblue', y='Count', x='Genre')
plt.xlabel('Counts')
plt.ylabel('Genres')
plt.title('Top 20 Genres')
plt.show()

top_os = os.head(5).sort_values(by='Count', ascending=True)
plt.figure()
top_os.plot(kind='barh', color='skyblue', y='Count', x='OS')
plt.xlabel('Counts')
plt.ylabel('OS')
plt.title('Top 5 Operating System')
plt.show()

top_release = release.head(10).sort_values(by='Count', ascending=True)
plt.figure()
top_release.plot(kind='barh', color='skyblue', y='Count', x='Year Released')
plt.xlabel('Counts')
plt.ylabel('Year')
plt.title('Top 10 Years Released')
plt.show()

top_producer = producer.head(10).sort_values(by='Count', ascending=True)
plt.figure()
top_producer.plot(kind='barh', color='skyblue', y='Count', x='Producer')
plt.xlabel('Counts')
plt.ylabel('Producer')
plt.title('Top 10 Producers')
plt.show()