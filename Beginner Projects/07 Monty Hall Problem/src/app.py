import time

import streamlit as st
from monty_hall import main

st.title(":abacus: Monty Hall Simulation")
num_of_game = st.number_input(
    "Enter number of games for simiulate",
    min_value=1, max_value=1000000,
    value=100
)

wins_switch = 0
wins_stay = 0

col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
chart1 = col1.line_chart(x=None, y=None, width=400, height=400)
chart1.add_rows([1.0])
col2.subheader("Win Percentage With Switching")
chart2 = col2.line_chart(x=None, y=None, width=400, height=400)
chart2.add_rows([1.0])

for i in range(num_of_game):
    wins_without_switch, wins_with_switch = main(1)

    wins_stay += wins_without_switch
    wins_switch += wins_with_switch
    chart1.add_rows([wins_stay / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
    time.sleep(0.01)
