import streamlit as st 
import pandas as pd 
import numpy as np  
from datetime import time
appointment=st.slider("Programando la asesoria:",
                       value=(time(11,30), time(12, 45)),
                      format="HH:mm")
st.write("esta agendado para: {} a {}".format(appointment[0].strftime("%H:%M"), appointment[1].strftime("%H:%M")))
