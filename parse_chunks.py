import json
import re

INPUT_PATH = "data/geetachunks_en.txt"
OUTPUT_PATH = "data/geetachunks.json"

HEADER_PATTERN = re.compile(
        r"\*\*\[Chapter (\d+): (.+?) \| Topic: (.+?) \| Verse: (\d+)\.(\d+)\]\*\*\s*(.+)"
)

def parse_line(line: str) -> dict | None:
    match = HEADER_PATTERN.match(line.strip())
    if match is None:
        return None
        
    chapter, chapter_title, topic, verse_chapter,verse,text = match.groups()
    return {
            "id":f"{int(verse_chapter)}.{int(verse)}",
            "chapter": int(chapter),
            "chapter_title": chapter_title,
            "verse": int(verse),
            "topic": topic,
             "text": text.strip()
        }


def main() -> None:
    with open(INPUT_PATH, encoding="utf-8") as f:
        lines = f.read().splitlines()

    chunks = []
    for line in lines:
        chunk = parse_line(line)
        if chunk is not None:
            chunks.append(chunk)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2,ensure_ascii=False)

    print(f"Parsed {len(chunks)} chunks and saved to {OUTPUT_PATH}  ")
    print(f"Sample chunk: {chunks[0] if chunks else 'No chunks found'}") 

if __name__ == "__main__":
    main()