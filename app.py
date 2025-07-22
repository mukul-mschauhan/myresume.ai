from dotenv import load_dotenv
load_dotenv() # Load the local variables
import streamlit as st
from pdf import process_pdf
from analysis import analyse_profile

# create the front end of the application here...
st.header("Scan my :blue[CV.ai]📝", divider="green")
st.subheader("✅Tips for Using the Application")

notes = f'''
* **Upload the Resume (pdf only):** Please upload the resume in the pdf format only.
* **Paste the Job Desc:** Copy Paste the Job Desc below
* Unleash the Power of LLMs:** Use the power of LLMs to derive insights about the resume with respect to the JD'''
st.write(notes)

# sidebar
st.sidebar.subheader("Upload the Resume")
pdf_doc = st.sidebar.file_uploader("Upload the Resume", type=["pdf"])
st.sidebar.write("Created by Mukul Chauhan")

# Job Description Text Box
st.subheader("Enter the Job Description", divider=True)
job_desc = st.text_area(label="Enter the Job Description from Job Board(e.g.Linkedin)",
             max_chars=10000)
submit = st.button(label="Get AI Powered Insights")

if submit:
    st.markdown(analyse_profile(pdf_doc=pdf_doc, job_desc=job_desc))
