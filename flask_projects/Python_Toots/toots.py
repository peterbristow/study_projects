"""Shows Toots."""
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Show Toots."""
    json_authors = open("data/authors.json")
    authors = json.load(json_authors)
    authors = {author['id']: author['name'] for author in authors}

    json_toots = open("data/toots.json")
    toots = json.load(json_toots)

    return render_template('index.html', authors=authors, toots=toots)


@app.route('/author/<author_name>')
def toot_threads_by_author(author_name):
    """Show Toot Threads."""
    # TODO: Implement me!
    return '<span>Specific Toot threads for {author_name}</span>'.format(
        author_name=author_name)


def render_toot(toot):
    """Render Toots."""
    author_name = 'Someone'  # FIXME
    text = 'Not a real Toot'  # FIXME

    return """
    <li>
        <span><a href="/author/{author_name}">{author_name}</a></span>
        <span>:</span>
        <span>{text}</span>
    </li>
    """.format(
        author_name=author_name,
        text=text,
    )
