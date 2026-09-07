from queries import get_active_mission, get_mission_progress, get_current_phase, get_current_milestone, get_next_task

mission = get_active_mission()
print("Mission:", mission["name"], "| id:", mission["id"])

progress = get_mission_progress(mission["id"])
print("Progress:", progress["percent_complete"], "%")

phase = get_current_phase(mission["id"])
print("Current phase:", phase["name"], "| id:", phase["id"])

milestone = get_current_milestone(phase["id"])
print("Current milestone:", milestone)
