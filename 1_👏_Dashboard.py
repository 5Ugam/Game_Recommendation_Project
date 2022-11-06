import streamlit as st
import pandas as pd
import plost
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='whitegrid')

# Setting the page configuration
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# This is for css styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Creating a title
st.title("DASHBOARD")


# ROW 1st FOR SUMMERY

st.markdown("## Markdown")
col1, col2, col3 = st.columns(3)
col1.metric(label="Games", value="20000")
col2.metric("Total Awards", "20")
col3.metric("Total Blogs Published", "20")
#col4.metric("Total News Published", "10")

# ROW 2ND FOR BAR CHART AND HISTOGRAM
name_max_community = pd.read_csv(r'https://raw.githubusercontent.com/sugam21/Game_Recommendation_Project/main/data_files/name_max_community.csv')
histogram = pd.read_csv(r'https://raw.githubusercontent.com/sugam21/Game_Recommendation_Project/main/data_files/histogram.csv')

r11, r12 = st.columns((5, 5))
with r11:
    age_count_plot = pd.read_csv(r"data_files\age_countplot.csv")
    st.markdown('## BarChart')
    fig = sns.barplot(x='age', y='count', data=age_count_plot,
                      color='#D87385', width=1.2)
    plt.xticks(age_count_plot['age'], fontsize=7)
    plt.yticks([0, 1000, 2000, 3000, 4000], fontsize=7)
    plt.title("Count of age", fontsize=10)
    plt.xlabel('age', fontsize=10)
    plt.ylabel('count', fontsize=10)
    sns.despine()
    st.pyplot()
    st.write(fig)


with r12:
    st.markdown('## Donut Chart')
    donut_graph = pd.read_csv(r"data_files\pie.csv")
    explode = (0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02)
    plt.pie(x=donut_graph['Values'], labels=donut_graph['Name'],
            pctdistance=0.5, radius=0.5,
            colors=['#80489C', '#9BA17B', '#D0B8A8',
                    '#DEB6AB', '#898AA6', '#AC7D88', '#E4CDA7'],
            explode=explode)
    # Draw circle
    centre_circle = plt.Circle((0, 0), 0.35, fc='white')
    fig = plt.gcf()
    # Adding circle to pie chart
    fig.gca().add_artist(centre_circle)
    plt.title("Count of categories", fontsize=10)
    plt.tight_layout()

    st.pyplot()


# ROW 3RD FOR LINE CHART
line = pd.read_csv(r'data_files\line.csv')

st.markdown("## Line Chart")  # Setting up the title
r21, r22 = st.columns((5, 5))  # Fot the first two figures of the bar graph
r31, r32 = st.columns(2)  # For the second two figures of the bar graph
with r21:
    plost.line_chart(data=line, x='yearpublished', y='totalvotes', pan_zoom='minimap',
                     use_container_width=True, width=600, height=250,
                     title='year published vs total votes')
with r22:
    plost.line_chart(data=line, x='yearpublished', y='numwanting', pan_zoom='minimap',
                     use_container_width=True, width=600, height=250,
                     title='year published vs number of people wanting the game')
with r31:
    v1 = st.selectbox("Year Publish vs", [
                      'news', 'blogs', 'weblink', 'podcast'], index=0, key=1)
    st.write(v1)
    plost.line_chart(data=line, x='yearpublished', y=v1, pan_zoom='minimap',
                     use_container_width=True, width=600, height=250,
                     title=f'year published vs {v1}')
with r32:
    v2 = st.selectbox("Year Publish vs", [
                      'news', 'blogs', 'weblink', 'podcast'], index=1, key=2)
    st.write(v2)
    plost.line_chart(data=line, x='yearpublished', y=v2, pan_zoom='minimap',
                     use_container_width=True, width=600, height=250,
                     title=f'year published vs {v2}')

# Ploting the line graph
r51, r52 = st.columns(2)
with r51:
    plt.figure(figsize=(9, 3))
    max_community_histogram = pd.read_csv(r"data_files\histogram.csv")
    sns.distplot(x=max_community_histogram['max_community'])
    plt.xlabel("minimum age")
    st.pyplot()

with r52:
    age = pd.read_csv(r"data_files\age.csv")
    plost.line_chart(data=age, x='minage', y="totalvotes",
                     use_container_width=True, width=600, height=250,
                     title='Minimum age vs total votes')

# Plotting the bar graph
st.markdown("## Bar Graph")
r41, r42 = st.columns(2)
with r41:
    name_max_community = pd.read_csv(r"data_files\name_max_community.csv")
    plost.bar_chart(bar='name', value='max_community', data=name_max_community,
                    direction='horizontal', width=500, color="#749F82")

with r42:
    total_votes_name = pd.read_csv(
        r"data_files\name_max_community_with_total_votes.csv")
    plost.bar_chart(bar='name', value='totalvotes', data=total_votes_name,
                    direction='horizontal', width=500, color='#7D6E83')


# BArGraph
plt.figure(figsize=(15, 5))
awards = pd.read_csv(r"data_files\awards.csv")
ax = sns.barplot(x='name', y='boardgamehonor_cnt', data=awards, palette='Set3')
ax.set_xticklabels(awards['name'], rotation=90, fontsize=7)
ax.set_yticklabels(range(0, 51, 10), rotation=90, fontsize=7)
ax.set_xlabel(xlabel='Name', fontsize=7)
ax.set_ylabel('Total Award Received', fontsize=7)
st.pyplot()
