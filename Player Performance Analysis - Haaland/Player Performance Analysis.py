#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Arc

# Function to draw a football pitch
def create_pitch():
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    # Pitch Outline & Centre Line
    plt.plot([0, 0], [0, 100], color="black")
    plt.plot([100, 100], [0, 100], color="black")
    plt.plot([0, 100], [100, 100], color="black")
    plt.plot([0, 100], [0, 0], color="black")
    plt.plot([50, 50], [0, 100], color="black")

    # Left Penalty Area
    plt.plot([16.5, 16.5], [75, 25], color="black")
    plt.plot([0, 16.5], [75, 75], color="black")
    plt.plot([16.5, 0], [25, 25], color="black")

    # Right Penalty Area
    plt.plot([83.5, 100], [75, 75], color="black")
    plt.plot([83.5, 83.5], [75, 25], color="black")
    plt.plot([83.5, 100], [25, 25], color="black")

    # Left 6-yard Box
    plt.plot([5.5, 5.5], [65, 35], color="black")
    plt.plot([0, 5.5], [65, 65], color="black")
    plt.plot([5.5, 0], [35, 35], color="black")

    # Right 6-yard Box
    plt.plot([94.5, 100], [65, 65], color="black")
    plt.plot([94.5, 94.5], [65, 35], color="black")
    plt.plot([94.5, 100], [35, 35], color="black")

    # Prepare Circles; 10 yard circle at centre and 1 yard circle at penalty spot
    centreCircle = plt.Circle((50, 50), 9.15, color="black", fill=False)
    centreSpot = plt.Circle((50, 50), 0.8, color="black")
    leftPenSpot = plt.Circle((11, 50), 0.8, color="black")
    rightPenSpot = plt.Circle((89, 50), 0.8, color="black")

    # Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    # Draw Arcs
    leftArc = Arc((11, 50), height=18.3, width=18.3, angle=0, theta1=308, theta2=52, color="black")
    rightArc = Arc((89, 50), height=18.3, width=18.3, angle=0, theta1=128, theta2=232, color="black")

    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

    return fig, ax

# Generate sample data for a striker (Haaland)
np.random.seed(0)
x = np.random.normal(loc=80, scale=10, size=300)  # More activity in the attacking third
y = np.random.normal(loc=50, scale=15, size=300)  # Centered around the goal area

# Create the pitch
fig, ax = create_pitch()

# Create the heatmap
sns.kdeplot(x, y, shade=True, shade_lowest=False, cmap='Reds', alpha=0.6, ax=ax)

# Show the plot
plt.title('Erling Haaland Heatmap')
plt.show()


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Arc

# Function to draw a football pitch
def create_pitch():
    fig, ax = plt.subplots(figsize=(12, 7))
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    # Pitch Outline & Centre Line
    plt.plot([0, 0], [0, 100], color="white")
    plt.plot([100, 100], [0, 100], color="white")
    plt.plot([0, 100], [100, 100], color="white")
    plt.plot([0, 100], [0, 0], color="white")
    plt.plot([50, 50], [0, 100], color="white")

    # Left Penalty Area
    plt.plot([16.5, 16.5], [75, 25], color="white")
    plt.plot([0, 16.5], [75, 75], color="white")
    plt.plot([16.5, 0], [25, 25], color="white")

    # Right Penalty Area
    plt.plot([83.5, 100], [75, 75], color="white")
    plt.plot([83.5, 83.5], [75, 25], color="white")
    plt.plot([83.5, 100], [25, 25], color="white")

    # Left 6-yard Box
    plt.plot([5.5, 5.5], [65, 35], color="white")
    plt.plot([0, 5.5], [65, 65], color="white")
    plt.plot([5.5, 0], [35, 35], color="white")

    # Right 6-yard Box
    plt.plot([94.5, 100], [65, 65], color="white")
    plt.plot([94.5, 94.5], [65, 35], color="white")
    plt.plot([94.5, 100], [35, 35], color="white")

    # Prepare Circles; 10 yard circle at centre and 1 yard circle at penalty spot
    centreCircle = plt.Circle((50, 50), 9.15, color="white", fill=False)
    centreSpot = plt.Circle((50, 50), 0.8, color="white")
    leftPenSpot = plt.Circle((11, 50), 0.8, color="white")
    rightPenSpot = plt.Circle((89, 50), 0.8, color="white")

    # Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    # Draw Arcs
    leftArc = Arc((11, 50), height=18.3, width=18.3, angle=0, theta1=308, theta2=52, color="white")
    rightArc = Arc((89, 50), height=18.3, width=18.3, angle=0, theta1=128, theta2=232, color="white")

    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

    return fig, ax

# Generate sample data for a striker (Haaland)
np.random.seed(0)
x = np.random.normal(loc=80, scale=10, size=300)  # More activity in the attacking third
y = np.random.normal(loc=50, scale=15, size=300)  # Centered around the goal area

# Create the pitch
fig, ax = create_pitch()

# Create the heatmap
sns.kdeplot(x, y, shade=True, shade_lowest=False, cmap='Reds', alpha=0.6, ax=ax)

# Set background color
fig.patch.set_facecolor('green')
ax.set_facecolor('green')

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')

# Show the plot
plt.title('Erling Haaland Heatmap', color='white')
plt.show()


# In[5]:


pip install highlight_text


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text
import matplotlib as mpl
from mplsoccer.pitch import Pitch


# In[7]:


#Set general use colors
text_color = 'w'


# In[8]:


data = pd.read_csv('shotmaps.csv')


# In[9]:


data


# In[65]:


import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import fig_text

# Set general use colors
text_color = 'w'

# Generate sample data points (x and y coordinates within and around the penalty box area)
data = pd.DataFrame({
    'x': [10, 12, 18, 15, 3, 7, 13, 13, 14, 16, 10, 9, 12, 17, 23, 10, 11, 18, 15, 16,
          18, 10, 11, 22, 19, 7, 5, 14, 12, 13, 11, 10, 8, 7, 6, 4],
    'y': [60, 55, 65, 38, 27, 28, 30, 31, 30, 67, 33, 41, 56, 37, 36, 49, 48, 42, 41, 44,
          39, 43, 37, 49, 46, 45, 24, 33, 25, 66, 67, 58, 47, 46, 45, 44]
})

# Create the figure
fig, ax = plt.subplots(figsize=(13, 8.5))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

# Draw the pitch
plt.plot([0, 0], [0, 80], color='w')
plt.plot([0, 120], [80, 80], color='w')
plt.plot([120, 120], [80, 0], color='w')
plt.plot([120, 0], [0, 0], color='w')

# Left penalty area
plt.plot([18, 18], [66, 14], color='w')
plt.plot([0, 18], [66, 66], color='w')
plt.plot([18, 0], [14, 14], color='w')

# Right penalty area
plt.plot([106, 106], [62, 18], color='w')
plt.plot([120, 106], [62, 62], color='w')
plt.plot([106, 120], [18, 18], color='w')

# Left 6-yard box
plt.plot([6, 6], [54, 26], color='w')
plt.plot([0, 6], [54, 54], color='w')
plt.plot([6, 0], [26, 26], color='w')

# Right 6-yard box
plt.plot([114, 114], [54, 26], color='w')
plt.plot([120, 114], [54, 54], color='w')
plt.plot([114, 120], [26, 26], color='w')

