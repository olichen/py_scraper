# py_scraper

Installation
```git clone https://github.com/olichen/py_scraper.git
cd py_scraper/
pip install scrapy```

Usage:
```scrapy crawl biorxiv -a search=<searchterm> -o <output>.json```

Converting json to csv:
```python scripts/json_to_cs.py <input>.json <output>.csv
