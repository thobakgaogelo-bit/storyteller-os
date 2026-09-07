from db import get_client

client = get_client()

# 1. INSERT
insert_result = client.table("missions").insert({
    "name": "CONNECTION TEST",
    "description": "Temporary — proves Python can write to Supabase",
    "start_date": "2026-01-01",
    "end_date": "2026-01-31"
}).execute()

test_id = insert_result.data[0]["id"]
print("Inserted row with id:", test_id)

# 2. READ
read_result = client.table("missions").select("*").eq("id", test_id).execute()
print("Read back:", read_result.data[0]["name"])

# 3. DELETE (cleanup)
client.table("missions").delete().eq("id", test_id).execute()
print("Deleted test row.")

# 4. CONFIRM CLEANUP
confirm = client.table("missions").select("*").eq("id", test_id).execute()
print("Rows remaining with that id:", len(confirm.data))
