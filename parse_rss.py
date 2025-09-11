import feedparser

def print_latest_entries(feed_url, count=5):
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)
    entries = feed.entries[:count]

    print(f"Latest {len(entries)} entries from {feed_url}:")
    for entry in entries:
        title = entry.title
        link = entry.link
        print(f"- {title}\n  {link}")

if __name__ == "__main__":
    # Example: Replace with your RSS feed URL
    rss_url = "https://blog.python.org/feeds/posts/default"
    print_latest_entries(rss_url)
