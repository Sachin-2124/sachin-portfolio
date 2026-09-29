import urllib.request
import os

urls = [
    "https://archive.org/download/tvtunes_1000/Spider-Man%20%281994%29%20-%20Main%20Theme.mp3",
    "https://ia800500.us.archive.org/21/items/tvtunes_1000/Spider-Man%20%281994%29%20-%20Main%20Theme.mp3",
    "https://archive.org/download/tvtunes_12441/Spider-Man%20%281967%29%20-%20Main%20Theme.mp3"
]

target_dir = os.path.join(os.path.dirname(__file__), "static", "audio")
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "spiderman_theme.mp3")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

downloaded = False
for url in urls:
    try:
        print(f"Downloading from {url}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            if len(content) > 10000:
                with open(target_path, "wb") as f:
                    f.write(content)
                print(f"Successfully downloaded to {target_path} ({len(content)} bytes)")
                downloaded = True
                break
    except Exception as e:
        print(f"Failed from {url}: {e}")

if not downloaded:
    print("Could not download, creating local synthesized audio fallback.")
