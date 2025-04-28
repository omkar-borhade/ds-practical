# server.py
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# HTML with basic Bootstrap
html_page = """
<!doctype html>
<html lang="en">
  <head>
    <title>Simple Web Service</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body class="text-center" style="margin-top: 100px;">
    <h1 class="mb-4">🌐 Welcome to the Web Service</h1>
    <p>This is a simple UI served from Flask.</p>
    <a href="/greet" class="btn btn-primary mt-3">Get JSON Greeting</a>
  </body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(html_page)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello from the Web Service!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
