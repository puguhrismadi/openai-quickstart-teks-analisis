import os
import json
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        teksinput = request.form["animal"]
        # response = openai.Image.create_variation(
        #     image=open("corgi_and_cat_paw.png", "rb"),
        #     n=1,
        #     size="1024x1024"
        # )
       
        response = openai.Image.create(
            prompt=teksinput,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        
        return redirect(url_for("index", result=image_url,teks=teksinput))

    result = request.args.get("result")
    return render_template("index.html", result=result)
@app.route("/moderasi", methods=("GET", "POST"))
def moderasi():
    if request.method == "POST":
        teksinput = request.form["tekstring"]
        response = openai.Moderation.create(
        input=teksinput,
        )
        python_obj = response['results'][0]['categories']
        print(python_obj)
        hasil =json.dumps(python_obj)
        
        return redirect(url_for("moderasi", result=hasil))

    result = request.args.get("result")
    return render_template("moderasi.html", result=result)
if __name__ == "__main__":
    app.run(host='0.0.0.0')