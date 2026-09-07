import streamlit as st
from queries import (
    get_active_mission,
    get_mission_progress,
    get_current_phase,
    get_phase_progress,
    get_current_milestone,
    get_next_task,
)

st.set_page_config(page_title="Storyteller OS", layout="centered")

mission = get_active_mission()

if not mission:
    st.error("No active mission found.")
    st.stop()

mission_progress = get_mission_progress(mission["id"])

st.title(mission["name"])
st.progress(mission_progress["percent_complete"] / 100)
st.caption(
    f"{mission_progress['completed_tasks']} of {mission_progress['total_tasks']} tasks complete "
    f"({mission_progress['percent_complete']}%)"
)

st.divider()

phase = get_current_phase(mission["id"])

if not phase:
    st.warning("No phases found for this mission yet.")
    st.stop()

phase_progress = get_phase_progress(phase["id"])

st.subheader(f"Current Phase: {phase['name']}")
st.progress(phase_progress["percent_complete"] / 100)
st.caption(f"{phase_progress['percent_complete']}% of this phase complete")

milestone = get_current_milestone(phase["id"])

if not milestone:
    st.warning("No milestones found for this phase yet.")
    st.stop()

st.markdown(f"**Milestone:** {milestone['name']}")

st.divider()

task = get_next_task(milestone["id"])

if not task:
    st.success("All tasks in this milestone are complete!")
else:
    st.subheader("What should I do RIGHT NOW?")
    st.markdown(f"### {task['title']}")
    if task.get("description"):
        st.write(task["description"])
    st.caption(f"Scheduled for {task['scheduled_date']}")
