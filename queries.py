from datetime import date
from db import get_client

def get_active_mission():
    client = get_client()
    result = client.table("missions").select("*").eq("status", "active").limit(1).execute()
    return result.data[0] if result.data else None

def get_mission_progress(mission_id):
    client = get_client()
    result = client.table("mission_progress").select("*").eq("mission_id", mission_id).execute()
    return result.data[0] if result.data else None

def get_current_phase(mission_id):
    """The current phase is the one containing the earliest pending task."""
    client = get_client()
    result = client.table("phases").select("*").eq("mission_id", mission_id).order("order_index").execute()
    for phase in result.data:
        milestones = client.table("milestones").select("id").eq("phase_id", phase["id"]).execute()
        milestone_ids = [m["id"] for m in milestones.data]
        if not milestone_ids:
            continue
        pending = client.table("tasks").select("id").in_("milestone_id", milestone_ids).eq("status", "pending").limit(1).execute()
        if pending.data:
            return phase
    return result.data[-1] if result.data else None

def get_phase_progress(phase_id):
    client = get_client()
    result = client.table("phase_progress").select("*").eq("phase_id", phase_id).execute()
    return result.data[0] if result.data else None

def get_current_milestone(phase_id):
    """The current milestone is the one containing the earliest pending task."""
    client = get_client()
    result = client.table("milestones").select("*").eq("phase_id", phase_id).order("order_index").execute()
    for milestone in result.data:
        pending = client.table("tasks").select("id").eq("milestone_id", milestone["id"]).eq("status", "pending").limit(1).execute()
        if pending.data:
            return milestone
    return result.data[-1] if result.data else None

def get_next_task(milestone_id):
    """The next task: earliest pending task by scheduled_date, then order_index."""
    client = get_client()
    result = client.table("tasks").select("*").eq("milestone_id", milestone_id).eq("status", "pending").order("scheduled_date").order("order_index").limit(1).execute()
    return result.data[0] if result.data else None

def mark_task_done(task_id, notes=None):
    client = get_client()
    update_data = {"status": "done", "completed_at": "now()"}
    if notes:
        update_data["notes"] = notes
    return client.table("tasks").update(update_data).eq("id", task_id).execute()
