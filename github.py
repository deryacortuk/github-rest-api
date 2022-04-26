from flask import Flask,render_template,request
import requests

app=Flask(__name__)

url ="https://api.github.com/users/"

@app.route('/',methods=["POST","GET"])
def index():
    if request.method=="POST":
        username =request.form.get("githubname")

        response =requests.get(url+username)

        response_repo =requests.get(url+username+"/repos")
        user =response.json()
        repo =response_repo.json()

        if "message" in user:
            return render_template("index.html",error="User is not found")

        return render_template("index.html",profile=user,repos=repo)
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)
