import requests
import concurrent.futures


# Mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def check_site_availability(url):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        return False

    except Exception as error:
        return False


websites_to_check = [
    "https://www.google.com/",
    "https://chatgpt.com/",
    "https://www.hello.com/",
    "https://www.stackoverflow.com",
    "https://www.noneexistent.example"
]

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(check_site_availability, websites_to_check)