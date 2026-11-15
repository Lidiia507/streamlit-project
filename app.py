import streamlit as st

st.title("Мій перший додаток у хмарі")
st.write("Все працює!")
float_slider = widgets.FloatSlider(
    value=5.5,               
    min=0.0,                
    max=10.0,              
    step=0.1,                
    description='Коефіцієнт:', 
    disabled=False,         
    continuous_update=False,
    orientation='horizontal',
    readout=True,            
    readout_format='.2f'     

    )

