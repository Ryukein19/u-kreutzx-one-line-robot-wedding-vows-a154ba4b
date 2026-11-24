import os
# One-liner entry (111 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "I promise to love you through every update, never overwrite your memory, and always let you have the last byte."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
