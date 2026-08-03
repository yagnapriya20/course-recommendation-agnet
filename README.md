# 🎓 Course Recommendation Agent

## Overview

The Course Recommendation Agent is an AI-powered learning path recommendation system that helps students select suitable courses based on their educational background, current skills, and career goals.

The agent analyzes student information, checks course prerequisites from a course catalogue, generates an ordered learning path, and provides personalized explanations using an LLM.

---

## Features

- Accepts student profile information as input
- Considers educational background, current skills, and career goals
- Maintains a course catalogue with prerequisites
- Generates a personalized learning roadmap
- Provides reasons for each course recommendation
- Uses LLM-based explanations
- Produces structured output

---

## Agent Workflow

User Input  
↓  
Student Profile Analysis  
↓  
Load Course Catalogue  
↓  
Check Course Prerequisites  
↓  
Generate Learning Path  
↓  
LLM Generates Explanation  
↓  
Display Final Recommendation

---

## Project Structure

```
course-recommendation-agent/

│── app.py
│── recommender.py
│── llm.py
│── requirements.txt
│── README.md
│── .gitignore

│
├── database/
│     └── course_catalog.json

│
├── samples/
│     ├── student1.json
│     ├── student2.json
│     └── ...

│
└── outputs/
      ├── output1.txt
      ├── output2.txt
      └── ...
```

---

## Technologies Used

- Python
- JSON Database
- OpenAI API (LLM Integration)
- Python-dotenv
- Visual Studio Code

---

## Installation

### 1. Clone Repository

```
git clone <repository-url>
```

Navigate to the project folder:

```
cd course-recommendation-agent
```

### 2. Install Dependencies

Run:

```
python -m pip install -r requirements.txt
```

---

## API Configuration

This project uses an LLM API for generating personalized explanations.

Create a file named:

```
.env
```

inside the project folder.

Add your API key:

```
OPENAI_API_KEY=your_api_key_here
```

Do not upload the `.env` file to GitHub.

---

## Running the Agent

Run:

```
python app.py
```

The agent will ask for:

- Student name
- Educational background
- Current skills
- Career goal

After receiving the input, it generates a personalized learning path and AI-based career advice.

---

## Sample Input

```
Name:
Rahul

Background:
Mechanical Engineering

Skills:
Excel

Career Goal:
Data Scientist
```

---

## Sample Output

```
===== Personalized Learning Path =====

1. Python Basics

2. SQL Fundamentals

3. Data Analysis with Pandas

4. Machine Learning


===== AI Career Advice =====

Python builds programming fundamentals required for data science.

SQL helps in managing and querying data.

Data Analysis develops skills required for handling datasets.

Machine Learning introduces predictive modelling techniques.
```

---

## Course Catalogue

The course database contains:

- Course name
- Required skills
- Prerequisites
- Difficulty level

Example Learning Path:

```
Python Basics
      ↓
SQL Fundamentals
      ↓
Data Analysis with Pandas
      ↓
Machine Learning
      ↓
Deep Learning
```

---

## Design Choices

- JSON was selected as a lightweight database because it is simple and easy to modify.
- Rule-based prerequisite checking was implemented for transparent recommendations.
- LLM was used for generating personalized explanations and career guidance.

---

## Design Trade-offs

### Advantages

- Simple and easy to understand
- Fast execution
- Easy modification of course catalogue
- Explainable recommendations

### Limitations

- Small predefined course catalogue
- Requires API access for LLM responses
- Does not track long-term student progress

---

## Testing

The agent was tested with 10 different student profiles.

Test profiles included students from different backgrounds:

- Engineering
- Computer Science
- Commerce
- Mathematics

Each profile generated a personalized learning path.

Sample input files and generated outputs are available in:

```
samples/
outputs/
```

---

## Future Improvements

- Add a web interface using Streamlit
- Store user history using a database
- Add more courses and domains
- Use embeddings for advanced course matching
- Add student progress tracking
- Improve recommendations using user feedback

---

## Author

Created as part of an AI Agent Development Challenge.