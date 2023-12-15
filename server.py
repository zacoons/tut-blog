import bottle
from os import listdir
import markdown

app = bottle.Bottle()

def get_page(filename, **kwargs):
    base = bottle.template("pages/" + filename, **kwargs)
    return bottle.template("template.html", base=base)

@app.route("/")
def home():
    posts = listdir("posts")
    return get_page("posts.html", posts=posts)

@app.route("/post/<filename>")
def post(filename):
    md = open("posts/" + filename).read()
    content = markdown.markdown(md)
    return get_page("post.html", content=content)