from flask import Flask
import redis

app = Flask(__name__)

cache = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    visits = cache.incr("visits")

    return f"""
    <h1>Hello Docker!</h1>
    <p>This page has been visited {visits} times.</p>
    """

app.run(
    host="0.0.0.0",
    port=5000
)
