import json
import os
import urllib.request
import base64

screens = ["Home", "Work", "Experience", "Social"]

for name in screens:
    with open(f"screens/{name}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
        # Save HTML
        if "htmlCode" in data:
            html_content = data["htmlCode"]
            if isinstance(html_content, dict):
                if "html" in html_content:
                    html_content = html_content["html"]
                else:
                    html_content = json.dumps(html_content, indent=2)
            
            with open(f"{name}.html", "w", encoding="utf-8") as html_file:
                html_file.write(html_content)
                print(f"Saved {name}.html")
        
        # Save Screenshot
        if "screenshot" in data:
            screenshot = data["screenshot"]
            if isinstance(screenshot, dict):
                # Maybe it has a URL or base64 field?
                if "downloadUrl" in screenshot:
                    screenshot = screenshot["downloadUrl"]
                else:
                    screenshot = None
            
            if screenshot:
                if screenshot.startswith("http"):
                    # Download URL
                    urllib.request.urlretrieve(screenshot, f"{name}.png")
                    print(f"Downloaded {name}.png")
                elif screenshot.startswith("data:image"):
                    # Decode Base64
                    header, encoded = screenshot.split(",", 1)
                    with open(f"{name}.png", "wb") as img_file:
                        img_file.write(base64.b64decode(encoded))
                    print(f"Decoded and saved {name}.png")
                else:
                    # Might be a plain url or base64 without header
                    print(f"Screenshot format unknown for {name}: {screenshot[:50]}...")
