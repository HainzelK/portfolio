import urllib.request
import json
import sys
import os

API_KEY = "AQ.Ab8RN6KLWiEAWdYoipV7U0SpRVw4wI0R05vATEEDaj0VqbeGyg"
PROJECT_ID = "15898168527140177881"

screens = {
    "Home": "adaa420b44a042aea7a2678ded8bf7c6",
    "Work": "971d593766a6443eb66318962d1279c2",
    "Experience": "4d8b67c9af6249658e5063f3b8816bc3",
    "Social": "490065b556604f37a5727fc410cde781"
}

def fetch_screen(screen_id):
    url = f"https://stitch.googleapis.com/v1/projects/{PROJECT_ID}/screens/{screen_id}"
    req = urllib.request.Request(url, headers={"X-Goog-Api-Key": API_KEY})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {screen_id}: {e}")
        return None

def main():
    os.makedirs("screens", exist_ok=True)
    for name, s_id in screens.items():
        print(f"Fetching {name} ({s_id})...")
        data = fetch_screen(s_id)
        if data:
            with open(f"screens/{name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            
            # Print top level keys to understand structure
            print(f"Keys for {name}: {list(data.keys())}")
            # If there's 'html', print it or save it
            
if __name__ == "__main__":
    main()
