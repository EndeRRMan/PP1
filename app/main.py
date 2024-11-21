from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import random as rand

app = FastAPI()

@app.get('/')
def read_root():
    return {"Готов к работе"}

@app.get("/parse")
def Parse_Website():
    url = "https://example.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        h1 = soup.h1.string
        p = soup.p.string
        return (url, title, h1, p)

    else:
        return {"error": f"Не удалось получить доступ к {url}", "status_code": response.status_code}
