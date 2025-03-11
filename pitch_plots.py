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


# Get either game dates or game matchups, or both in list


# Read in files



# Make selection boxes


# Create pitch plot, capture image, and display