# Prepare Circles for center circle and penalty spots
center_circle = plt.Circle((60, 40), 8.1, color='w', fill=False)
center_spot = plt.Circle((60, 40), 0.71, color='w')
left_pen_spot = plt.Circle((9, 40), 0.71, color='w')
right_pen_spot = plt.Circle((111, 40), 0.71, color='w')

# Draw Circles
ax.add_patch(center_circle)
ax.add_patch(center_spot)
ax.add_patch(left_pen_spot)
ax.add_patch(right_pen_spot)

# Plot the points
plt.scatter(data['x'], data['y'], s=100, c='#ea6969', alpha=.7)

# Title text
s = 'Haaland_goal_position'
fig_text(s=s,
         x=.13, y=.10,
         fontfamily='Andale Mono',
         fontsize=21,
         color=text_color)

# Set limits and hide axes
plt.xlim(0, 120)
plt.ylim(0, 80)
plt.axis('off')

# Display the plot
plt.show()


# In[66]:


import pandas as pd

# Define the data
data = {
    "Competition": [
        "Premier League", "Bundesliga", "UEFA Champions League", "Eliteserien", 
        "Bundesliga", "First Division", "UEFA Nations League", "DFB Pokal", 
        "FA Cup", "UEFA Europa League", "WC Qualification Europe", 
        "Norwegian Football Cup", "UEFA Euro Qualifiers", "UEFA Euro U21 Championship", 
        "FIFA World Cup U20", "League Cup", "DFL Super Cup", "Community Shield", 
        "J League World Challenge", "UEFA Super Cup", "Austrian Cup", "UEFA Youth League"
    ],
    "Matches Played (MP)": [
        66, 52, 39, 39, 16, 16, 10, 7, 7, 6, 6, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1
    ],
    "Goals": [
        63, 49, 41, 14, 17, 0, 12, 8, 8, 4, 5, 1, 0, 0, 9, 1, 1, 0, 2, 0, 4, 0
    ],
    "Assists": [
        13, 13, 5, 5, 4, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0
    ],
    "PEN": [
        6, 5, 5, 3, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
    "Minutes Played (Min')": [
        5338, 4325, 3089, 1979, 1066, 422, 847, 551, 565, 411, 493, 188, 170, 215, 270, 107, 158, 154, 44, 90, 90, 30
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# In[69]:


import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Competition": [
        "Premier League", "German Bundesliga", "UEFA Champions League", "Eliteserien", 
        "Austrian Bundesliga", "First Division", "UEFA Nations League", "DFB Pokal", 
        "FA Cup", "UEFA Europa League", "WC Qualification Europe", 
        "Norwegian Football Cup", "UEFA Euro Qualifiers", "UEFA Euro U21 Championship", 
        "FIFA World Cup U20", "League Cup", "DFL Super Cup", "Community Shield", 
        "J League World Challenge", "UEFA Super Cup", "Austrian Cup", "UEFA Youth League"
    ],
    "Matches Played (MP)": [
        66, 52, 39, 39, 16, 16, 10, 7, 7, 6, 6, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1
    ],
    "Goals": [
        63, 49, 41, 14, 17, 0, 12, 8, 8, 4, 5, 1, 0, 0, 9, 1, 1, 0, 2, 0, 4, 0
    ],
    "Assists": [
        13, 13, 5, 5, 4, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0
    ],
    "PEN": [
        6, 5, 5, 3, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
    "Minutes Played (Min')": [
        5338, 4325, 3089, 1979, 1066, 422, 847, 551, 565, 411, 493, 188, 170, 215, 270, 107, 158, 154, 44, 90, 90, 30
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Plot total goals in each competition
plt.figure(figsize=(14, 8))
bars = plt.barh(df['Competition'], df['Goals'], color='skyblue')
plt.xlabel('Goals')
plt.title('Total Goals by Erling Haaland in Different Competitions')
plt.gca().invert_yaxis()  # Invert y-axis to show the top competition first

# Add text labels
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
             f'{int(bar.get_width())}', 
             va='center', ha='left', color='black')

plt.show()

# Plot total matches played in each competition
plt.figure(figsize=(14, 8))
bars = plt.barh(df['Competition'], df['Matches Played (MP)'], color='salmon')
plt.xlabel('Matches Played')
plt.title('Total Matches Played by Erling Haaland in Different Competitions')
plt.gca().invert_yaxis()  # Invert y-axis to show the top competition first

# Add text labels
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
             f'{int(bar.get_width())}', 
             va='center', ha='left', color='black')

plt.show()


# In[70]:


import pandas as pd
import matplotlib.pyplot as plt

# Define the market value data
data = {
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Market Value (mil €)": [100, 150, 170, 180, 180]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# In[75]:


import matplotlib.pyplot as plt

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the bar chart
bars = plt.bar(df['Year'], df['Market Value (mil €)'], color='mediumseagreen')

# Add title and labels
plt.suptitle('Market Value', x=0.06,ha='left', fontsize=14, style='italic')
plt.xlabel('Year', fontsize=1)
plt.ylabel('Market Value (mil €)', fontsize=14)

# Add text labels on the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'€{yval} mil.', ha='center', va='bottom', fontsize=12)

# Add the current market value label
current_value = df['Market Value (mil €)'].iloc[-1]

# Remove x and y axis lines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

# Display the plot
plt.show()


# In[76]:


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from plottable import ColumnDefinition, Table
from plottable.cmap import normed_cmap
from plottable.plots import image

# Sample Data
data = {
    "Competition": ["Premier League", "German Bundesliga", "UEFA Champions League", "Eliteserien", "Austrian Bundesliga", "First Division", "UEFA Nations League", "DFB Pokal", "FA Cup", "UEFA Europa League", "WC Qualification Europe", "Norwegian Football Cup", "UEFA Euro Qualifiers", "UEFA Euro U21 Championship", "FIFA World Cup U20", "League Cup", "DFL Super Cup", "Community Shield", "J League World Challenge", "UEFA Super Cup", "Austrian Cup", "UEFA Youth League"],
    "MP": [66, 52, 39, 39, 16, 16, 10, 7, 7, 6, 6, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1],
    "Goals": [63, 49, 41, 14, 17, 0, 12, 8, 8, 4, 5, 1, 0, 0, 9, 1, 1, 0, 2, 0, 4, 0],
    "Assists": [13, 13, 5, 5, 4, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    "PEN": [6, 5, 5, 3, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Min'": [5338, 4325, 3089, 1979, 1066, 422, 847, 551, 565, 411, 493, 188, 170, 215, 270, 107, 158, 154, 44, 90, 90, 30]
}

df = pd.DataFrame(data)

# Set up the colors
bg_color = "#FFFFFF"
text_color = "#000000"

plt.rcParams["text.color"] = text_color
plt.rcParams["font.family"] = "monospace"

# Create ColumnDefinitions for the table
col_defs = [
    ColumnDefinition(name="Competition", textprops={"ha": "left", "weight": "bold"}, width=2.75),
    ColumnDefinition(name="MP", textprops={"ha": "center"}, width=0.75),
    ColumnDefinition(name="Goals", textprops={"ha": "center", "color": "#000000", "weight": "bold", "bbox": {"boxstyle": "circle", "pad": 0.35}}, cmap=normed_cmap(df["Goals"], cmap=matplotlib.cm.PiYG, num_stds=2)),
    ColumnDefinition(name="Assists", textprops={"ha": "center", "color": "#000000", "weight": "bold", "bbox": {"boxstyle": "circle", "pad": 0.35}}, cmap=normed_cmap(df["Assists"], cmap=matplotlib.cm.PiYG_r, num_stds=2)),
    ColumnDefinition(name="PEN", textprops={"ha": "center"}, width=0.75),
    ColumnDefinition(name="Min'", textprops={"ha": "center"}, width=1.0)
]

# Create the table
fig, ax = plt.subplots(figsize=(20, 12))
fig.set_facecolor(bg_color)
ax.set_facecolor(bg_color)
table = Table(
    df,
    column_definitions=col_defs,
    index_col="Competition",
    row_dividers=True,
    row_divider_kw={"linewidth": 1, "linestyle": (0, (1, 5))},
    footer_divider=True,
    textprops={"fontsize": 14},
    col_label_divider_kw={"linewidth": 1, "linestyle": "-"},
    column_border_kw={"linewidth": .5, "linestyle": "-"},
    ax=ax,
).autoset_fontcolors(colnames=["Goals", "Assists"]) # This will set the font color of the columns based on the cmap so the text is readable

fig.show()


# In[77]:


pip install plottable


# In[80]:


import pandas as pd
import matplotlib.pyplot as plt
from plottable import ColumnDefinition, Table
from plottable.cmap import normed_cmap

# Sample Data
data = {
    "Competition": ["Premier League", "German Bundesliga", "UEFA Champions League", "Eliteserien", "Austrian Bundesliga", "First Division", "UEFA Nations League", "DFB Pokal", "FA Cup", "UEFA Europa League", "WC Qualification Europe", "Norwegian Football Cup", "UEFA Euro Qualifiers", "UEFA Euro U21 Championship", "FIFA World Cup U20", "League Cup", "DFL Super Cup", "Community Shield", "J League World Challenge", "UEFA Super Cup", "Austrian Cup", "UEFA Youth League"],
    "MP": [66, 52, 39, 39, 16, 16, 10, 7, 7, 6, 6, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1],
    "Goals": [63, 49, 41, 14, 17, 0, 12, 8, 8, 4, 5, 1, 0, 0, 9, 1, 1, 0, 2, 0, 4, 0],
    "Assists": [13, 13, 5, 5, 4, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    "PEN": [6, 5, 5, 3, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Min'": [5338, 4325, 3089, 1979, 1066, 422, 847, 551, 565, 411, 493, 188, 170, 215, 270, 107, 158, 154, 44, 90, 90, 30]
}

df = pd.DataFrame(data)
df.insert(0, 'S.no', range(1, 1 + len(df)))

# Set up the colors
bg_color = "#FFFFFF"
text_color = "#000000"

plt.rcParams["text.color"] = text_color
plt.rcParams["font.family"] = "monospace"

# Create ColumnDefinitions for the table
col_defs = [
    ColumnDefinition(name="S.no", textprops={"ha": "center"}, width=0.5),
    ColumnDefinition(name="Competition", textprops={"ha": "left", "weight": "bold"}, width=2.75),
    ColumnDefinition(name="MP", textprops={"ha": "center"}, width=0.75),
    ColumnDefinition(name="Goals", textprops={"ha": "center", "color": "#000000", "weight": "bold", "bbox": {"boxstyle": "circle", "pad": 0.35}}, cmap=normed_cmap(df["Goals"], cmap=matplotlib.cm.PiYG, num_stds=2)),
    ColumnDefinition(name="Assists", textprops={"ha": "center", "color": "#000000", "weight": "bold", "bbox": {"boxstyle": "circle", "pad": 0.35}}, cmap=normed_cmap(df["Assists"], cmap=matplotlib.cm.PiYG_r, num_stds=2)),
    ColumnDefinition(name="PEN", textprops={"ha": "center"}, width=0.75),
    ColumnDefinition(name="Min'", textprops={"ha": "center"}, width=1.0)
]

# Create the table
fig, ax = plt.subplots(figsize=(20, 12))
fig.set_facecolor(bg_color)
ax.set_facecolor(bg_color)
table = Table(
    df,
    column_definitions=col_defs,
    index_col="S.no",
    row_dividers=True,
    row_divider_kw={"linewidth": 1, "linestyle": (0, (1, 5))},
    footer_divider=True,
    textprops={"fontsize": 14},
    col_label_divider_kw={"linewidth": 1, "linestyle": "-"},
    column_border_kw={"linewidth": .5, "linestyle": "-"},
    ax=ax,
).autoset_fontcolors(colnames=["Goals", "Assists"]) # This will set the font color of the columns based on the cmap so the text is readable

fig.show()


# In[81]:


import pandas as pd
import matplotlib.pyplot as plt
from plottable import ColumnDefinition, Table

# New Data for Goals
goals_data = {
    "Rank": [1, 2, 3, 4, 4, 4, 7, 8, 9, 9, 11],
    "Player": ["Erling Haaland • Manchester City", "Cole Palmer • 2 squads", "Alexander Isak • Newcastle Utd",
               "Ollie Watkins • Aston Villa", "Dominic Solanke • Bournemouth", "Phil Foden • Manchester City",
               "Mohamed Salah • Liverpool", "Son Heung-min • Tottenham", "Jean-Philippe Mateta • Crystal Palace",
               "Jarrod Bowen • West Ham", "Bukayo Saka • Arsenal"],
    "Goals": [27, 22, 21, 19, 19, 19, 18, 17, 16, 16, None]
}

# Create DataFrame
goals_df = pd.DataFrame(goals_data)

# Set up the colors
bg_color = "#FFFFFF"
text_color = "#000000"

plt.rcParams["text.color"] = text_color
plt.rcParams["font.family"] = "monospace"

# Create ColumnDefinitions for the table
col_defs = [
    ColumnDefinition(name="Rank", textprops={"ha": "center"}, width=0.5),
    ColumnDefinition(name="Player", textprops={"ha": "left", "weight": "bold"}, width=2.75),
    ColumnDefinition(name="Goals", textprops={"ha": "center"}, width=0.75)
]

# Create the table
fig, ax = plt.subplots(figsize=(12, 8))
fig.set_facecolor(bg_color)
ax.set_facecolor(bg_color)
table = Table(
    goals_df,
    column_definitions=col_defs,
    index_col="Rank",
    row_dividers=True,
    row_divider_kw={"linewidth": 1, "linestyle": (0, (1, 5))},
    footer_divider=True,
    textprops={"fontsize": 14},
    col_label_divider_kw={"linewidth": 1, "linestyle": "-"},
    column_border_kw={"linewidth": .5, "linestyle": "-"},
    ax=ax
)

fig.show()


# In[83]:





# In[88]:


import pandas as pd
import matplotlib.pyplot as plt
from plottable import ColumnDefinition, Table

# Define data for each table
tables_data = {
    "Goals": {
        "Rank": [1, 2, 3, 4, 4, 4, 7, 8, 9, 9, 11],
        "Player": ["Erling Haaland • Manchester City", "Cole Palmer • 2 squads", "Alexander Isak • Newcastle Utd",
                   "Ollie Watkins • Aston Villa", "Dominic Solanke • Bournemouth", "Phil Foden • Manchester City",
                   "Mohamed Salah • Liverpool", "Son Heung-min • Tottenham", "Jean-Philippe Mateta • Crystal Palace",
                   "Jarrod Bowen • West Ham", "Bukayo Saka • Arsenal"],
        "Goals": [27, 22, 21, 19, 19, 19, 18, 17, 16, 16, 16]
    },
    "Goals/90": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],
        "Player": ["Erling Haaland • Manchester City", "Alexander Isak • Newcastle Utd", "Diogo Jota • Liverpool",
                   "Cole Palmer • 2 squads", "Michael Olise • Crystal Palace", "Chris Wood • Nott'ham Forest",
                   "Richarlison • Tottenham", "Leandro Trossard • Arsenal", "Mohamed Salah • Liverpool",
                   "Elijah Adebayo • Luton Town", "Jean-Philippe Mateta • Crystal Palace"],
        "Goals/90": [0.95, 0.84, 0.79, 0.76, 0.71, 0.70, 0.66, 0.65, 0.64, 0.63, 0.63]
    },
    "Goals + Assists": {
        "Rank": [1, 2, 2, 4, 5, 5, 7, 8, 9, 9],
        "Player": ["Cole Palmer • 2 squads", "Erling Haaland • Manchester City", "Ollie Watkins • Aston Villa",
                   "Mohamed Salah • Liverpool", "Son Heung-min • Tottenham", "Phil Foden • Manchester City",
                   "Bukayo Saka • Arsenal", "Alexander Isak • Newcastle Utd", "Jarrod Bowen • West Ham",
                   "Dominic Solanke • Bournemouth"],
        "Goals + Assists": [33, 32, 32, 28, 27, 27, 25, 23, 22, 22]
    },
    "Goals + Assists/90": {
        "Rank": [1, 1, 1, 4, 5, 6, 7, 8, 9, 10],
        "Player": ["Erling Haaland • Manchester City", "Michael Olise • Crystal Palace", "Cole Palmer • 2 squads",
                   "Kevin De Bruyne • Manchester City", "Diogo Jota • Liverpool", "Mohamed Salah • Liverpool",
                   "Alexander Isak • Newcastle Utd", "Richarlison • Tottenham", "Ollie Watkins • Aston Villa",
                   "Phil Foden • Manchester City"],
        "Goals + Assists/90": [1.13, 1.13, 1.13, 1.03, 1.02, 0.99, 0.92, 0.91, 0.90, 0.85]
    },
    "Penalty Kicks Made": {
        "Rank": [1, 2, 3, 4, 4, 4, 7, 7, 7, 10],
        "Player": ["Cole Palmer • 2 squads", "Erling Haaland • Manchester City", "Bukayo Saka • Arsenal",
                   "Carlton Morris • Luton Town", "Mohamed Salah • Liverpool", "Alexander Isak • Newcastle Utd",
                   "João Pedro • Brighton", "Douglas Luiz • Aston Villa", "Bruno Fernandes • Manchester Utd",
                   "Bryan Mbeumo • Brentford"],
        "Penalty Kicks Made": [9, 7, 6, 5, 5, 5, 4, 4, 4, 4]
    },
    "Non-Penalty Goals": {
        "Rank": [1, 2, 2, 4, 5, 5, 7, 8, 8, 8],
        "Player": ["Erling Haaland • Manchester City", "Ollie Watkins • Aston Villa", "Phil Foden • Manchester City",
                   "Dominic Solanke • Bournemouth", "Jarrod Bowen • West Ham", "Alexander Isak • Newcastle Utd",
                   "Son Heung-min • Tottenham", "Chris Wood • Nott'ham Forest", "Jean-Philippe Mateta • Crystal Palace",
                   "Nicolas Jackson • Chelsea"],
        "Non-Penalty Goals": [20, 19, 19, 17, 16, 16, 15, 14, 14, 14]
    },
    "xG: Expected Goals": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Player": ["Erling Haaland • Manchester City", "Mohamed Salah • Liverpool", "Alexander Isak • Newcastle Utd",
                   "Dominic Solanke • Bournemouth", "Nicolas Jackson • Chelsea", "Cole Palmer • 2 squads",
                   "Ollie Watkins • Aston Villa", "Darwin Núñez • Liverpool", "Bukayo Saka • Arsenal",
                   "Julián Álvarez • Manchester City"],
        "xG": [29.2, 21.2, 20.3, 19.6, 18.6, 18.2, 16.8, 16.3, 15.5, 13.0]
    },
    "xG/90": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],
        "Player": ["Erling Haaland • Manchester City", "Alexander Isak • Newcastle Utd", "Mohamed Salah • Liverpool",
                   "Darwin Núñez • Liverpool", "Cole Palmer • 2 squads", "Nicolas Jackson • Chelsea",
                   "Chris Wood • Nott'ham Forest", "Richarlison • Tottenham", "Dominic Calvert-Lewin • Everton",
                   "Dominic Solanke • Bournemouth", "João Pedro • Brighton"],
        "xG/90": [1.03, 0.81, 0.75, 0.72, 0.63, 0.60, 0.59, 0.58, 0.54, 0.53, 0.53]
    },
    "Shots Total": {
        "Rank": [1, 2, 2, 2, 5, 6, 7, 8, 8, 10],
        "Player": ["Erling Haaland • Manchester City", "Darwin Núñez • Liverpool", "Ollie Watkins • Aston Villa",
                   "Mohamed Salah • Liverpool", "Dominic Solanke • Bournemouth", "Phil Foden • Manchester City",
                   "Bukayo Saka • Arsenal", "Alejandro Garnacho • Manchester Utd", "Cole Palmer • 2 squads",
                   "Julián Álvarez • Manchester City"],
        "Shots Total": [113, 107, 107, 107, 106, 105, 102, 100, 100, 96]
    },
    "Shots Total/90": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Player": ["Darwin Núñez • Liverpool", "Rodrigo Muniz • Fulham", "Erling Haaland • Manchester City",
                   "Michael Olise • Crystal Palace", "Mohamed Salah • Liverpool", "Richarlison • Tottenham",
                   "Cody Gakpo • Liverpool", "Eberechi Eze • Crystal Palace", "Alejandro Garnacho • Manchester Utd",
                   "Cole Palmer • 2 squads"],
        "Shots Total/90": [4.70, 4.12, 3.99, 3.95, 3.80, 3.74, 3.60, 3.59, 3.51, 3.44]
    },
    "Shots on Target": {
        "Rank": [1, 2, 3, 3, 5, 6, 6, 8, 8, 8],
        "Player": ["Erling Haaland • Manchester City", "Phil Foden • Manchester City", "Ollie Watkins • Aston Villa",
                   "Mohamed Salah • Liverpool", "Darwin Núñez • Liverpool", "Son Heung-min • Tottenham",
                   "Nicolas Jackson • Chelsea", "Julián Álvarez • Manchester City", "Jarrod Bowen • West Ham",
                       "Cole Palmer • 2 squads"],
            "Shots on Target": [50, 48, 47, 47, 46, 38, 38, 37, 37, 37]
        },
        "Shots on Target/90": {
            "Rank": [1, 2, 3, 4, 4, 6, 7, 8, 9, 10],
            "Player": ["Darwin Núñez • Liverpool", "Erling Haaland • Manchester City", "Mohamed Salah • Liverpool",
                       "Phil Foden • Manchester City", "Richarlison • Tottenham", "Diogo Jota • Liverpool",
                       "Rodrigo Muniz • Fulham", "Eberechi Eze • Crystal Palace", "Alexander Isak • Newcastle Utd",
                       "Michael Olise • Crystal Palace"],
            "Shots on Target/90": [2.02, 1.76, 1.67, 1.51, 1.51, 1.49, 1.47, 1.45, 1.44, 1.41]
        }
}

