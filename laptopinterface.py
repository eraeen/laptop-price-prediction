import streamlit as st
import pandas as pd
import pickle as p
import sys

st.title('laptop price prediction')

Brand = st.text_input('enter brand name')
Processor_Speed = st.number_input('enter processor speed')
RAM_Size = st.number_input('enter RAM size')
Storage_Capacity = st.number_input('enter Storage_Capacity')
Screen_Size = st.number_input('enter screen size')
Weight	= st.number_input('enter weight')



if st.button('predict'):
    in_pickle = open("laptop_price.pkl", 'rb')
    pipe = p.load(in_pickle)
    result = pd.DataFrame(
            [[Brand,Processor_Speed,RAM_Size,Storage_Capacity,Screen_Size,Weight]],
                              columns = ['Brand','Processor_Speed','RAM_Size','Storage_Capacity','Screen_Size','Weight'])
    r = pipe.predict(result)
            
    st.success('Predicted Laptop Price is : {}'.format(r))
    

