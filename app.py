import streamlit as st
from queries import (
    get_active_mission,
    get_mission_progress,
    get_current_phase,
    get_phase_progress,
    get_current_milestone,
    get_next_task,
    mark_task_done,
)

st.set_page_config(
    page_title="Storyteller OS",
    page_icon="🎯",
    layout="centered",
)

st.markdown(
    """
    <style>
    .block-container { padding-top: 2.5rem; padding-bottom: 3rem; max-width: 720px; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; }
    .task-card {
        background-color: #f0f2f6;
        border-radius: 12px;
        padding: 1.5rem 1.5rem 1rem 1.5rem;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
    }
    .phase-pill {
        display: inline-block;
        background-color: #e8e2f7;
        color: #4b2e83;
        border-radius: 999px;
        padding: 0.15rem 0.9rem;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

try:
    mission = get_active_mission()
except Exception as e:
    st.error("Couldn't connect to the database. Check your connection and try again.")
    st.caption(f"Technical detail: {e}")
    st.stop()

if not mission:
    st.error("No active mission found.")
    st.stop()

mission_progress = get_mission_progress(mission["id"])

st.title(f"🎯 {mission['name']}")

col1, col2 = st.columns([3, 1])
with col1:
    st.progress(mission_progress["percent_complete"] / 100)
with col2:
    st.metric("Mission", f"{mission_progress['percent_complete']}%")
st.caption(
    f"{mission_progress['completed_tasks']} of {mission_progress['total_tasks']} tasks complete"
)

st.divider()

phase = get_current_phase(mission["id"])

if not phase:
    st.warning("No phases found for this mission yet.")
    st.stop()

phase_progress = get_phase_progress(phase["id"])

st.markdown(f'<span class="phase-pill">CURRENT PHASE</span>', unsafe_allow_html=True)
st.subheader(phase["name"])
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
    if mission_progress["percent_complete"] >= 100:
        st.balloons()
        st.success(f"🎉 Mission complete! You've finished every task in \"{mission['name']}\".")
    else:
        st.success("All tasks in this milestone are complete! Refresh shortly as more become available.")
else:
    st.markdown('<div class="task-card">', unsafe_allow_html=True)
    st.markdown("#### 🔥 What should I do RIGHT NOW?")
    st.markdown(f"### {task['title']}")
    if task.get("description"):
        st.write(task["description"])
    st.caption(f"📅 Scheduled for {task['scheduled_date']}")

    notes = st.text_input("Notes (optional)", key=f"notes_{task['id']}")

    if st.button("✅ DONE", type="primary", key=f"done_{task['id']}", use_container_width=True):
        mark_task_done(task["id"], notes if notes else None)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
