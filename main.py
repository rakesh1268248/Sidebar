import streamlit as st
import pandas as pd
import numpy as np

def st_ui():
  st.set_page_config(layout = "wide")
  st.title("Auto Review Legal contracts - DocumentAI")  
  fileupload = st.sidebar.file_uploader("Upload a Contract here")
  select_category = st.sidebar.selectbox("select_category",["Summarization", "Sentiment Analytics", "Risk Analytics","Price Analytics","People/Stakeholders Analytics","Spatial Analytics",
                                                             "Text To Search","Grid Analytics","Social Analytics","Conversation-Transcripts Analytics","Non English Text","Filter Non English",
                                                            "List Of Languages","Display Full English Version","Full Document Translation"])
  Button=st.sidebar.button('content Analytics')
  #button=st.sidebar.button('Risk Analytics')
  Enter_text = st.sidebar.text_input("Text to search")
  df = pd.DataFrame([[  37.7790262 , -122.419906  ],
       [  37.6535403 , -122.4168664 ],
       [  29.6330078 ,  -97.98859404],
       [  38.6920451 ,  -75.4013315 ],
       [  51.4534963 ,    0.21878742],
       [  39.4225192 , -111.714358  ],
       [  52.45777545,   -1.86920994],
       [  36.5748441 ,  139.2394179 ]],columns=['lat', 'lon'])
  st.map(df)
        
if __name__ == "__main__":
  st_ui() 
