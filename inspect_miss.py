import json

from retrieve import retrieve

CHUNKS_PATH = "data/geetachunks.json"
EVAL_PATH = "evals/questions.json"  # use your real path
CASE_ID = "GITA-EVAL-001"


def main() -> None:
    with open(CHUNKS_PATH, encoding="utf-8") as f:
        chunks = {chunk["id"]: chunk for chunk in json.load(f)}

    with open(EVAL_PATH, encoding="utf-8") as f:
        cases = json.load(f)["evaluation_cases"]

    case = next(c for c in cases if c["id"] == CASE_ID)
    print("QUESTION:", case["user_input"], "\n")

    print("=== EXPECTED ===")
    for v in case["expected_verses"]:
        verse_id = f'{v["chapter"]}.{v["verse"]}'
        print(verse_id, "|", chunks[verse_id]["text"], "\n")

    print("=== RETRIEVED ===")
    for verse_id, score in retrieve(case["user_input"], k=5):
        print(verse_id, round(score, 3), "|", chunks[verse_id]["text"], "\n")
print("THis ",retrieve("doing your duty without attachment to success or failure"))

if __name__ == "__main__":
    main()