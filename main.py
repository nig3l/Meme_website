# from flask import Flask,render_template
# import requests
# import json


# app = Flask(__name__)

# def get_meme():
#     url = "https://meme-api.com/gimme"
#     response = json.loads(requests.request("GET",url).text)
#     meme_large = response["preview"][-2]
#     subreddit = response["subreddit"]
#     return meme_large,subreddit

# @app.route("/")
# def index ():
#     meme_pic, subreddit = get_meme()
#     return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)
# app.run(host = "0.0.0.0",port=80)

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    if "preview" in response and len(response["preview"]) >= 2:
        meme_large = response["preview"][-2]
    else:
        # Handle the case when "preview" doesn't exist or has fewer than two elements
        meme_large = None
    subreddit = response.get("subreddit")
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
