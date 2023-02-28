import requests


def Info(title):
    url = f"https://moviesdatabase.p.rapidapi.com/titles/search/title/{title}"
    querystring = {"exact": "false"}
    headers = {
        "X-RapidAPI-Key": "11d370affdmsh368155118513778p1d5b3cjsnd43f6eaa93d2",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()
    # print(result["results"][0]["titleText"]["text"])

