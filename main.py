from flask import Flask,render_template
import requests
import json


app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["url"]
    subreddit = response["subreddit"]
    return meme_large,subreddit

@app.route("/")
def index ():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__": 
   app.run(host = "0.0.0.0", port=55000, debug=True)

