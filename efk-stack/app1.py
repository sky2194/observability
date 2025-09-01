from flask import Flask
from prometheus_client import Counter, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
REQUEST_COUNT = Counter('app1_requests_total', 'Total requests to app1')

@app.route('/')
def index():
    REQUEST_COUNT.inc()
    return "Hello from App 1!"

# Add /metrics endpoint
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {'/metrics': make_wsgi_app()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)