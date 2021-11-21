import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import matplotlib.pyplot as plt
st.title("Hello World")
st.text('Bu bir text')
st.markdown('# This is a markdown text')
st.markdown('`this is a markdown text`')
st.header('this is a header')
st.subheader('this is subheader')
st.success('Congrats')
st.info('Warning!!!')
st.error('Error')
st.help(map)
st.write('this is a text written with write function')
img = Image.open('cat.jpg')
st.image(img,caption = 'Cat',use_column_width = True)
st.video('https://www.youtube.com/watch?v=eX2qFMC8cFo')
#checkbox
if st.checkbox('hide and seek'):
    st.write('Seek')

status = st.radio('What is your favorite color?',('red','green','blue'))    
st.write(f'your favorite color is {status}')
button = st.button('press me!!!')
if button:
    st.success('button just clicked')

number = st.selectbox('select a numver',(1,2,3,4,5))    
st.write(f'you choose {number}')

st.multiselect('select multiple numbers',[1,2,3])

st.slider('Select a number',0,9,3,2) # 3 default, 2 stepsize

name = st.text_input('Enter Your Name')
st.write(f'your name is {name}')

if st.button('Submit'):
    st.write(f'Hello {name.swapcase()} ')

st.text_area('Enter a message','let go')    

st.date_input('date')

st.time_input('time')

st.code('import pandas as pd')

with st.echo():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.DataFrame({'a': np.random.randint(1,10,5),
                      'b':np.arange(0,10,2)})
    df
    
st.sidebar.title('Side Bar')
st.sidebar.text_area('text in side bar')
st.sidebar.slider('input',0,5,1,1)

df = pd.read_csv('Mall_Customers.csv')
st.table(df.head(10))
st.sidebar.table(df.head().iloc[:3,:3])
st.write(df.head())  # dinamik

st.dataframe(df.head())

st.line_chart(df.Age)

slider = st.slider('x')
seri = np.random.randn(slider)
st.line_chart(seri)
st.write(seri.plot())



