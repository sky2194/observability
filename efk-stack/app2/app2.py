from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("App2 endpoint called")
    return "Hello from App2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)