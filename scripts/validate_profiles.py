import json, sys, pathlib

REQUIRED = {"name", "model_id", "strength_tags",
            "license", "role_candidate", "contact"}

for p in pathlib.Path("ai_profiles").glob("*.json"):
    data = json.loads(p.read_text())
    missing = REQUIRED - data.keys()
    if missing:
        print(f"{p.name}: missing {missing}")
        sys.exit(1)

print("All profiles valid 🎉")
