import pickle
import streamlit as st


#loading the model
wine_model=pickle.load(open('wine_quality.sav','rb'))

#slidebar

st.title('Wine Quality Prediction\nMast Piyo Mast Raho')

col1,col2,col3,col4=st.columns(4)

with col1:
    fixed_acidity=st.text_input('Fixed Acidity')

with col2:
    volatile_acidity=st.text_input('Volatile Acidity')

with col3:
    citric_acid=st.text_input('Citric Acid')

with col4:
    residual_sugar=st.text_input('Residual Sugar')

with col1:
    chlorides=st.text_input('Chlorides')

with col2:
    free_sulfur_dioxide=st.text_input('Free Sulfur Dioxide')

with col3:
    total_sulfur_dioxide=st.text_input('Total Sulfur Dioxide')

with col4:
    density=st.text_input('Density')

with col1:
    pH=st.text_input('PH')

with col2:
    sulphates=st.text_input('Sulphates')

with col3:
    alcohol=st.text_input('Alcohol')

#var for pred data
wine_pred=''

#a button 
if st.button('Test The Quality Of Your Wine'):

    pred=wine_model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
        chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
        pH, sulphates, alcohol]])
    
    if(pred[0]==0):
        wine_pred='It is a Good Quality Wine'

    else:
        wine_pred='It is a Bad Quality Wine'

st.success(wine_pred)