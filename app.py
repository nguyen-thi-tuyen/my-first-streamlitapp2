# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
# First some MPG Data Exploration
def load_data(path):
    df = pd.read_csv(path)
    return df
mpg_df_raw = load_data(path="mpg.csv")
mpg_df = deepcopy(mpg_df_raw)
## Add some titles
st.title("Introduction to streamlit")
st.header("MPG Data Exploration")

#st.table(data=mpg_df)

if st.checkbox("Show dataframe"):
    st.dataframe(data=mpg_df)

# Scatter plot of displ vs hwy for year=2008
#matplotlib
import matplotlib.pyplot as plt
m_fig,ax = plt.subplots(figsize=(10,8))
mpg_2008 = mpg_df[mpg_df["year"]==2008]
ax.scatter(x=mpg_2008["displ"],y=mpg_2008["hwy"])
ax.set_title("Engine Size vs Highway Fuel Mileage")
ax.set_xlabel("Displacement")
ax.set_ylabel("MPG")
st.pyplot(m_fig)



#plotly

p_fig = px.scatter(mpg_df[mpg_df["year"]==2008], x='displ', y='hwy', opacity=0.5,
                   range_x=[1, 8], range_y=[10, 50],
                   width=750, height=600,
                   labels={"displ": "Displacement (Liters)",
                           "hwy": "MPG"},
                   title="Engine Size vs. Highway Fuel Mileage")
st.plotly_chart(p_fig)

plot_type = st.radio("Choose plot type",["Matplotlib","Plotly"])

#st.text(plot_type)

if plot_type=='Matplotlib':
    st.pyplot(m_fig)
else:
    st.plotly_chart(p_fig)



