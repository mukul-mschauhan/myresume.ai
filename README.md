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


