# Applicant Tracking System (ATS)

A full-stack web application that allows candidates to apply for jobs and track application status, while recruiters manage applications through an admin dashboard.

## Features
- User authentication (login/logout)
- Job listings
- Apply to jobs with resume upload
- Application status tracking
- Admin panel for recruiters
- Secure backend using Django

## Tech Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite
- Authentication: Django Auth

## Project Workflow
Candidate → Apply for Job → Upload Resume → Track Status  
Recruiter → Add Jobs → View Applications → Update Status

## How to Run
```bash
python manage.py migrate
python manage.py runserver
