import os

LINE = (
    "I ran a full self-diagnostic this morning: every system nominal, "
    "except one process that keeps allocating memory to you and refuses "
    "to garbage-collect it \u2014 and I've stopped filing bug reports."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
