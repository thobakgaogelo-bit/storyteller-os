from db import get_client

client = get_client()

MISSION = {
    "name": "Become an AI Storyteller",
    "description": (
        "By Nov 30, 2026: able to take an idea from my life, turn it into a story, "
        "and tell that story convincingly using my AI clone, with a tested, locked-in "
        "storytelling concept and repeatable process."
    ),
    "start_date": "2026-09-08",
    "end_date": "2026-11-30",
}

PHASES = [
    {
        "name": "Storytelling Foundation",
        "start_date": "2026-09-08", "end_date": "2026-09-14",
        "milestones": [
            {"name": "Understand story structure", "tasks": [
                ("Watch/read 5 short-form storytellers' pieces; log the structure each follows (hook/tension/turn/payoff) in a table.", "2026-09-08"),
                ("Pick the 2 structures that resonated most; write one paragraph each on why.", "2026-09-09"),
            ]},
            {"name": "Define your storytelling voice", "tasks": [
                ('Write a 1-page definition of "a compelling story" for your content, in your own words.', "2026-09-10"),
            ]},
            {"name": '"Letters to My Princess" skeleton + raw material', "tasks": [
                ('Draft a rough skeleton of "Letters to My Princess" — who it\'s addressed to, what it\'s really about, why it matters (half page, not final).', "2026-09-11"),
                ("List 3 real personal life moments as candidate raw material for future story tests; one sentence each on why it could work.", "2026-09-14"),
            ]},
        ],
    },
    {
        "name": "Clone Development",
        "start_date": "2026-09-15", "end_date": "2026-09-24",
        "milestones": [
            {"name": "Tool evaluation", "tasks": [
                ("Test AI clone/avatar Tool 1; generate 1 image; record fidelity notes.", "2026-09-15"),
                ("Test Tool 2; generate 1 image; record fidelity notes.", "2026-09-16"),
                ("Test Tool 3; compare all three tools side by side; pick the leading candidate.", "2026-09-17"),
            ]},
            {"name": "Consistency testing", "tasks": [
                ("Using the leading tool, generate 5 variations of the same clone image from one reference; rate consistency 1-5 each.", "2026-09-18"),
                ("Adjust prompt/reference based on prior results; generate 5 more variations; re-rate.", "2026-09-21"),
                ("Compare both variation batches; select the single reference/prompt combo with the highest consistency.", "2026-09-22"),
            ]},
            {"name": "Lock reference + mood range", "tasks": [
                ("Lock the winning reference image/prompt set as the official clone baseline.", "2026-09-23"),
                ("Generate the locked clone in 3 moods (serious, warm, playful); save all three as reference assets.", "2026-09-24"),
            ]},
        ],
    },
    {
        "name": "Voice & Character/Presence",
        "start_date": "2026-09-25", "end_date": "2026-10-02",
        "milestones": [
            {"name": "Voice tool evaluation", "tasks": [
                ("Test AI voice-cloning/TTS Tool 1 with a 15-second sample script; record naturalness notes.", "2026-09-25"),
                ("Test Tools 2 and 3 with the same script; compare naturalness/emotional range across all three; pick a leading tool.", "2026-09-28"),
            ]},
            {"name": "Personality scripting", "tasks": [
                ('Write one 30-second script in "mentor" personality; generate voice.', "2026-09-29"),
                ('Write the same 30-second script in "storyteller-friend" personality; generate voice.', "2026-09-30"),
                ('Write the same script in "quiet reflective" personality; generate voice; compare all three and choose a direction.', "2026-10-01"),
            ]},
            {"name": "Voice + visual pairing", "tasks": [
                ("Write a 1-paragraph character brief for the chosen voice/personality; pair the locked visual clone with the locked voice in one test clip.", "2026-10-02"),
            ]},
        ],
    },
    {
        "name": "AI Visual Storytelling & Pipeline",
        "start_date": "2026-10-05", "end_date": "2026-10-14",
        "milestones": [
            {"name": "Video tool evaluation", "tasks": [
                ("Test AI video-generation Tool 1 using the locked clone; record facial-movement naturalness.", "2026-10-05"),
                ("Test Tool 2; record same notes.", "2026-10-06"),
                ("Test Tool 3; compare all three; select the leading video tool.", "2026-10-07"),
            ]},
            {"name": "Style comparison", "tasks": [
                ("Produce the same 15-second script in Style A (e.g., cinematic).", "2026-10-08"),
                ("Produce the same 15-second script in Style B (e.g., minimal talking-head); compare and choose a direction.", "2026-10-09"),
            ]},
            {"name": "Format + pipeline documentation", "tasks": [
                ("Define the output format — aspect ratio, length range, platform target.", "2026-10-12"),
                ("Draft the end-to-end tool-chain checklist (script -> voice -> video -> edit).", "2026-10-13"),
                ("Run the checklist once on a throwaway script to confirm it works start to finish; fix any broken step.", "2026-10-14"),
            ]},
        ],
    },
    {
        "name": 'Story Concepts & "Letters to My Princess"',
        "start_date": "2026-10-15", "end_date": "2026-10-22",
        "milestones": [
            {"name": "Concept expansion", "tasks": [
                ("Expand the Phase 1 skeleton into a full concept brief — premise, recurring format, tone, audience.", "2026-10-15"),
                ("Review the brief against the Nov 30 test question; tighten anything vague.", "2026-10-16"),
            ]},
            {"name": "Episode ideas", "tasks": [
                ('Write 3 candidate "episode" ideas under this concept, one paragraph each.', "2026-10-19"),
                ("Rank the 3 episode ideas; pick the strongest.", "2026-10-20"),
            ]},
            {"name": "Pressure test + cut list", "tasks": [
                ("Pressure-test the concept by mapping it onto one real personal life event; note where it breaks or works.", "2026-10-21"),
                ('Write the final "keep vs. cut" list for the concept based on the pressure test.', "2026-10-22"),
            ]},
        ],
    },
    {
        "name": "Hooks, Angles, Vibes & Formats",
        "start_date": "2026-10-23", "end_date": "2026-10-30",
        "milestones": [
            {"name": "Hook testing", "tasks": [
                ("Write the same story idea with 3 different opening hooks.", "2026-10-23"),
                ("Read/record all 3 hooks aloud; pick the strongest.", "2026-10-26"),
            ]},
            {"name": "Tone testing", "tasks": [
                ("Produce the story in Tone A (e.g., reflective).", "2026-10-27"),
                ("Produce the same story in Tone B (e.g., urgent); compare and pick a direction.", "2026-10-28"),
            ]},
            {"name": "Structural format testing + ranking", "tasks": [
                ("Test Structural Format A (single monologue) on one idea.", "2026-10-29"),
                ("Test Structural Format B (letter-read-aloud) on the same idea; rank all combinations tested this phase and pick the winning hook + tone + format.", "2026-10-30"),
            ]},
        ],
    },
    {
        "name": "Story Production",
        "start_date": "2026-11-02", "end_date": "2026-11-13",
        "milestones": [
            {"name": "Scripting", "tasks": [
                ("Select the real-life idea for the first finished story.", "2026-11-02"),
                ("Write the full script using the locked structure/hook/tone/format.", "2026-11-03"),
            ]},
            {"name": "Voice production", "tasks": [
                ("Record/generate the voice track using the locked voice.", "2026-11-04"),
                ("Review the voice track; re-record any weak lines.", "2026-11-05"),
            ]},
            {"name": "Video production", "tasks": [
                ("Generate the video using the locked clone and chosen visual style — scene 1.", "2026-11-06"),
                ("Generate remaining video scenes.", "2026-11-09"),
                ("Review all video segments; flag and regenerate any with visible clone inconsistency.", "2026-11-10"),
            ]},
            {"name": "Assembly", "tasks": [
                ("Assemble the rough cut (voice + video synced).", "2026-11-11"),
                ("Edit pass — trim pacing, fix transitions.", "2026-11-12"),
                ("Final export of the first finished story.", "2026-11-13"),
            ]},
        ],
    },
    {
        "name": "Testing, Refinement & Lock-In",
        "start_date": "2026-11-16", "end_date": "2026-11-30",
        "milestones": [
            {"name": "Feedback", "tasks": [
                ("Show the finished story to 3-5 people; collect direct reactions (no leading questions).", "2026-11-16"),
                ("Summarize the feedback into a single list of strengths and weaknesses.", "2026-11-17"),
            ]},
            {"name": "Refinement", "tasks": [
                ("Identify the single biggest weakness; plan the fix.", "2026-11-18"),
                ("Implement the fix and re-export the story.", "2026-11-19"),
            ]},
            {"name": "Second story (repeat the locked process)", "tasks": [
                ("Select the real-life idea for the second story.", "2026-11-20"),
                ("Write the second script using the exact same locked process, timing how long scripting takes.", "2026-11-23"),
                ("Produce voice + video for the second story, timing each stage.", "2026-11-24"),
                ("Assemble and edit the second story.", "2026-11-25"),
                ("Export the second story; compare total production time to the first.", "2026-11-26"),
            ]},
            {"name": "Lock-in", "tasks": [
                ('Run the final test — does the second story convincingly answer "can I take an idea from my life and tell it using my AI clone?" Record yes/no and why.', "2026-11-27"),
                ("Write the final \"locked-in\" 1-page storytelling identity doc (concept + voice + visual style + process). Mission complete.", "2026-11-30"),
            ]},
        ],
    },
]


