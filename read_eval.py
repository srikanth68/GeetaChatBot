import json

with open("evals/questions.json",encoding="utf-8") as f:
    evals = json.load(f)

print("Number of questions:", len(evals["evaluation_cases"]))

for q in evals["evaluation_cases"]:
    print(q["user_input"], "->", q["expected_verses"][0]["theme"])


with open("data/geetachunks.json", encoding="utf-8") as f:
    chunks = json.load(f)

chunk_ids = {chunk["id"] for chunk in chunks}

for case in evals["evaluation_cases"]:
    for v in case["expected_verses"]:
        verse_id = f'{v["chapter"]}.{v["verse"]}'
        if verse_id not in chunk_ids:
            print("MISSING:", case["id"], verse_id)