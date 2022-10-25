import streamlit as st

def st_ui():
  st.set_page_config(layout = "wide")
  st.title("Auto Review Legal contracts - DocumentAI")  
  fileupload = st.sidebar.file_uploader("Upload a Contract here")
  select_category = st.sidebar.selectbox("select_category", ["Summarization", "Sentiment Analytics", "Risk Analytics"])
  Button=st.sidebar.button('content Analytics')
  #button=st.sidebar.button('Risk Analytics')
  Enter_text = st.sidebar.text_input("Text to search")
        
if __name__ == "__main__":
  st_ui() 
