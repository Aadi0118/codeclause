from flask import Flask, request, redirect, url_for, render_template_string
import string
import random

app = Flask(__name__)

# In-memory database to store the short and actual URLs
url_db = {}

def generate_short_url():
    """Generate a random string of 6 characters for the short URL."""
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if short_url not in url_db:
            return short_url

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = generate_short_url()
        url_db[short_url] = original_url
        return render_template_string('''
            <p>Short URL: <a href="{{ url_for('redirect_to_url', short_url=short_url, _external=True) }}">{{ url_for('redirect_to_url', short_url=short_url, _external=True) }}</a></p>
            <p><a href="/">Shorten another URL</a></p>
        ''', short_url=short_url)
    return render_template_string('''
        <form method="post">
            <label for="original_url">Enter URL:</label>
            <input type="text" id="original_url" name="original_url" required>
            <input type="submit" value="Shorten">
        </form>
    ''')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = url_db.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return '<h1>URL not found</h1>', 404

if __name__ == '__main__':
    app.run(debug=True)
