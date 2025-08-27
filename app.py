# https://docs.streamlit.io/
#เนื้อหา
#import streamlit as st
#st.write('สวัสดี นภสร')
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.write("สวัสดี บูม")

x = np.array([5,15,25,35,45,55,22,30]).reshape(-1, 1)#เปลี่ยนจาก1มิติเป็น2มิติ
y = np.array([5,20,14,32,22,38,11,15])

file_name = 'price_model.ml'
load_model = pickle.load(open(file_name, 'rb'))
r2 = load_model.score(x, y)

st.write(r2)
#map_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#    columns=['lat', 'lon'])

#st.map(map_data)

#import streamlit as st
#x = st.slider('x')  # 👈 this is a widget
#st.write(x, 'squared is', x * x)

#if st.checkbox('Show dataframe'):
#    chart_data = pd.DataFrame(
#       np.random.randn(20, 3),
#       columns=['a', 'b', 'c'])

#    chart_data

#df = pd.DataFrame({
#    'first column': [1, 2, 3, 4],
#    'second column': [10, 20, 30, 40]
#    })

#option = st.selectbox(
#    'Which number do you like best?',
#     df['second column'])

#'You selected: ', option

# Add a selectbox to the sidebar:
#add_selectbox = st.sidebar.selectbox(
#    'How would you like to be contacted?',
#    ('Email', 'Home phone', 'Mobile phone')
#)
# Add a slider to the sidebar:
#add_slider = st.sidebar.slider(
#    'Select a range of values',
#    0.0, 100.0, (25.0, 75.0)
#)

#left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
#left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
#with right_column:
#    chosen = st.radio(
#        'Sorting hat',
#        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#    st.write(f"You are in {chosen} house!")


#import time

#'Starting a long computation...'

# Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)

#for i in range(10):
#  # Update the progress bar with each iteration.
#  latest_iteration.text(f'Iteration {i+1}')
#  bar.progress(i + 1)
#  time.sleep(0.1)

#'...and now we\'re done!'

#if "counter" not in st.session_state:
#    st.session_state.counter = 0

#st.session_state.counter += 1

#st.header(f"This page has run {st.session_state.counter} times.")
#st.button("Run it again")


# import streamlit as st

# conn = st.connection("my_database")
# df = conn.query("select * from film")
# st.dataframe(df)
