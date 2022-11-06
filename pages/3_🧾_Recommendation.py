from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pandas as pd
import numpy as np

# Importing the dataset
df = pd.read_csv(r"data_files\recommender.csv")

# Elements in the webiste

st.title("Recommendation")  # Title of the site

# Creating name , age and categories boxes
# What we can do is either recommend via
# age
# vote
# award
# minimum player
# maximum player

columns = {"minage": "Minimum Age",
           "totalvotes": "Total Votes",
           "minplayers": "Minimum Players",
           "maxplayers": "Maximum Players"}
name, age = st.columns(2)
with name:
    name_to_display = df[df['usersrated'] > 250].name.values
    name = st.selectbox("Name", name_to_display)

    st.write(name)
with age:
    recommendation_category = st.selectbox(
        'Recommendation', columns.values())
    st.write(recommendation_category)


# Filtering out the dataframe with user rating > 200
filtered_rating = df[df['usersrated'] > 100]

# Creating the pivote table for recommendation based on the columns we have created on line 21
col_values = list(columns.values())
col_keys = list(columns.keys())
pt = filtered_rating.pivot_table(
    index='name', columns=col_keys[col_values.index(recommendation_category)], values='usersrated').fillna(0)


# Inititating the module
similarity_scores = cosine_similarity(pt)


def recommend(game_name):
    # index fetch
    game_names = []
    index = np.where(pt.index == game_name)[0][0]
    similar_items = sorted(list(
        enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:11]
    for i in similar_items:
        game_names.append(pt.index[i[0]])
    return game_names


name = recommend(name)

columns = ['yearpublished', "name", 'minage', "minplayers",
           "maxplayers", "totalvotes", "boardgamecategory"]

# Showing the recommendation
recommended_games = df[df['name'].isin(name)][columns].rename(
    columns={'yearpublished': "Year Published",
             "name": "Name",
             "minage": "Minimum Age",
             "totalvotes": "Total Votes",
             "boardgamecategory": "Category",
             "minplayers": "Minimum Players",
             "maxplayers": "Maximum Players"}).reset_index(drop=True)
# In the above line we have filtered top 11 games habing the columns present in the column list and renaming the columns for simplicity and setting year published to the index
#recommended_games = st.dataframe(data=recommended_games)
st.write(recommended_games, use_container_width=True)
