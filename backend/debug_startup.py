import sys
import os
import traceback

print(f"CWD: {os.getcwd()}")
# print(f"Path: {sys.path}")

try:
    print("Attempting to import app.main...")
    from app.main import app
    print("SUCCESS: App imported")
except Exception:
    traceback.print_exc()
