import streamlit as st
from pybaseball.plotting import plot_strike_zone
from pybaseball import statcast_pitcher
import pandas as pd

# Title and description
st.title("Field Manager Pitch Plots")
st.write(
    "Choose an MLB pitcher and game and see their pitches plotted for that game. "
    "  \n  Currently 2025 spring training games don't work, so don't select them. "
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

# Get full names of players
#full_names = data.apply(lambda row: f"{row['name_first']} {row['name_last']}", axis=1).tolist()
#full_names.sort()
#full_names = [s.title() for s in full_names]

data['Full Name'] = data['name_first'] + ' ' + data['name_last']
data['Full Name'] = data['Full Name'].str.title()
#full_names = pitching_data.apply(lambda row: f"{row['name_first']} {row['name_last']}", axis=1)#.tolist()

# Create a dictionary of player names and their MLBAM IDs
# df.set_index('Key')['Value'].to_dict()
# need to make full names a single column first then do the second player dict below
#player_dict = data.apply(lambda row: (f"{row['Full Name']}", row['key_mlbam']), axis=1).to_dict()
player_dict = data.set_index('Full Name')['key_mlbam'].to_dict()

# Get full names of players
full_names = list(player_dict.keys())
full_names.sort()
#full_names = [s.title() for s in full_names]

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
#name_first = entered_name.split(' ')[0]
#name_last = entered_name.split(' ')[1]

# Get either game dates or game matchups, or both in list
game_list = pd.read_csv('https://raw.githubusercontent.com/Zthan/pitch_plots/refs/heads/main/pitch_plot_game_list.csv')
# Filter game_list based on mlbam id of entered name
game_list['option'] = game_list['game_date'] + ' - ' + game_list['Matchup']
game_list.sort_values(by='game_date', ascending=True, inplace=True)
filtered_game_list = game_list[game_list['pitcher'] == mlbam_id]

# Ensure the filtered_game_list has the necessary columns
#if 'game_date' in filtered_game_list.columns and 'matchup' in filtered_game_list.columns:
    # Create a list of formatted game dates and matchups
#    game_options = filtered_game_list.apply(lambda row: f"{row['game_date']} - {row['matchup']}", axis=1).tolist()
#    game_options.sort()
#else:
#    game_options = []
#game_options = filtered_game_list.apply(lambda row: f"{row['game_date']} - {row['matchup']}", axis=1).tolist()
entered_game = st.selectbox("Pick a game to plot.", filtered_game_list['option'])

# make colorby options selectable
colorby_options = ['pitch_type', 'description', 'release_speed', 'launch_speed', 'hit_distance_sc',
                   'bb_type', 'hit_distance', 'release_extension']
entered_colorby = st.selectbox("Pick a Color By option.", colorby_options)

# Create pitch plot, capture image, and display
game_date = entered_game.split(' - ')[0]
pitcher_data = statcast_pitcher(game_date, game_date, mlbam_id)

# create pitch type filter
#pitch_filter = st.selectbox("Pick a pitch type to filter by.", pitcher_data['pitch_type'].unique())
#pitcher_data = pitcher_data[pitcher_data['pitch_type'] == pitch_filter]

# create pitch type filter
pitch_types = ['All'] + list(pitcher_data['pitch_type'].unique())
pitch_filter = st.selectbox("Pick a pitch type to filter by.", pitch_types)

if pitch_filter != 'All':
    pitcher_data = pitcher_data[pitcher_data['pitch_type'] == pitch_filter]

# create batter handedness filter
stand_options = ['Both', 'L', 'R']
#stand_dict = {'Both': 'Both', 'Left-Handed Batters': 'L', 'Right-Handed Batters': 'R'}

if stand_filter != 'Both':
    pitcher_data = pitcher_data[pitcher_data['stand'] == stand_filter]

plot_img = plot_strike_zone(pitcher_data, title=f"{entered_name} - {entered_game}", colorby='pitch_type', legend_title='pitch_type', annotation=entered_colorby)
if st.button("Let's go already!"):
    st.pyplot(plot_img.figure)
