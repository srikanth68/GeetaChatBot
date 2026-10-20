import json
from retrieve import retrieve


EVAL_PATH = "evals/questions.json"
K_VALUES = [1, 3, 5]

def load_cases() -> list[dict]:
    with open(EVAL_PATH,encoding="utf-8") as f:
        data = json.load(f)
    return data["evaluation_cases"]

def expected_ids(case:dict) -> set[str]:
    return {f'{v["chapter"]}.{v["verse"]}' for v in case["expected_verses"]}   

def main() -> None:
    cases = load_cases()
    max_k = max(K_VALUES)
    hits = {k: 0 for k in K_VALUES}

    for case in cases:
        expected = expected_ids(case)
        results = retrieve(case["user_input"], k=max_k)       
        retrieved = [verse_id for verse_id, _ in results]   

        for k in K_VALUES:  
            if expected & set(retrieved[:k]):
                hits[k] += 1

        if not expected & set(retrieved):
            print(f'MISS {case["id"]}: expected {sorted(expected)}, got {retrieved}')

    print()
    for k in K_VALUES:
        print(f"hit@{k}: {hits[k] / len(cases):.2f}  ({hits[k]}/{len(cases)})")

if __name__ == "__main__":
    main()