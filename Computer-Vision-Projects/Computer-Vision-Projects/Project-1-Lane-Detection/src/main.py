"""Starter entry point for Road Lane Detection and Departure Warning.

Implement the task-specific pipeline and evaluation before claiming results.
"""
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]

def main():
    for name in ("results", "evaluation", "screenshots"):
        (PROJECT_DIR / name).mkdir(parents=True, exist_ok=True)
    print("Road Lane Detection and Departure Warning")
    print("Starter scaffold only: add dataset paths, implementation, and evaluation.")

if __name__ == "__main__":
    main()
