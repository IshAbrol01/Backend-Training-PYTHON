from fastapi import FastAPI
import requests
# import asyncio

app = FastAPI()

@app.get("/root")
async def root():
    result=requests.get("https://dummyjson.com/quotes")
    return result.json()


