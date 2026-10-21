# CareerForge AI

## About the Project

CareerForge AI is a web application that helps users understand their resumes and explore career options using AI.

The project uses Django and Google's Gemini AI to analyze resumes and provide career suggestions, skill gap analysis, institute recommendations, and a learning roadmap.

## Features

- **Resume Analysis:** Upload your resume in PDF format and get an AI-generated analysis.
- **Skill Gap Analysis:** Find out which skills you need to improve.
- **Career Recommendations:** Get career suggestions based on your resume and skills.
- **Institute Recommendations:** Get suggestions for relevant institutes.
- **Learning Roadmap:** Get a step-by-step plan to learn new skills.
- **Save Results:** Your analysis and recommendations are saved so you can view them again.
- **Upload New Resume:** Upload another resume to get updated results.

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Google Gemini API
- SQLite
- PyPDF

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/NiharGadhia/CareerForge-AI
cd CareerForge-AI
```

Replace the repository URL with your actual GitHub repository link.

### 2. Create and Activate a Virtual Environment

```bash
python -m venv careerenv
careerenv\Scripts\activate
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Set Up the Gemini API Key

Create a `.env` file in the main `CareerForge-AI` folder and add your Gemini API key using the variable name expected by the project.

Do not upload your API key to GitHub.

### 5. Go to the Django Project Folder

```bash
cd careerforge
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Project

```bash
python manage.py runserver
```

Open this URL in your browser:

http://127.0.0.1:8000/

## How It Works

1. Upload a resume in PDF format.
2. The application reads the resume and analyzes it using Gemini AI.
3. View the resume analysis.
4. Check your skill gaps and career recommendations.
5. Explore institute recommendations.
6. Generate a learning roadmap to plan what to learn next.

## Project Goal

The goal of CareerForge AI is to make career planning easier by helping users understand their skills, explore career options, and decide what they should learn next.

## Author

Developed as an academic project using Django and Google's Gemini AI.