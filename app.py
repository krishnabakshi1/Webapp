import numpy as np
import pandas as pd
import pickle 
import streamlit as st

pickle_a=open("model.pkl","rb")
regressor=pickle.load(pickle_a) # our model

def predict_species(Weight,Length1,Length2,Length3,Height,Width):
    prediction=regressor.predict([[Weight,Length1,Length2,Length3,Height,Width]])
    return prediction 


def main():
    st.title("Fish Species Classifier") 
    html_temp="""
        <div>
        <h2>Fish Species</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    Weight=st.text_input("Weight")
    Length1=st.text_input("Length2")
    Length3=st.text_input("Length3")
    Height=st.text_input("Height") 
    Width=st.text_input("Width")
    result=""
    if st.button("Predict"):
        result=predict_species(Weight,Length1,Length2,Length3,Height,Width) 
    st.success("Fish Species is{}".format(result))
        
if __name__=='__main__':
    main()