# Define function to create and save tables
def create_and_save_table(data, title):
    df = pd.DataFrame(data)
    bg_color = "#FFFFFF"
    text_color = "#000000"
    
    plt.rcParams["text.color"] = text_color
    plt.rcParams["font.family"] = "monospace"
    
    col_defs = [ColumnDefinition(name=col, textprops={"ha": "center"}, width=1.0) for col in df.columns]
    if "Player" in df.columns:
        col_defs[df.columns.get_loc("Player")] = ColumnDefinition(name="Player", textprops={"ha": "left", "weight": "bold"}, width=3.0)
    
    fig, ax = plt.subplots(figsize=(12, len(df) * 0.5 + 2))
    fig.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    
    table = Table(
        df,
        column_definitions=col_defs,
        row_dividers=True,
        row_divider_kw={"linewidth": 1, "linestyle": (0, (1, 5))},
        footer_divider=True,
        textprops={"fontsize": 14},
        col_label_divider_kw={"linewidth": 1, "linestyle": "-"},
        column_border_kw={"linewidth": .5, "linestyle": "-"},
        ax=ax
    )

# Create and save tables for each category
for title, data in tables_data.items():
    create_and_save_table(data, title)


# In[92]:


import pandas as pd

# Define the data for each table
data = {
    "Goals": {
        "Rank": [1, 2, 3, 4, 4, 4, 7, 8, 9, 9, 11],
        "Player": ["Erling Haaland • Manchester City", "Cole Palmer • 2 squads", "Alexander Isak • Newcastle Utd",
                   "Ollie Watkins • Aston Villa", "Dominic Solanke • Bournemouth", "Phil Foden • Manchester City",
                   "Mohamed Salah • Liverpool", "Son Heung-min • Tottenham", "Jean-Philippe Mateta • Crystal Palace",
                   "Jarrod Bowen • West Ham", "Bukayo Saka • Arsenal"],
        "Goals": [27, 22, 21, 19, 19, 19, 18, 17, 16, 16, 16]
    },
    "Goals_per_90": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],
        "Player": ["Erling Haaland • Manchester City", "Alexander Isak • Newcastle Utd", "Diogo Jota • Liverpool",
                   "Cole Palmer • 2 squads", "Michael Olise • Crystal Palace", "Chris Wood • Nott'ham Forest",
                   "Richarlison • Tottenham", "Leandro Trossard • Arsenal", "Mohamed Salah • Liverpool",
                   "Elijah Adebayo • Luton Town", "Jean-Philippe Mateta • Crystal Palace"],
        "Goals/90": [0.95, 0.84, 0.79, 0.76, 0.71, 0.70, 0.66, 0.65, 0.64, 0.63, 0.63]
    },
    "Goals_Assists": {
        "Rank": [1, 2, 2, 4, 5, 5, 7, 8, 9, 9],
        "Player": ["Cole Palmer • 2 squads", "Erling Haaland • Manchester City", "Ollie Watkins • Aston Villa",
                   "Mohamed Salah • Liverpool", "Son Heung-min • Tottenham", "Phil Foden • Manchester City",
                   "Bukayo Saka • Arsenal", "Alexander Isak • Newcastle Utd", "Jarrod Bowen • West Ham",
                   "Dominic Solanke • Bournemouth"],
        "Goals + Assists": [33, 32, 32, 28, 27, 27, 25, 23, 22, 22]
    }
}

