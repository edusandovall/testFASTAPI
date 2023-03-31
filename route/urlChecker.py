from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from selenium import webdriver
from langdetect import detect

url_checker = APIRouter()

@url_checker.get('/getUrl')
async def analize_url(url: str):
    
    #Analice if page is translated to Hindi
    try:
        language = detect(url)
        # driver = webdriver.Firefox()
        # driver.get(url)
        # language= driver.find_element
    except:
        raise HTTPException(status_code=400, detail="Invalid URL")
    
    if language == 'hi': {"display_message": "PASS"}
    else: {"display_message": "FAIL"} 