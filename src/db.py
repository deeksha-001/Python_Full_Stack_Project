import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

#-----------
# MEMBERSHIP_PLANS TABLE
#-----------

def create_plan(name, duration_days):
    return supabase.table("membership_plans").insert({
        "name": name,
        "duration_days": duration_days
    }).execute()

def get_all_plans():
    return supabase.table("membership_plans").select("*").order("id").execute()

def update_plan(plan_id, data: dict):
    if not data:
        return {"error": "no data provided"}
    return supabase.table("membership_plans").update(data).eq("id", plan_id).execute()

def delete_plan(plan_id):
    return supabase.table("membership_plans").delete().eq("id", plan_id).execute()


#---------
# USERS TABLE
#---------
def create_user(name, email, join_date, membership_plan_id):
    return supabase.table("users").insert({
        "name": name,
        "email": email,
        "join_date": join_date,
        "membership_plan_id": membership_plan_id
    }).execute()

def get_all_users():
    return supabase.table("users").select("*").order("id").execute()

def update_user(user_id, data: dict):
    if not data:
        return {"error": "no data provided"}
    return supabase.table("users").update(data).eq("id", user_id).execute()

def delete_user(user_id):
    return supabase.table("users").delete().eq("id", user_id).execute()


# -------
# SESSIONS TABLE
# -------
def create_session(user_id, hours, workout_type, date=None):
    session_data = {
        "user_id": user_id,
        "hours": hours,
        "workout_type": workout_type
    }
    if date:
        session_data["date"] = date

    return supabase.table("sessions").insert(session_data).execute()

def get_all_sessions(user_id=None):
    query = supabase.table("sessions").select("*").order("id")
    if user_id:
        query = query.eq("user_id", user_id)
    return query.execute()

def update_session(session_id, data: dict):
    if not data:
        return {"error": "no data provided"}
    return supabase.table("sessions").update(data).eq("id", session_id).execute()

def delete_session(session_id):
    return supabase.table("sessions").delete().eq("id", session_id).execute()


# ----------
# WORKOUT_LOGS TABLE
# ----------
def create_workout_log(session_id, exercise, sets, reps):
    log_data = {
        "session_id": session_id,
        "exercise": exercise,
        "sets": sets,
        "reps": reps
    }
    return supabase.table("workout_logs").insert(log_data).execute()

def get_all_workout_logs(session_id=None):
    query = supabase.table("workout_logs").select("*").order("id")
    if session_id:
        query = query.eq("session_id", session_id)
    return query.execute()

def update_workout_log(log_id, data: dict):
    if not data:
        return {"error": "no data provided"}
    return supabase.table("workout_logs").update(data).eq("id", log_id).execute()

def delete_workout_log(log_id):
    return supabase.table("workout_logs").delete().eq("id", log_id).execute()