# Define the path
excel_path = r"C:\BA\Projects\Sports Analytics\Individual project\General Metrics.xlsx"

# Create an Excel writer object
writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')

# Write each dataframe to a different worksheet
for sheet_name, sheet_data in data.items():
    df = pd.DataFrame(sheet_data)
    # Sanitize sheet name by replacing invalid characters with underscore
    sanitized_sheet_name = sheet_name.replace("/", "_").replace(" ", "_").replace("+", "_")
    df.to_excel(writer, sheet_name=sanitized_sheet_name, index=False)
    worksheet = writer.sheets[sanitized_sheet_name]
    
    # Apply formatting
    format1 = writer.book.add_format({'num_format': '0.00', 'align': 'center'})
    format2 = writer.book.add_format({'align': 'center'})
    worksheet.set_column('A:A', 5, format2)
    worksheet.set_column('B:B', 35, format2)
    worksheet.set_column('C:C', 10, format1)
    worksheet.autofilter(0, 0, len(df), len(df.columns) - 1)

# Save the Excel file
writer.save()

print(f"Excel file saved at: {excel_path}")


# In[95]:


import pandas as pd

# Define the data for each table
data = {
    "Goals": {
        "Rank": [1, 2, 3, 4, 4, 4, 7, 8, 9, 9, 11],
        "Player": ["Erling Haaland • Manchester City", "Cole Palmer • 2 squads", "Alexander Isak • Newcastle Utd",
                   "Ollie Watkins • Aston Villa", "Dominic Solanke • Bournemouth", "Phil Foden • Manchester City",
                   "Mohamed Salah • Liverpool", "Son Heung-min • Tottenham", "Jean-Philippe Mateta • Crystal Palace",
                   "Jarrod Bowen • West Ham", "Bukayo Saka • Arsenal"],
        "Goals": [27, 22, 21, 19, 19, 19, 18, 17, 16, 16, 16]
    },
    "Goals_90": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],
        "Player": ["Erling Haaland • Manchester City", "Alexander Isak • Newcastle Utd", "Diogo Jota • Liverpool",
                   "Cole Palmer • 2 squads", "Michael Olise • Crystal Palace", "Chris Wood • Nott'ham Forest",
                   "Richarlison • Tottenham", "Leandro Trossard • Arsenal", "Mohamed Salah • Liverpool",
                   "Elijah Adebayo • Luton Town", "Jean-Philippe Mateta • Crystal Palace"],
        "Goals_90": [0.95, 0.84, 0.79, 0.76, 0.71, 0.70, 0.66, 0.65, 0.64, 0.63, 0.63]
    },
    "Goals_Assists": {
        "Rank": [1, 2, 2, 4, 5, 5, 7, 8, 9, 9],
        "Player": ["Cole Palmer • 2 squads", "Erling Haaland • Manchester City", "Ollie Watkins • Aston Villa",
                   "Mohamed Salah • Liverpool", "Son Heung-min • Tottenham", "Phil Foden • Manchester City",
                   "Bukayo Saka • Arsenal", "Alexander Isak • Newcastle Utd", "Jarrod Bowen • West Ham",
                   "Dominic Solanke • Bournemouth"],
        "Goals_Assists": [33, 32, 32, 28, 27, 27, 25, 23, 22, 22]
    },
    "Penalty_Kicks_Made": {
        "Rank": [1, 2, 3, 4, 4, 4, 7, 7, 7, 10],
        "Player": ["Cole Palmer • 2 squads", "Erling Haaland • Manchester City", "Bukayo Saka • Arsenal",
                   "Carlton Morris • Luton Town", "Mohamed Salah • Liverpool", "Alexander Isak • Newcastle Utd",
                   "João Pedro • Brighton", "Douglas Luiz • Aston Villa", "Bruno Fernandes • Manchester Utd",
                   "Bryan Mbeumo • Brentford"],
        "Penalty_Kicks_Made": [9, 7, 6, 5, 5, 5, 4, 4, 4, 3]
    },
    "Non_Penalty_Goals": {
        "Rank": [1, 2, 2, 4, 5, 5, 7, 8, 8, 8],
        "Player": ["Erling Haaland • Manchester City", "Ollie Watkins • Aston Villa", "Phil Foden • Manchester City",
                   "Dominic Solanke • Bournemouth", "Jarrod Bowen • West Ham", "Alexander Isak • Newcastle Utd",
                   "Son Heung-min • Tottenham", "Chris Wood • Nott'ham Forest", "Jean-Philippe Mateta • Crystal Palace",
                   "Nicolas Jackson • Chelsea"],
        "Non_Penalty_Goals": [20, 19, 19, 17, 16, 16, 15, 14, 14, 14]
    },
    "Non_Penalty_Goals_Assists_90": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
        "Player": ["Michael Olise • Crystal Palace", "Kevin De Bruyne • Manchester City", "Diogo Jota • Liverpool",
                   "Richarlison • Tottenham", "Ollie Watkins • Aston Villa", "Erling Haaland • Manchester City",
                   "Phil Foden • Manchester City", "Darwin Núñez • Liverpool", "Leon Bailey • Aston Villa",
                   "Cole Palmer • 2 squads"],
        "Non_Penalty_Goals_Assists_90": [1.06, 1.03, 1.02, 0.91, 0.90, 0.88, 0.85, 0.84, 0.83, 0.83]
    },
    "xG_Expected_Goals": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Player": ["Erling Haaland • Manchester City", "Mohamed Salah • Liverpool", "Alexander Isak • Newcastle Utd",
                   "Dominic Solanke • Bournemouth", "Nicolas Jackson • Chelsea", "Cole Palmer • 2 squads",
                   "Ollie Watkins • Aston Villa", "Darwin Núñez • Liverpool", "Bukayo Saka • Arsenal",
                   "Julián Álvarez • Manchester City"],
        "xG": [29.2, 21.2, 20.3, 19.6, 18.6, 18.2, 16.8, 16.3, 15.5, 13.0]
    },
    "xG_90": {
        "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],
        "Player": ["Erling Haaland • Manchester City", "Alexander Isak • Newcastle Utd", "Mohamed Salah • Liverpool",
                   "Darwin Núñez • Liverpool", "Cole Palmer • 2 squads", "Nicolas Jackson • Chelsea",
                   "Chris Wood • Nott'ham Forest", "Richarlison • Tottenham", "Dominic Calvert-Lewin • Everton",
                   "Dominic Solanke • Bournemouth", "João Pedro • Brighton"],
        "xG_90": [1.03, 0.81, 0.75, 0.72, 0.63, 0.60, 0.59, 0.58, 0.54, 0.53, 0.53]
    },
    "Shots_Total": {
        "Rank": [1, 2, 2, 2, 5, 6, 7, 8, 8, 10],
        "Player": ["Erling Haaland • Manchester City", "Darwin Núñez • Liverpool", "Ollie Watkins • Aston Villa",
                   "Mohamed Salah • Liverpool", "Dominic Solanke • Bournemouth", "Phil Foden • Manchester City",
                   "Bukayo Saka • Arsenal", "Alejandro Garnacho • Manchester Utd", "Cole Palmer • 2 squads",
                   "Julián Álvarez • Manchester City"],
        "Shots_Total": [113, 107, 107, 107, 106, 105, 102, 100, 100, 96]
    },
    "Shots_on_Target": {
        "Rank": [1, 2, 3, 3, 5, 6, 6, 8, 8, 8],
        "Player": ["Erling Haaland • Manchester City", "Phil Foden • Manchester City", "Ollie Watkins • Aston Villa",
                   "Mohamed Salah • Liverpool", "Darwin Núñez • Liverpool", "Son Heung-min • Tottenham",
                   "Nicolas Jackson • Chelsea", "Julián Álvarez • Manchester City", "Jarrod Bowen • West Ham",
                   "Cole Palmer • 2 squads"],
        "Shots_on_Target": [50, 48, 47, 47, 46, 38, 38, 37, 37, 37]
    }
}

