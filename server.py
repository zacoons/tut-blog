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

# static

@app.route("/<filepath:path>")
def server_static(filepath):
    return bottle.static_file(filepath, "./static")

# only for testing: must be commented out when deploying
bottle.run(app)