import streamlit as st
from pybaseball.plotting import plot_strike_zone
from pybaseball import statcast_pitcher
import pandas as pd

# Title and description
st.title("Field Manager Pitch Plots")
st.write(
    "Choose an MLB pitcher and game and see their pitches plotted for that game. "
)
# Notes on what the arguments for plot strike zone are
#plot_strike_zone(data: pd.DataFrame, title: str = '', colorby: str = 'pitch_type', 
#       legend_title: str = '', annotation: str = 'pitch_type', axis: Optional[axes.Axes] = None) -> axes.Axes:

#Arguments
#data: StatCast pandas.DataFrame of StatCast pitcher data
#title: (str), default = '' Optional: Title of plot
#colorby: (str), default = 'pitch_type', Optional: Which category to color the mark with. 'pitch_type', 
#       'pitcher', 'description' or a column within data
#legend_title: (str), default = based on colorby, Optional: Title for the legend
#annotation: (str), default = 'pitch_type', Optional: What to annotate in the marker. 'pitch_type', 
#       'release_speed', 'effective_speed', 'launch_speed', or something else in the data
#axis: (matplotlib.axis.Axes), default = None, Optional: Axes to plot the strike zone on. If None, a new Axes will be created


# Get pitchers for this year and last 3 years
data = pd.read_csv('https://raw.githubusercontent.com/Zthan/pitch_plots/refs/heads/main/pitch_plot_player_list.csv')

# Create a dictionary of player names and their MLBAM IDs
player_dict = data.apply(lambda row: (f"{row['name_first']} {row['name_last']}", row['key_mlbam']), axis=1).to_dict()


# Get full names of players
full_names = list(player_dict.keys())
full_names.sort()
full_names = [s.title() for s in full_names]

# Default player selection
default_index = full_names.index('Spencer Schwellenbach')
entered_name = st.selectbox("Pick an MLB Player.", full_names, index=default_index)
mlbam_id = player_dict[entered_name]

# Get full names of players
#full_names = data.apply(lambda row: f"{row['name_first']} {row['name_last']}", axis=1).tolist()
#full_names.sort()
#full_names = [s.title() for s in full_names]

# Default player selection
#default_index = full_names.index('Spencer Schwellenbach')
#entered_name = st.selectbox("Pick an MLB Player.", full_names, index=default_index)
name_first = entered_name.split(' ')[0]
name_last = entered_name.split(' ')[1]

# Get either game dates or game matchups, or both in list
game_list = pd.read_csv('https://raw.githubusercontent.com/Zthan/pitch_plots/refs/heads/main/pitch_plot_game_list.csv')
# Filter game_list based on mlbam id of entered name
filtered_game_list = game_list[game_list['pitcher'] == mlbam_id]

# Ensure the filtered_game_list has the necessary columns
if 'game_date' in filtered_game_list.columns and 'matchup' in filtered_game_list.columns:
    # Create a list of formatted game dates and matchups
    game_options = filtered_game_list.apply(lambda row: f"{row['game_date']} - {row['matchup']}", axis=1).tolist()
    game_options.sort()
else:
    game_options = []

entered_game = st.selectbox("Pick a game to plot.", game_options)

# Filter game_list based on entered name
#game_list = game_list[game_list['player_name'] == entered_name]
#game_list = game_list['game_date'].tolist()
#game_list.sort()
#game_list = [str(s) for s in game_list]

#entered_game = st.selectbox("Pick a game to plot.", game_list)

# Read in files



# Make selection boxes


# Create pitch plot, capture image, and display

