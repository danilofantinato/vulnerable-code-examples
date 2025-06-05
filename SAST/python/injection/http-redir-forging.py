from flask import Flask, redirect, request
from urllib.parse import urlparse, urljoin

app = Flask("example")

@app.route("/redirect")
def redirect():
    url = request.args.get("url")
    if url:
        parsed_url = urlparse(url)
        allowed_hosts = ["example.com", "www.example.com"]
        if parsed_url.netloc in allowed_hosts:
            return redirect(url)
    return redirect("/")

if __name__ == "__main__":
    app.run()