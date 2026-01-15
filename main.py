import streamlit as st
import pandas as pd

st.title("📊 Любими неща – класна анкета")

if "colors" not in st.session_state:
  st.session_state.colors = {
    "Червен": 0,
    "Син": 0,
    "Зелен": 0,
    "Жълт": 0,
  }
  
if "sports" not in st.session_state:
  st.session_state.sports = {
    "Футбол": 0,
    "Баскетбол": 0,
    "Волейбол": 0,
    "Плуване": 0,
  }

color = st.selectbox("Любим цвят:", list(st.session_state.colors.keys()))
sport = st.selectbox("Любим цвят:", list(st.session_state.sports.keys()))

if st.button("Запази избора"):
  st.session_state.colors[color] += 1
  st.session_state.colors[sport] += 1
  st.success("Избора е записан")

st.divider()

st.subheader("Резултати")

# Графика за цветовете
st.write("Любими цветове")
colors_df = pd. DataFrame.from_dict(
df = pd.DataFrame.from_dict(st.session_state.colors, orient="index", columns=["Брой"])
st.bar_chart(colors_df)
)
# Графика за спортовете
st.write("Любими спортове")
sports_df = pd.DataFrame.from_dict(
  df = pd.DataFrame.from_dict(st.session_state.sports, orient="index", columns=["Брой"])
)
st.bar_chart(sports_df)


