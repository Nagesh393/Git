
import pandas as pd 
import streamlit as st




def calc_time(qty, mins, workers, eff):
    total_work=qty*mins
    theo_mins=total_work/workers
    act_mins=(theo_mins/(eff/100))
    return act_mins/60


st.title("Garment Product Time Predictor")

garment = st.text_input("GARMENT")
quantity = st.number_input("QUANTITY", min_value=1, step=1)
workers = st.number_input("NO OF WORKERS", min_value=1, step=1)
time_per_garment = st.number_input("TIME PER GARMENT (minutes)")
efficiency = st.number_input("Efficiency")




if st.button("Predict Time",    type="primary", ):
    # prediction code

    if garment.strip()=="":
        st.error("Enter Garment Name")
    if quantity<=0:
        st.error("Enter Quantity")
    if workers<=0:
        st.error("Enter no of workers")
    if efficiency<=0:
        st.error("Efficiency cannot be zero")
    if time_per_garment<=0:
        st.error("Time cannot be zero")

    try:
        total_time = round(calc_time(quantity, time_per_garment, workers, efficiency))
        result=  {
            'garment': [garment],
            'quantity':[quantity],
            'workers':[workers],
            'time_per_garment':[time_per_garment],
            'efficiency':f"{efficiency}%",   
            'Estimated Production Time': f"{total_time}hr"
            }
        st.toast("Result Calculated")
        output=pd.DataFrame(result)
        st.dataframe(output, use_container_width=True)
    except ZeroDivisionError:
        (st.error("Error: Item With Any Value Zero Cannot Be Predicted"))

  