# Create an Excel writer object
excel_path = r"C:\BA\Projects\Sports Analytics\Individual project\General Metrics.xlsx"
writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')

# Write each dataframe to a different worksheet
for sheet_name, sheet_data in data.items():
    df = pd.DataFrame(sheet_data)
    # Sanitize sheet name by replacing invalid characters with underscore
    sanitized_sheet_name = sheet_name.replace("/", "_").replace(" ", "_").replace("+", "_").replace(":", "_")
    df.to_excel(writer, sheet_name=sanitized_sheet_name, index=False
    )
    worksheet = writer.sheets[sanitized_sheet_name]
    
    # Apply formatting
    format1 = writer.book.add_format({'num_format': '0.00', 'align': 'center'})
    format2 = writer.book.add_format({'align': 'center'})
    worksheet.set_column('A:A', 5, format2)
    worksheet.set_column('B:B', 35, format2)
    worksheet.set_column('C:C', 10, format1)
    worksheet.autofilter(0, 0, len(df), len(df.columns) - 1)

# Save the Excel file
writer.save()

print(f"Excel file saved at: {excel_path}")


# In[97]:


import matplotlib.pyplot as plt
import seaborn as sns

# Define the data
data = {
    'Metrics': ['Goals Per 90', 'Assists Per 90', 'G+A Per 90', 'xG Per 90', 'xA Per 90', 'Cards Per 90'],
    'Values': [1.17, 0.26, 1.42, 0.82, 0.20, 0.16],
    'Totals': ['36 Goals Total', '8 Assists Total', '44 Goal Contributions Total', '25.23 Expected Goals', '6.32 Expected Assists', '5 Cards Total'],
    'Percentiles': ['99th Percentile', '94th Percentile', '99th Percentile', '99th Percentile', '82nd Percentile', '42nd Percentile'],
    'Colors': ['#00a65a', '#00a65a', '#00a65a', '#00a65a', '#66cc66', '#ff6666']
}

