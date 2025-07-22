# myresume.ai
Resume Analysis...

### Steps for Creating the Project
* Create the Virtual Environment using ``python -m venv .venv``
* Activate the Virtual Environment using ``source .venv/Scripts/activate``
* Create the .env file to store the API Key
* Create the requirements.txt file and add the libraries for installation using ``pip install -r requirements.txt``

### Project Synopsis
* We want to create an Application that will analyse the resume of the candidate using Gen AI model with the Job Desc and provide insights such as:-
- ATS Scores
- Probability of getting hired
- Keyword Analysis
- SWOT Analysis
- Suggestions for Overall Improvements

### Architecture
* app.py: Front end creation and output of the Genai Model.
It will have the feature of capturing information such as Resume and JD
* Information we are capturing is ``Resume.pdf`` and ``job_desc``.
* pdf.py that will process the information in pdf and thats why we have installed ``pypdf``
* analysis.py that will triangulate the pdf information and the JD and will provide insights and next step.

🚀 Project Overview
myresume.ai is an AI-powered resume analysis tool designed to assist job seekers in optimizing their resumes for specific job descriptions. By leveraging Generative AI models, this application provides valuable insights to enhance resume quality and alignment with job requirements.

🧠 Key Features
- ATS Score: Evaluate how well your resume is likely to perform with Applicant Tracking Systems.
- Probability of Success: Estimate your chances of getting hired based on resume-job description alignment.
- Keyword Analysis: Identify missing keywords and suggest relevant additions.
- SWOT Analysis: Assess your resume's Strengths, Weaknesses, Opportunities, and Threats in the context of the job description.
- Improvement Suggestions: Receive actionable tips to enhance resume content and structure.

⚙️ Technical Stack
- Backend: Python
- Web Framework: Streamlit
- NLP & AI: OpenAI's GPT models
- PDF Parsing: PyPDF2
- Environment Management: Python-dotenv

📄 Usage
- Upload your resume: Ensure your resume is in PDF format.
- Paste the job description: Input the job description you're targeting.
- Analyze: Click the "Analyze & Optimize" button to receive insights and suggestions.

🧪 Project Workflow
- Resume Upload: Users upload their resume in PDF format.
- Job Description Input: Users paste the job description into the provided field.
- Analysis: The application processes the inputs using AI models to generate insights.
- Results Display: Users receive a detailed report, including ATS score, keyword analysis, SWOT analysis, and improvement suggestions.
