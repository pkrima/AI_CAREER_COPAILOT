# 🚀 AI Career Copilot

AI Career Copilot is an intelligent web application designed to help job seekers optimize their career trajectory. Upload your resume (PDF or DOCX) along with your dream target role to receive instant AI-powered skill extraction, gap analysis, a personalized roadmap, and role-specific interview preparation questions.

---

## ✨ Features

- 📄 **Resume Parsing**: Seamlessly extract text from `.pdf` and `.docx` files.
- 🎯 **Target Role Gap Analysis**: Identifies your current skills vs. skills required for your target job title.
- 🗺️ **Personalized Roadmap**: Step-by-step actionable recommendations (projects, certifications, frameworks).
- 💡 **Interview Prep**: Tailored behavioral and technical interview questions based on your resume.
- 📂 **Project Tracker**: Manage and track your personal portfolio projects with progress statuses.
- 📜 **Analysis History**: View past resume reviews and track your improvements over time.
- 🤖 **Multi-AI Engine**: Powered by Google Gemini (`gemini-2.0-flash`), OpenAI (`gpt-4o-mini`), or Smart Offline Fallback Mode.
- 🗄️ **Flexible Database**: Supports local SQLite out of the box, with TiDB Cloud / MySQL support for production.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask, SQLAlchemy, Gunicorn
- **AI Models**: Google GenAI SDK (`google-genai`), OpenAI SDK
- **File Parsing**: `PyPDF2`, `python-docx`
- **Database**: SQLite (default) / TiDB Cloud (MySQL compatible)
- **Frontend**: Responsive HTML5, Vanilla CSS (Glassmorphism UI)

---

## 🚀 Live Deployment Guide (Free on Render)

Since this project has a Python Flask backend and database, it cannot run on GitHub Pages (which only supports static HTML). Follow these steps to make your project live for **FREE** using Render:

### Step 1: Push your code to GitHub
Make sure your latest code is pushed to your GitHub repository:
```bash
git add .
git commit -m "Configure production deployment"
git push origin main
```

### Step 2: Connect to Render.com
1. Go to [Render.com](https://render.com) and click **Sign Up** (or log in with your GitHub account).
2. Click **New +** at the top right and select **Web Service**.
3. Choose **Build and deploy from a Git repository**.
4. Select your repository: `AI_CAREER_COPAILOT`.

### Step 3: Configure Settings
Render will auto-detect settings or you can set:
- **Name**: `ai-career-copilot`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Free

### Step 4: Environment Variables (Optional)
Under the **Environment Variables** section on Render, add:
- `FLASK_SECRET_KEY`: *(Generate any random string)*
- `GEMINI_API_KEY`: *(Your Google AI Studio API key - free from https://aistudio.google.com/)*
- *(Optional)* `DEMO_MODE`: `false` (or leave empty; smart analysis will run if no API key is provided)

Click **Create Web Service**. Within 2-3 minutes, your project will be **LIVE** at a public URL like:
`https://ai-career-copilot.onrender.com` 🎉

---

## 💻 Local Setup & Development

### 1. Clone the repository
```bash
git clone https://github.com/pkrima/AI_CAREER_COPAILOT.git
cd AI_CAREER_COPAILOT
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Add your `GEMINI_API_KEY` (optional, smart fallback mode works without it).

### 5. Run the application
```bash
python app.py
```
Open your browser and navigate to: [http://localhost:5000](http://localhost:5000)

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