# Create a figure and a set of subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 8), constrained_layout=True)

# Flatten the axes array for easy iteration
axs = axs.flatten()

# Plot each metric
for i, ax in enumerate(axs):
    ax.set_facecolor(data['Colors'][i])
    ax.text(0.5, 0.7, f"{data['Values'][i]}", ha='center', va='center', fontsize=24, weight='bold', color='white')
    ax.text(0.5, 0.4, data['Metrics'][i], ha='center', va='center', fontsize=14, color='white')
    ax.text(0.5, 0.25, data['Totals'][i], ha='center', va='center', fontsize=12, color='white')
    ax.text(0.5, 0.1, data['Percentiles'][i], ha='center', va='center', fontsize=12, weight='bold', color='white')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

# Set the main title
plt.suptitle('Per 90 minute stats in the Premier League', fontsize=16, weight='bold')


# Show the plot
plt.show()


# In[98]:


import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Year": ["2018-2019", "2019-2020", "2019-2020", "2020-2021", "2021-2022", "2022-2023", "2023-2024"],
    "Club": ["RB Salzburg", "RB Salzburg", "Dortmund", "Dortmund", "Dortmund", "Manchester City", "Manchester City"],
    "Goal involvement Ratio": [36.78, 81.41, 56.72, 57.63, 79.43, 54.97, 45.03]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Goal involvement Ratio'], marker='o', linestyle='-', color='b')
