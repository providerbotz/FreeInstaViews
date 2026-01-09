import requests
import time

url = "https://indianbestsmm.com/insta.php"


insta_url = input("Enter Instagram reel/post URL: ")

payload = {
    'user_link': insta_url
}

headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua': "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    'sec-ch-ua-mobile': "?0",
    'origin': "https://indianbestsmm.com",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://indianbestsmm.com/insta.php",
    'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i",
    'Cookie': "PHPSESSID=644c9fa32cb89d43c74c37d97c2d7f16"
}

#abbas_devs
count = int(input("Enter number of times to run: "))

for i in range(count):
    try:
        response = requests.post(url, data=payload, headers=headers, timeout=15)
        print(f"\nRun {i + 1} Response:")
        print(response.text)
    except Exception as e:
        print(f"\nRun {i + 1} Error:", e)

    time.sleep(2)
