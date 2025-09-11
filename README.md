# RSS Feed Parser

This script allows you to parse any RSS feed (such as a blog's feed) and print the latest 5 entry titles and links.

## Features

- Parses RSS feeds using [feedparser](https://pythonhosted.org/feedparser/)
- Prints the latest 5 entries (title + link)
- Simple and easy to use

## Requirements

- Python 3.x
- [feedparser](https://pypi.org/project/feedparser/)

## Installation

Install feedparser using pip:

```bash
pip install feedparser
```

## Usage

1. Edit `parse_rss.py` and set your desired RSS feed URL for the `rss_url` variable.

2. Run the script:

```bash
python parse_rss.py
```

Example output:

```
Latest 5 entries from https://blog.python.org/feeds/posts/default:
- Python 3.12 Released!
  https://blog.python.org/2023/10/python-3120-is-now-available.html
- New Python Steering Council Members
  https://blog.python.org/2023/09/new-python-steering-council.html
...
```

## Customization

To fetch more or fewer entries, change the `count` argument in the `print_latest_entries()` function call.

## License

MIT

---
Made by [vmpxklblast](https://github.com/vmpxklblast)
