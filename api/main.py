from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.append(src_path)

from logic import MembershipManager, UserManager, SessionManager, WorkoutLogManager

app = FastAPI(title="Fitness Tracker", version="1.0")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Managers
membership_manager = MembershipManager()
user_manager = UserManager()
session_manager = SessionManager()
workout_manager = WorkoutLogManager()

# ---- Schemas ----
class PlanCreate(BaseModel):
    name: str
    duration_days: int

class PlanUpdate(BaseModel):
    name: str | None = None
    duration_days: int | None = None

class UserCreate(BaseModel):
    name: str
    email: str
    join_date: str
    membership_plan_id: int

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    membership_plan_id: int | None = None

class SessionCreate(BaseModel):
    user_id: int
    hours: float
    workout_type: str
    date: str | None = None

class SessionUpdate(BaseModel):
    hours: float | None = None
    workout_type: str | None = None
    date: str | None = None

class WorkoutLogCreate(BaseModel):
    session_id: int
    exercise: str
    sets: int
    reps: int

class WorkoutLogUpdate(BaseModel):
    exercise: str | None = None
    sets: int | None = None
    reps: int | None = None

# ---- Routes ----
@app.get("/")
def home():
    return {"message": "Fitness Tracker API is running!"}

# --- Membership Plans ---
@app.get("/membership_plans")
def get_plans():
    return membership_manager.get_plans()

@app.post("/membership_plans")
def create_plan(plan: PlanCreate):
    result = membership_manager.add_plan(plan.name, plan.duration_days)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/membership_plans/{id}")
def update_plan(id: int, plan: PlanUpdate):
    result = membership_manager.update_plan(id, plan.dict(exclude_none=True))
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.delete("/membership_plans/{id}")
def delete_plan(id: int):
    result = membership_manager.delete_plan(id)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

# --- Users ---
@app.get("/users")
def get_users():
    return user_manager.get_users()

@app.post("/users")
def create_user(user: UserCreate):
    result = user_manager.add_user(user.name, user.email, user.join_date, user.membership_plan_id)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/users/{id}")
def update_user(id: int, user: UserUpdate):
    result = user_manager.update_user(id, user.dict(exclude_none=True))
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.delete("/users/{id}")
def delete_user(id: int):
    result = user_manager.delete_user(id)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

# --- Sessions ---
@app.get("/sessions")
def get_sessions(user_id: int | None = None):
    return session_manager.get_sessions(user_id)

@app.post("/sessions")
def create_session(session: SessionCreate):
    result = session_manager.add_session(session.user_id, session.hours, session.workout_type, session.date)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/sessions/{id}")
def update_session(id: int, session: SessionUpdate):
    result = session_manager.update_session(id, session.dict(exclude_none=True))
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.delete("/sessions/{id}")
def delete_session(id: int):
    result = session_manager.delete_session(id)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

# --- Workout Logs ---
@app.get("/workout_logs")
def get_logs(session_id: int | None = None):
    return workout_manager.get_workout_logs(session_id)

@app.post("/workout_logs")
def create_log(log: WorkoutLogCreate):
    result = workout_manager.add_workout_log(log.session_id, log.exercise, log.sets, log.reps)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/workout_logs/{id}")
def update_log(id: int, log: WorkoutLogUpdate):
    result = workout_manager.update_workout_log(id, log.dict(exclude_none=True))
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.delete("/workout_logs/{id}")
def delete_log(id: int):
    result = workout_manager.delete_workout_log(id)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

# --- Run server ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
