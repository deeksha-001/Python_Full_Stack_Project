# 🏋️‍♀️ FitnessLog – Personal Fitness Tracker

**FitnessLog** is a full-stack **fitness tracking application** built with **React**, **Supabase (PostgreSQL)**, and **Python**.  
It helps users log workouts, track attendance, monitor progress, and visualize fitness data over time.

---

## 🚀 Features

- **User Registration & Login** (Supabase Auth)  
- **Workout Tracking**: Record exercises, sets, reps, weights, or hours spent.  
- **Attendance Log**: Track days attended each month.  
- **Progress Monitoring**: View summaries and charts of your activities.  
- **Responsive UI** built with React or Streamlit frontend.

---

## 🗄️ Database Schema (Supabase / PostgreSQL)

| Table          | Purpose                               | Key Columns (examples) |
|----------------|---------------------------------------|------------------------|
| **users**      | Stores user profiles                  | id, name, email, age, weight, height |
| **workouts**   | Logs individual workouts              | id, user_id, date, exercise, duration, calories |
| **attendance** | Tracks days attended per month        | id, user_id, date, status |
| **progress**   | Stores monthly progress summaries     | id, user_id, month, weight_change, notes |

---

## 📁 Project Structure

FITNESS_TRACKER/
|
|---src/        # core application login
|   |---db.py       # Database operations
|   |---logic.py    # business logic & task
|
|---api/        # Backend API
|   |---main.py     # FastAPI endpoints
|
|---frontend/   # Frontend application
|   |---app.py      # Streamlit web interface
|
|---requirements.txt    # Python Dependencies
|
|---README.md           # Project documentation
|
|---.env                # Python variables

## Quick Start

### Prerequisites

- Python 3.8 or higher
- A Supabase account
- Git(Push, Clone) 

## 1. Clone or Download the project
### Option 1: Clone with Git
git clone <repositary-url>

### Option 2: Download and extract the ZIP file

## 2. Install Dependencies

### Install all required Python packages
pip install -r requirements.txt

## 3. Set Up Supabase Database

1.Create a Supabase Project:

2.Create the Tasks Table:
- Go to the SQL Editor in your Supabase dashboard
- Run this command:

``` sql
CREATE TABLE membership_plans (
  id SERIAL PRIMARY KEY,          
  name TEXT NOT NULL,
  duration_days INT NOT NULL
);

```

3.**Get your credentials**:

## 4. Configure Environmental Variables

1. Create a `.env` file in the project root

2. Add your Supabase credentials tp `.env`:
SUPABASE_URL = your_project_url
SUPABASE_KEY = your_anon_key

## 5. Run the application

## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at 'http://localhost:8080'

## FastAPI backend

**cd api**
python main.py

The API will be available at 'http://localhost:8000'

## How to use

## Technical Details

### 🛠️ Tech Stack

- **Frontend**: React.js or Streamlit (Python)
- **Backend**: FastAPI (Python REST API framework)
- **Database**: Supabase (PostgreSQL)
- **Language**: Python 3.8+

### Key Components

1. **`src/db.py`**: Database operations
    - Handles all CRUD operations with Supabase

2. **`src/logic.py`**: Business logic
    - Task validation and processing.

## Troubleshooting

## Common Issues

1. **"Module not found" errors**
    - Make sure you've installed all dependencies:
    pip install -r requirements.txt
    - Check that you're running commands from the correct directory

## Future Enhancements

- **User Authentication Enhancements**: strengthen login/signup security, implement JWT-based sessions.  
- **Progress Tracking**: add charts for workouts, calories burned, and attendance trends.  
- **Goal Setting**: weekly or monthly targets for sessions or workout hours.  
- **Profile Customization**: allow profile picture, weight, height, and BMI tracking.  
- **Third-Party Integrations**: connect with APIs for calorie estimation or advanced fitness metrics.  

## Support

If you encounter any issues or have questions contact:
deekshareddy0126@gmail.com