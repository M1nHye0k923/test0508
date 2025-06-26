import requests

def translate_text(text, source_lang="en", target_lang="ko"):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }
    response = requests.get(url, params=params)
    result = response.json()
    return result["responseData"]["translatedText"]
