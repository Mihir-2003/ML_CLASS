import requests
import pandas as pd
from datetime import datetime

TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def fetch_top_story_ids(limit=30):
    """Fetch top story IDs from HN API."""
    resp = requests.get(TOP_STORIES, timeout=15)
    resp.raise_for_status()
    ids = resp.json()
    return ids[:limit]


def fetch_story(item_id):
    """Fetch each story detail using item API."""
    url = ITEM_URL.format(item_id)
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.json()


def parse_stories(ids):
    """Parse 30 stories into clean structure."""
    items = []
    for item_id in ids:
        story = fetch_story(item_id)
        if not story:   # Skip null items
            continue

        items.append({
            "scraped_at": datetime.utcnow().isoformat() + "Z",
            "title": story.get("title"),
            "link": story.get("url"),
            "score": story.get("score", 0),
            "author": story.get("by"),
            "time": story.get("time"),
            "type": story.get("type"),
            "comments_count": story.get("descendants", 0),
            "item_id": story.get("id")
        })

    return items


def save_to_csv(items, filename="hackernews_latest_api.csv"):
    df = pd.DataFrame(items)
    df.to_csv(filename, index=False)
    return df


def main():
    print("Fetching top stories via API...")
    ids = fetch_top_story_ids(limit=30)

    print("Fetching story details...")
    items = parse_stories(ids)

    print(f"Fetched {len(items)} stories. Saving CSV...")
    df = save_to_csv(items)

    print("Done. Sample:")
    print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
