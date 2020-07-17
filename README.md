# py_scraper

Usage:
```pip install scrapy
scrapy crawl biorxiv -a search=<searchterm> -o <output>.json```

Converting json to csv:
```python scripts/json_to_cs.py <input>.json <output>.csv
