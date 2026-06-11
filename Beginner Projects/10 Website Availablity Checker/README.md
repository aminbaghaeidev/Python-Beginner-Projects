# 🌐 Website Availability Checker

A fast Python script that checks whether a list of websites are online — using **multithreading** to send all requests simultaneously instead of one by one.

## How It Works

Without threading, checking 5 sites one by one might take 5 × 5s = 25 seconds in the worst case. With `ThreadPoolExecutor`, all requests run **in parallel**, so the total time is roughly equal to the slowest single request.

```
google.com      ──────► ✅
chatgpt.com     ──────► ✅
hello.com       ──────► ✅   (all at the same time)
stackoverflow   ──────► ✅
nonexistent     ──────► ❌
```

## Features

- Concurrent requests with `concurrent.futures.ThreadPoolExecutor`
- Custom `User-Agent` header to avoid bot-blocking
- 5-second timeout per request to avoid hanging
- Handles all exceptions gracefully — unreachable sites return `False`

## Getting Started

### Requirements

```bash
pip install requests
```

`concurrent.futures` is part of Python's standard library — no installation needed.

### Running the Script

```bash
python availability_checker.py
```

## Usage

Add or remove URLs from the `websites_to_check` list:

```python
websites_to_check = [
    "https://www.google.com/",
    "https://www.github.com/",
    "https://www.nonexistent.example"
]
```

You can also increase `max_workers` for checking a larger list of sites faster:

```python
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(check_site_availability, websites_to_check)
```

## Notes

- The script currently only treats status code `200` as available — codes like `301` or `403` return `False` even if the site is up
- `results` is a generator; to print the output pair it with the URLs like this:

```python
for url, is_available in zip(websites_to_check, results):
    status = "✅ Online" if is_available else "❌ Offline"
    print(f"{url} — {status}")
```
