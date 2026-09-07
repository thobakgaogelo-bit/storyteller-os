from db import get_client

client = get_client()

phase_id = "20a11f4c-0ad1-4bd1-99ac-409b1d0e7ba8"

all_phases = client.table("phases").select("id, name").execute()
print("ALL PHASES:")
for p in all_phases.data:
    print(" ", p["id"], "|", p["name"])

all_milestones = client.table("milestones").select("id, phase_id, name").execute()
print("ALL MILESTONES:")
for m in all_milestones.data:
    print(" ", m["id"], "| phase_id:", m["phase_id"], "|", m["name"])

matching = client.table("milestones").select("*").eq("phase_id", phase_id).execute()
print("MILESTONES MATCHING", phase_id, ":", matching.data)