plt.title('Goal Involvement Ratio Over the Years')
plt.xlabel('Year')
plt.ylabel('Goal Involvement Ratio (%)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig(r"C:\BA\Projects\Sports Analytics\Individual project\Goal_Involvement_Ratio_Over_Years.png")

# Show the plot
plt.show()


# In[100]:


pip install mplsoccer


# In[104]:


import pandas as pd

# Define the data
data = {
    "Season": ["2016", "2017", "2018", "2018/2019", "2019/2020", "2020/2021", "2021/2022", "2022/2023", "2023/2024"],
    "Goals per 90": [0, 0.47, 0.68, 1.08, 1.46, 1.01, 1.03, 1.17, 0.95],
    "Club": ["molde.png", "salzburg.png", "salzburg.png", "salzburg.png", "salzburg.png", "dortmund.png", "dortmund.png", "manchester_city.png", "manchester_city.png"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame columns to ensure they are correct
print(df.columns)
print(df)


# In[108]:


import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Function to add images to the plot
def add_image(ax, image_path, xy, zoom=0.1):
    img = plt.imread(image_path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, xy, frameon=False)
    ax.add_artist(ab)

# Set up the plot
fig, ax = plt.subplots(figsize=(13, 7))

# Plot the line chart
ax.plot(df['Season'], df['Goals per 90'], marker='o', color='b', linestyle='-', linewidth=2, markersize=5)

# Add goal values on the plot
for i, (season, goals) in enumerate(zip(df['Season'], df['Goals per 90'])):
    ax.text(season, goals + 0.05, f'{goals}', ha='center', va='bottom')

# Add images to the plot
for i, (season, club, goals) in enumerate(zip(df['Season'], df['Club'], df['Goals per 90'])):
    add_image(ax, rf"C:\BA\Projects\Sports Analytics\Individual project\icon\{club}", (season, goals), zoom=0.1)

# Set title and labels
ax.set_title('Goals per 90 min in the league', fontsize=14)
ax.set_xlabel('Season', fontsize=12)
ax.set_ylabel('Goals per 90 min', fontsize=12)

# Display grid
ax.grid(True)

# Show plot
plt.show()


# In[116]:





# In[117]:


import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns

# Read in the data
df = pd.read_csv('messibetis.csv')

# Convert the data to match the mplsoccer StatsBomb pitch
df['x'] = df['x'] * 1.2
df['y'] = df['y'] * 0.8
df['endX'] = df['endX'] * 1.2
df['endY'] = df['endY'] * 0.8

# Display the modified DataFrame
df


# In[120]:


import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch

# Read in the data
df = pd.read_csv('messibetis.csv')

# Convert the data to match the mplsoccer StatsBomb pitch
df['x'] = df['x'] * (120 / 100)
df['y'] = df['y'] * (80 / 100)
df['endX'] = df['endX'] * (120 / 100)
df['endY'] = df['endY'] * (80 / 100)

# Create the pitch
pitch = Pitch(pitch_type='statsbomb', line_zorder=2)
fig, ax = pitch.draw(figsize=(10, 7))

# Plot the passes
for i, row in df.iterrows():
    if row['outcome'] == 'Successful':
        color = 'green'
    else:
        color = 'red'
    pitch.arrows(row['x'], row['y'], row['endX'], row['endY'], color=color, ax=ax, width=1, headwidth=3, alpha=0.7)

plt.title('Messi Passes against Betis')
plt.show()


# In[2]:


import pandas as pd

# Define the data
data = {
    "Shot zones": ["Out of box", "Penalty area", "Six-yard box"],
    "Sh": [26, 357, 67],
    "G": [5, 87, 33],
    "KP": [26, 84, 7],
    "A": [2, 21, 5],
    "xG": [2.20, 79.30, 32.44],
    "xA": [1.03, 16.68, 4.34],
    "xG/Sh": [0.08, 0.22, 0.48],
    "xA/KP": [0.04, 0.20, 0.62]
}

# Create a DataFrame
df = pd.DataFrame(data)


# In[4]:


import matplotlib.pyplot as plt

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart for Shots, Goals, and Key Passes
bar_width = 0.2
index = df.index

bars1 = ax.bar(index, df['Sh'], bar_width, label='Shots')
bars2 = ax.bar(index + bar_width, df['G'], bar_width, label='Goals')
bars3 = ax.bar(index + 2 * bar_width, df['KP'], bar_width, label='Key Passes')

# Add some text for labels, title and axes ticks
ax.set_xlabel('Shot Zones')
ax.set_ylabel('Count')
ax.set_title('Shots, Goals, and Key Passes by Shot Zone')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(df['Shot zones'])
ax.legend()

# Display the chart
plt.show()


# In[5]:


# Plot the pie chart for Goals distribution
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(df['G'], labels=df['Shot zones'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
ax.set_title('Goals Distribution by Shot Zone')

# Display the chart
plt.show()


# In[6]:


# Plot the scatter plot for xG vs G
fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(df['xG'], df['G'], c=['red', 'green', 'blue'], s=100)

# Add some text for labels, title, and custom x-axis tick labels, etc.
for i, txt in enumerate(df['Shot zones']):
    ax.annotate(txt, (df['xG'][i], df['G'][i]), fontsize=12, ha='right')

ax.set_xlabel('Expected Goals (xG)')
ax.set_ylabel('Goals (G)')
ax.set_title('Expected Goals vs Actual Goals by Shot Zone')

# Display the chart
plt.show()


# In[7]:


import pandas as pd

# Define the data
data = {
    "Shot types": ["Left foot", "Right foot", "Head", "Other body part"],
    "Sh": [294, 67, 85, 4],
    "G": [92, 16, 16, 1],
    "KP": [47, 69, 1, 0],
    "A": [13, 15, 0, 0],
    "xG": [81.80, 15.26, 15.30, 1.57],
    "xA": [10.17, 11.86, 0.03, 0.00],
    "xG/Sh": [0.28, 0.23, 0.18, 0.39],
    "xA/KP": [0.22, 0.17, 0.03, 0.00]
}

# Create a DataFrame
df = pd.DataFrame(data)


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data
data = {
    "Shot types": ["Left foot", "Right foot", "Head", "Other body part"],
    "Sh": [294, 67, 85, 4],
    "G": [92, 16, 16, 1],
    "KP": [47, 69, 1, 0],
    "A": [13, 15, 0, 0],
    "xG": [81.80, 15.26, 15.30, 1.57],
    "xA": [10.17, 11.86, 0.03, 0.00],
    "xG/Sh": [0.28, 0.23, 0.18, 0.39],
    "xA/KP": [0.22, 0.17, 0.03, 0.00]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Heatmap for intensity of shots, goals, xG, and xA
heatmap_data = df[['Shot types', 'Sh', 'G', 'xG', 'xA']].set_index('Shot types')

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='YlGnBu')
plt.title('Intensity of Shots, Goals, xG, and xA by Shot Type')
plt.show()


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data
data = [
    {"Description": "Muscle Injury", "Start Date": "17/04/24", "End Date": "26/04/24"},
    {"Description": "Foot Injury", "Start Date": "09/12/23", "End Date": "24/01/24"},
    {"Description": "Ankle Injury", "Start Date": "16/11/23", "End Date": "23/11/23"},
    {"Description": "Ankle Injury", "Start Date": "04/11/23", "End Date": "05/11/23"},
    {"Description": "Groin Injury", "Start Date": "20/03/23", "End Date": "04/04/23"},
    {"Description": "Knock", "Start Date": "12/02/23", "End Date": "13/02/23"},
    {"Description": "Knock", "Start Date": "25/10/22", "End Date": "03/11/22"},
    {"Description": "Illness", "Start Date": "03/05/22", "End Date": "05/05/22"},
    {"Description": "Knock", "Start Date": "22/01/22", "End Date": "11/03/22"},
    {"Description": "Hip/Thigh Injury", "Start Date": "21/10/21", "End Date": "25/11/21"},
    {"Description": "Thigh Injury", "Start Date": "19/09/21", "End Date": "14/10/21"},
    {"Description": "Knock", "Start Date": "24/04/21", "End Date": "12/05/21"},
    {"Description": "Hamstring", "Start Date": "01/12/20", "End Date": "01/01/21"},
    {"Description": "Knee Injury", "Start Date": "26/05/20", "End Date": "11/06/20"},
]

# Convert to DataFrame
df = pd.DataFrame(data)
df['Start Date'] = pd.to_datetime(df['Start Date'], format='%d/%m/%y')
df['End Date'] = pd.to_datetime(df['End Date'], format='%d/%m/%y')

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

for i, row in df.iterrows():
    ax.plot([row['Start Date'], row['End Date']], [i, i], marker='o')

# Formatting
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
plt.xticks(rotation=45)
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Description'])

plt.xlabel('Date')
plt.ylabel('Injury Type')
plt.title('Injury Timeline')
plt.grid(True)

plt.tight_layout()
plt.show()


# In[22]:


import pandas as pd
import matplotlib.pyplot as plt

# Data
data = [
    {"Description": "Muscle Injury", "Start Date": "17/04/24", "End Date": "26/04/24"},
    {"Description": "Foot Injury", "Start Date": "09/12/23", "End Date": "24/01/24"},
    {"Description": "Ankle Injury", "Start Date": "16/11/23", "End Date": "23/11/23"},
    {"Description": "Ankle Injury", "Start Date": "04/11/23", "End Date": "05/11/23"},
    {"Description": "Groin Injury", "Start Date": "20/03/23", "End Date": "04/04/23"},
    {"Description": "Knock", "Start Date": "12/02/23", "End Date": "13/02/23"},
    {"Description": "Knock", "Start Date": "25/10/22", "End Date": "03/11/22"},
    {"Description": "Illness", "Start Date": "03/05/22", "End Date": "05/05/22"},
    {"Description": "Knock", "Start Date": "22/01/22", "End Date": "11/03/22"},
    {"Description": "Hip/Thigh Injury", "Start Date": "21/10/21", "End Date": "25/11/21"},
    {"Description": "Thigh Injury", "Start Date": "19/09/21", "End Date": "14/10/21"},
    {"Description": "Knock", "Start Date": "24/04/21", "End Date": "12/05/21"},
    {"Description": "Hamstring", "Start Date": "01/12/20", "End Date": "01/01/21"},
    {"Description": "Knee Injury", "Start Date": "26/05/20", "End Date": "11/06/20"},
]

# Convert to DataFrame
df = pd.DataFrame(data)
df['Start Date'] = pd.to_datetime(df['Start Date'], format='%d/%m/%y')
df['End Date'] = pd.to_datetime(df['End Date'], format='%d/%m/%y')
df['Duration'] = (df['End Date'] - df['Start Date']).dt.days

# Group by Description and sum the durations
duration_df = df.groupby('Description')['Duration'].sum().reset_index()

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(duration_df['Description'], duration_df['Duration'], color='skyblue')
ax.set_xlabel('Total Days Sidelined')
ax.set_ylabel('Injury Type')
ax.set_title('Total Days Sidelined by Injury Type')

plt.tight_layout()
plt.show()


# In[28]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data
data = [
    {"Description": "Muscle Injury", "Start Date": "17/04/24", "End Date": "26/04/24"},
    {"Description": "Foot Injury", "Start Date": "09/12/23", "End Date": "24/01/24"},
    {"Description": "Ankle Injury", "Start Date": "16/11/23", "End Date": "23/11/23"},
    {"Description": "Ankle Injury", "Start Date": "04/11/23", "End Date": "05/11/23"},
    {"Description": "Groin Injury", "Start Date": "20/03/23", "End Date": "04/04/23"},
    {"Description": "Knock", "Start Date": "12/02/23", "End Date": "13/02/23"},
    {"Description": "Knock", "Start Date": "25/10/22", "End Date": "03/11/22"},
    {"Description": "Illness", "Start Date": "03/05/22", "End Date": "05/05/22"},
    {"Description": "Knock", "Start Date": "22/01/22", "End Date": "11/03/22"},
    {"Description": "Hip/Thigh Injury", "Start Date": "21/10/21", "End Date": "25/11/21"},
    {"Description": "Thigh Injury", "Start Date": "19/09/21", "End Date": "14/10/21"},
    {"Description": "Knock", "Start Date": "24/04/21", "End Date": "12/05/21"},
    {"Description": "Hamstring", "Start Date": "01/12/20", "End Date": "01/01/21"},
    {"Description": "Knee Injury", "Start Date": "26/05/20", "End Date": "11/06/20"},
]

# Convert to DataFrame
df = pd.DataFrame(data)
df['Start Date'] = pd.to_datetime(df['Start Date'], format='%d/%m/%y')
df['End Date'] = pd.to_datetime(df['End Date'], format='%d/%m/%y')
df['Duration'] = (df['End Date'] - df['Start Date']).dt.days

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

for i, row in df.iterrows():
    ax.plot([row['Start Date'], row['End Date']], [i, i], marker='o')
    ax.text(row['End Date'], i, f" ({row['Duration']} days)", verticalalignment='center')

# Formatting
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Description'])


plt.ylabel('Injury Type')
plt.title('Injury Timeline')

plt.tight_layout()
plt.show()


# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the DataFrame from the provided data
data_jude = {
    "Shot types": ["Right foot", "Left foot", "Head", "Other body part"],
    "Sh": [122, 54, 28, 1],
    "G": [16, 11, 4, 0],
    "KP": [82, 44, 7, 0],
    "A": [13, 7, 1, 0],
    "xG": [15.85, 7.13, 5.94, 0.03],
    "xA": [11.48, 6.73, 1.40, 0.00],
    "xG/Sh": [0.13, 0.13, 0.21, 0.03],
    "xA/KP": [0.14, 0.15, 0.20, 0.00]
}

df_jude = pd.DataFrame(data_jude)

# Selecting columns to visualize in heatmap
heatmap_data = df_jude.set_index("Shot types")[["Sh", "G", "xG", "xA"]]

# Plotting the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=.5)
plt.title("Intensity of Shots, Goals, xG, and xA by Shot Type")
plt.show()


# In[ ]:




