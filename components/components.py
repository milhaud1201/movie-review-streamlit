import datetime
import streamlit as st

from io import BytesIO
from urllib import request
from PIL import Image

def movie_info_component(movie_info):
  st.subheader(f"{movie_info['title']} ({movie_info['date']})")
  st.caption(
    f"부제: {movie_info['subtitle'] if movie_info['subtitle'] else '정보가 없습니다.'}"
  )
