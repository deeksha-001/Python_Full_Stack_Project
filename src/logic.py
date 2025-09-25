import db

class MembershipManager:
    """Handles membership_plans table operations."""

    def add_plan(self, name, duration_days):
        if not name or not duration_days:
            return {"success": False, "message": "Name & Duration are required"}
        result = db.create_plan(name, duration_days)
        return {"success": True, "data": result.data}

    def get_plans(self):
        result = db.get_all_plans()
        return {"success": True, "data": result.data}

    def update_plan(self, plan_id, data: dict):
        if not plan_id:
            return {"success": False, "message": "Plan ID is required"}
        result = db.update_plan(plan_id, data)
        return {"success": True, "data": result.data}

    def delete_plan(self, plan_id):
        if not plan_id:
            return {"success": False, "message": "Plan ID is required"}
        result = db.delete_plan(plan_id)
        return {"success": True, "data": result.data}


class UserManager:
    """Handles users table operations."""

    def add_user(self, name, email, join_date, membership_plan_id):
        if not (name and email and join_date and membership_plan_id):
            return {"success": False, "message": "All fields are required"}
        result = db.create_user(name, email, join_date, membership_plan_id)
        return {"success": True, "data": result.data}

    def get_users(self):
        result = db.get_all_users()
        return {"success": True, "data": result.data}

    def update_user(self, user_id, data: dict):
        if not user_id:
            return {"success": False, "message": "User ID is required"}
        result = db.update_user(user_id, data)
        return {"success": True, "data": result.data}

    def delete_user(self, user_id):
        if not user_id:
            return {"success": False, "message": "User ID is required"}
        result = db.delete_user(user_id)
        return {"success": True, "data": result.data}


class SessionManager:
    """Handles sessions table operations."""

    def add_session(self, user_id, hours, workout_type, date=None):
        if not (user_id and hours and workout_type):
            return {"success": False, "message": "User ID, hours, and workout type are required"}
        result = db.create_session(user_id, hours, workout_type, date)
        return {"success": True, "data": result.data}

    def get_sessions(self, user_id=None):
        result = db.get_all_sessions(user_id)
        return {"success": True, "data": result.data}

    def update_session(self, session_id, data: dict):
        if not session_id:
            return {"success": False, "message": "Session ID is required"}
        result = db.update_session(session_id, data)
        return {"success": True, "data": result.data}

    def delete_session(self, session_id):
        if not session_id:
            return {"success": False, "message": "Session ID is required"}
        result = db.delete_session(session_id)
        return {"success": True, "data": result.data}


class WorkoutLogManager:
    """Handles workout_logs table operations."""

    def add_workout_log(self, session_id, exercise, sets, reps):
        if not (session_id and exercise and sets and reps):
            return {"success": False, "message": "All fields are required"}
        result = db.create_workout_log(session_id, exercise, sets, reps)
        return {"success": True, "data": result.data}

    def get_workout_logs(self, session_id=None):
        result = db.get_all_workout_logs(session_id)
        return {"success": True, "data": result.data}

    def update_workout_log(self, log_id, data: dict):
        if not log_id:
            return {"success": False, "message": "Log ID is required"}
        result = db.update_workout_log(log_id, data)
        return {"success": True, "data": result.data}

    def delete_workout_log(self, log_id):
        if not log_id:
            return {"success": False, "message": "Log ID is required"}
        result = db.delete_workout_log(log_id)
        return {"success": True, "data": result.data}
