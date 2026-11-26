import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI INTERVIEW ASSISTANT', layout='centered')
st.title('AI INTERVIEW ASSISTANT')
st.caption('Practice interviews with AI-generated questions and constructive feedback.')
st.caption('Launched by CHANDRAKANTH.')
st.write("Depatment of aids")

try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection succesful")
except (KeyError, FileNotFoundError):
  st.error('GROQ_API_KEY is missing. Add it to Streamlit Cloud -> App setting secrets')
  st.stop()


role = st.selectbox("Select Job Role",[
  "Python Developer",
  "Data Analyst",
  "Machine Learning Engineer",
  "Software Engineer",
  "HR Executive"
])

difficulties =  st.selectbox("Select Job Role",[
  "begineer",
  "intermediate",
  "pro"
])
  

if st.button("Generate Interview Questions"):

  prompt = "Generate 5 interview questions for the role of" +role +"with" +difficulties+ "difficulty"

  response = client.chat.completions.create(
     model="openai/gpt-oss-120b",
     messages=[
              {"role":"system","content":"You are an expert technical Interviwer"}, 
       {"role":"user","content":prompt}
     ]
  )
  output = response.choices[0].message.content
  st.write(output)