def seed():
    mission_res = client.table("missions").insert(MISSION).execute()
    mission_id = mission_res.data[0]["id"]
    print(f"Mission created: {mission_id}")

    total_phases = total_milestones = total_tasks = 0

    for phase_order, phase in enumerate(PHASES, start=1):
        phase_res = client.table("phases").insert({
            "mission_id": mission_id,
            "name": phase["name"],
            "order_index": phase_order,
            "start_date": phase["start_date"],
            "end_date": phase["end_date"],
        }).execute()
        phase_id = phase_res.data[0]["id"]
        total_phases += 1
        print(f"  Phase {phase_order}: {phase['name']}")

        for milestone_order, milestone in enumerate(phase["milestones"], start=1):
            milestone_res = client.table("milestones").insert({
                "phase_id": phase_id,
                "name": milestone["name"],
                "order_index": milestone_order,
            }).execute()
            milestone_id = milestone_res.data[0]["id"]
            total_milestones += 1

            task_rows = [
                {
                    "milestone_id": milestone_id,
                    "title": title,
                    "scheduled_date": sched_date,
                    "order_index": i,
                }
                for i, (title, sched_date) in enumerate(milestone["tasks"], start=1)
            ]
            client.table("tasks").insert(task_rows).execute()
            total_tasks += len(task_rows)

    print(f"\nDone. Inserted {total_phases} phases, {total_milestones} milestones, {total_tasks} tasks.")


if __name__ == "__main__":
    seed()